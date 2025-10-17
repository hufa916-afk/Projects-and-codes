#!/usr/bin/env python3
"""
auth_log_bruteforce_detector.py
Scans an auth log for repeated 'failed' login attempts by IP.
Usage:
  python3 auth_log_bruteforce_detector.py /path/to/auth.log --threshold 5
"""
import re
import sys
from collections import defaultdict
import argparse

FAIL_PATTERNS = [
    re.compile(r'Failed password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)'),
    re.compile(r'authentication failure;.*rhost=(?P<ip>\d+\.\d+\.\d+\.\d+)'),
    re.compile(r'Invalid user .* from (?P<ip>\d+\.\d+\.\d+\.\d+)'),
]

def scan_log(path, threshold=5, window_lines=None):
    ip_counts = defaultdict(int)
    lines_checked = 0
    with open(path, 'r', errors='ignore') as fh:
        for line in fh:
            lines_checked += 1
            for pat in FAIL_PATTERNS:
                m = pat.search(line)
                if m:
                    ip = m.group('ip')
                    ip_counts[ip] += 1
    report = {ip: cnt for ip, cnt in ip_counts.items() if cnt >= threshold}
    return report, lines_checked, sum(ip_counts.values())

def main():
    p = argparse.ArgumentParser()
    p.add_argument('logfile', help='Path to auth-style log file')
    p.add_argument('--threshold', type=int, default=5, help='Number of failed attempts to flag IP')
    args = p.parse_args()
    report, lines, total = scan_log(args.logfile, threshold=args.threshold)
    print(f"Scanned {lines} lines, {total} failed attempts found.")
    if not report:
        print("No suspicious IPs found.")
        return
    print("Suspicious IPs (attempts >= threshold):")
    for ip, cnt in sorted(report.items(), key=lambda x: -x[1]):
        print(f"  {ip}  -> {cnt} failed attempts")
    print("\nSuggested actions:")
    print(" - Investigate logs for top IPs.")
    print(" - Block suspicious IPs at firewall or cloud provider if malicious.")
    print(" - Consider rate-limiting or 2FA.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
generate_deploy_apply.py
Generate a K8s Deployment YAML and optionally apply it using kubectl.
Usage:
  python3 generate_deploy_apply.py --name myapp --image nginx:stable --replicas 2 --apply
"""
import argparse
import subprocess
import sys
import yaml  # only used for pretty output if available; fallback to manual yaml

def build_deployment(name, image, replicas, port):
    dep = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": name, "labels": {"app": name}},
        "spec": {
            "replicas": replicas,
            "selector": {"matchLabels": {"app": name}},
            "template": {
                "metadata": {"labels": {"app": name}},
                "spec": {
                    "containers": [
                        {"name": name, "image": image, "ports": [{"containerPort": port}]}
                    ]
                },
            },
        },
    }
    return dep

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--replicas", type=int, default=1)
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--apply", action="store_true", help="Apply with kubectl apply -f -")
    args = parser.parse_args()

    deployment = build_deployment(args.name, args.image, args.replicas, args.port)

    try:
        import yaml as _yaml
        printed = _yaml.safe_dump(deployment, sort_keys=False)
    except Exception:
        # simple manual dump if PyYAML not installed
        import json
        printed = json.dumps(deployment, indent=2)
    print("Generated deployment YAML/JSON:")
    print(printed)

    if args.apply:
        print("Applying to cluster with kubectl...")
        p = subprocess.Popen(["kubectl", "apply", "-f", "-"], stdin=subprocess.PIPE)
        out, _ = p.communicate(input=printed.encode())
        if p.returncode == 0:
            print("kubectl apply succeeded.")
        else:
            print("kubectl apply failed. Return code:", p.returncode)
            sys.exit(p.returncode)

if __name__ == "__main__":
    main()

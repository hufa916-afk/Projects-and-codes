#!/usr/bin/env python3
"""
ai_text_detector.py
Heuristic detection of "AI-like" text. Not machine-learning, just interpretable signals.
Usage: python3 ai_text_detector.py "text to analyze"
"""
import sys
import re
import statistics
from collections import Counter

def tokenize_sentences(text):
    # naive split
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sents if s]

def word_features(text):
    words = re.findall(r"\w+'?\w*|\w+", text.lower())
    return words

def score_ai_like(text):
    sents = tokenize_sentences(text)
    words = word_features(text)
    if not words:
        return 0.0, {}

    # Feature 1: sentence length uniformity (AI often produces similar-length sentences)
    sent_lens = [len(re.findall(r'\w+', s)) for s in sents] or [0]
    try:
        uniformity = 1.0 - (statistics.stdev(sent_lens) / (statistics.mean(sent_lens) + 1e-6))
    except statistics.StatisticsError:
        uniformity = 0.0

    # Feature 2: repetition ratio (AI sometimes repeats phrases)
    counts = Counter(words)
    rep_ratio = sum(v for v in counts.values() if v > 1) / len(words)

    # Feature 3: punctuation variety (AI may use less exclamation or question variety)
    punct = Counter(re.findall(r'[^\w\s]', text))
    punct_variety = len(punct) / (sum(punct.values()) + 1e-6)

    # Feature 4: average word length
    avg_word_len = sum(len(w) for w in words) / len(words)

    # Combine heuristically into a score 0..1 where higher = more "AI-like"
    score = 0.4 * max(0, uniformity) + 0.3 * rep_ratio + 0.2 * (1.0 - punct_variety) + 0.1 * (avg_word_len / 6.0)
    score = max(0.0, min(1.0, score))
    features = {
        "uniformity": round(uniformity,3),
        "rep_ratio": round(rep_ratio,3),
        "punct_variety": round(punct_variety,3),
        "avg_word_len": round(avg_word_len,3),
    }
    return score, features

def demo_texts():
    human = "I visited the market today and bought apples, bananas, and some bread. The weather was pleasant. I met an old friend and we chatted for a while."
    ai_like = ("This product offers innovative features and enhanced performance. "
               "It delivers superior results across a wide range of tasks. "
               "Users will appreciate the high-quality experience and the robust support.")
    for t in (human, ai_like):
        score, feats = score_ai_like(t)
        print("Text:", t)
        print("Score:", score, "Features:", feats)
        print("-"*40)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        score, feats = score_ai_like(text)
        print("AI-like score:", score)
        print("Features:", feats)
    else:
        demo_texts()

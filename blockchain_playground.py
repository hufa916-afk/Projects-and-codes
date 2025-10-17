#!/usr/bin/env python3
"""
simple_blockchain.py
A minimal proof-of-work blockchain for demonstration and testing.
Run: python3 simple_blockchain.py
"""
import hashlib
import json
import time
from typing import List, Dict

class Block:
    def __init__(self, index:int, timestamp:float, data:Dict, previous_hash:str, nonce:int=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class SimpleChain:
    def __init__(self, difficulty:int=3):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, time.time(), {"genesis": True}, "0")
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, block:Block) -> str:
        prefix = "0" * self.difficulty
        while not block.hash.startswith(prefix):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block.hash

    def add_block(self, data:Dict):
        new_block = Block(self.last_block.index + 1, time.time(), data, self.last_block.hash)
        mined_hash = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return mined_hash

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i-1]
            if cur.previous_hash != prev.hash:
                return False
            if cur.compute_hash() != cur.hash:
                return False
            if not cur.hash.startswith("0" * self.difficulty):
                return False
        return True

def demo():
    print("Creating blockchain with difficulty=3 (adjust difficulty for faster/slower mining)")
    bc = SimpleChain(difficulty=3)
    print("Genesis hash:", bc.last_block.hash)
    for i in range(1,4):
        data = {"tx": f"user{i} -> user{i+1}", "amount": i*10}
        print(f"\nMining block {i} with data {data} ...")
        h = bc.add_block(data)
        print("Mined hash:", h)
        print("Block nonce:", bc.last_block.nonce)
    print("\nChain valid?", bc.is_valid())
    # print chain
    for b in bc.chain:
        print(f"#{b.index} {b.hash} prev={b.previous_hash} nonce={b.nonce} data={b.data}")

if __name__ == "__main__":
    demo()

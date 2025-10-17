#!/usr/bin/env python3
"""
expr_compiler_vm.py
Small expression compiler: parse arithmetic expressions into bytecode, run in a stack VM.
Supports +, -, *, /, parentheses, integers.
Run: python3 expr_compiler_vm.py "2*(3+4)-5"
"""
import re
import sys

TOKEN_RE = re.compile(r'\s*(?:(\d+)|(.))')

def tokenize(expr):
    for num, other in TOKEN_RE.findall(expr):
        if num:
            yield ('NUM', int(num))
        else:
            yield (other, other)
    yield ('EOF', None)

# Recursive descent parser producing bytecode (postfix-like)
class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.tok, self.val = next(self.tokens)

    def eat(self, expected):
        if self.tok == expected:
            self.tok, self.val = next(self.tokens)
        else:
            raise SyntaxError(f"Expected {expected} got {self.tok}")

    def parse(self):
        code = self.expr()
        if self.tok != 'EOF':
            raise SyntaxError("Unexpected token after expression")
        return code

    def expr(self):
        code = self.term()
        while self.tok in ('+', '-'):
            op = self.tok
            self.eat(op)
            code += self.term()
            code.append(('OP', op))
        return code

    def term(self):
        code = self.factor()
        while self.tok in ('*', '/'):
            op = self.tok
            self.eat(op)
            code += self.factor()
            code.append(('OP', op))
        return code

    def factor(self):
        if self.tok == 'NUM':
            v = self.val
            self.eat('NUM')
            return [('PUSH', v)]
        elif self.tok == '(':
            self.eat('(')
            code = self.expr()
            self.eat(')')
            return code
        else:
            raise SyntaxError("Unexpected token in factor")

# Simple stack VM
def run_vm(code):
    stack = []
    for instr, arg in code:
        if instr == 'PUSH':
            stack.append(arg)
        elif instr == 'OP':
            b = stack.pop()
            a = stack.pop()
            if arg == '+': stack.append(a + b)
            elif arg == '-': stack.append(a - b)
            elif arg == '*': stack.append(a * b)
            elif arg == '/': stack.append(a / b)
            else: raise RuntimeError("Unknown op")
    return stack[-1] if stack else None

def compile_and_run(expr):
    tokens = tokenize(expr)
    p = Parser(tokens)
    code = p.parse()
    print("Bytecode:", code)
    result = run_vm(code)
    print("Result:", result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_and_run(" ".join(sys.argv[1:]))
    else:
        compile_and_run("2*(3+4)-5")

# muse
 my own language [WIP]

 name is subject to change

muse is designed to be a python-esque language but fast and safe

Planned features:
- Static typing with the option to declare types for improved performance
- Simple, unintrusive and readable syntax
- focus on a math-like declarative style, but with the option of also doing things the traditional, imerative way.
- focus on immutable code
- Hybrid paradigm, supports both functional and OOP
- Safe memory management, no GC is palnned (something similar to rust)
- runs on LLVM (maybe?)
- Supports both JIT compilation and interpreting (working on compilation first)
- concurrency (something similar to go)

# TODO:
    - Lexer (basic implementation is already done)
    - Parser [we are here]
    - Visitor
    - Integration with LLVM 

Syntax examples

```

# 2 ways to declare types

int a = 10
b = 20

string hello = "Hello World"

# example of a declarative single line function defenition with strong typing 

f(x: int, y: int) = (x^2) + y*(3-1) -> int

# example of an imerative function defenition

function(array)
    return [i^2 for i in array if i%2==0]

# function call

res = f(a, b)
```
# muse
 my own language [WIP]

 name is subject to change

muse is designed to be a python-esque language but fast and safe

### Planned features:
    - Static typing with the option to declare types for improved performance
    - Simple, unintrusive and readable syntax
    - focus on a math-like declarative style, but with the option of also doing things the traditional, imerative way.
    - focus on immutable code
    - Hybrid paradigm, supports both functional and OOP
    - Safe memory management, no GC is palnned (something similar to rust)
    - runs on LLVM (maybe?)
    - Supports both JIT compilation and interpreting (working on compilation first)
    - concurrency (something similar to go)

### TODO:
    - Lexer (basic implementation is already done)
    - Parser [we are here]
    - Visitor
    - Integration with LLVM 
    - optimization
    - memory management
    - standard library

### Syntax examples

```

# 2 ways to declare variables

a = 20

string hello = "Hello World"

# example of a declarative single line function defenition with strong typing 

f(x: int) = x^2 -> int

# example of an imerative function defenition

even(array)
    return [i for i in array if i%2==0]

# function call

res = f(a)
```

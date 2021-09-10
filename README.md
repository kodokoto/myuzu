# myuzu
 my own language [WIP]

*I am currently rewriting this in C as I found that using python with llvmlite codegen was too much of a hinderance, I will make that public when I have at working version up and running. Meanwhile I will leave my spaghetti python code up on github.

muse is designed to be a readable language that lets you write how you want to without compromising in speed and saftey*

### Planned features:
    - Optional typing, declare types if you want preformance, else don't bother
    - Simple, unintrusive and readable syntax
    - focus on a math-like declarative style, but with the option of also doing things the traditional, imerative way.
    - All variables are immutable by default
    - Hybrid paradigm, supports both functional and OOP
    - Safe memory management done before run-time, no GC is palnned (will probably implement something like rusts borrow checker)
    - runs on LLVM (maybe?)
    - Supports both JIT compilation and interpreting (working on compilation first)
    - concurrency (something similar to rust again, but with a syntax that is closer to go)

### TODO:
    - Lexer (basic implementation is already done)
    - Parser [we are here]
    - implement span for better compiler erros
    - Visitor
    - Semmantic analysis
      - Borrow checking
      - type checking
      - lifetime checking
    - Integration with LLVM 
    - optimization
    - memory management
    - standard library

### Syntax examples


Each example will have a version with dynamic typing, and one without



declaring variables:
```

x = 10
y float = 2.0     // this can also be written as: float y = 0

```
function defenitions:
```

// declarative:

f(x, y) = x + y

f(x int, y float) float = x + y    // argument names and types are interchangable


// imperative:

f(x, y)                       // code blocks are handled entirely through indentation
    return x + y

f(x int, y int) int         // I might make it possible to add an optional "def" keyword if it makes it faster   
    return x + y

```
if elif else statement:
```

if x > y
    largest = x

elif x < y
    largest = y

else largest = none

// ternary operator:

even(x int) bool = true if x >= 0 else false

```
for loop:
```

for i in iterable
    print(i)

// list comprehension:

cube(array) = [x^3 for x in array]

```
while loop:
```

while x < 20
    x += 1
    
```

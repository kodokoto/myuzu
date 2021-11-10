# myuzu
 my own language [WIP]

 name is subject to change

myuzu is designed to be a readable language that lets you write how you want to without compromising in speed and saftey

### Planned features:
    - Optional typing through the use of type inference and multiple dispatch before runtime
    - Simple, unintrusive and readable syntax
    - focus on a math-like declarative style, but with the option of also doing things the traditional, imerative way.
    - All variables are immutable by default
    - Only one "owner" of a value at a time
    - Hybrid paradigm, supports both functional and OOP
    - Safe memory management done before run-time, no GC (will probably implement something like rusts borrow checker)
    - uses LLVM and MLIR
    - Supports both JIT compilation and interpreting (working on compilation first)
    - concurrency (something similar to rust again, but with a syntax that is closer to go)

### TODO:
    - Lexer [re-writing in C++]
    - Parser [re-writing in C++]
    - Semmantic analysis
      - Borrow checking 
      - type checking [WIP in python]
      - lifetime checking
    - Integration with LLVM [WIP in python]
    - optimization
    - memory management
    - standard library

### Syntax examples


Each example will have a version with dynamic typing, and one without

declaring variables:
```

x = "Foo"
y float = 2.0

// there can only be one owner of a place in memory at any moment (like rust)

a = x           // this clones "Fitz", a is now equal to "Fitz"
x := "Bar"      // := is the reassignment operator, in this situation the variable x drops ownership of "Foo" and becomes the owner of "Bar"

```

function defenitions:
```

// declarative:

f(x, y) = x + y

f(x int, y float) float = x + y   


// imperative:

f(x, y)                       // code blocks are handled entirely through indentation
    return x + y

f(x int, y int) int         
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

# char = '_awd awd==wad'
# counter = 8
# double_operators = {
#     "==" : "EQUAL_EQUAL",
#     "!=" : "BANG_EQUAL",
#     "<=" : "LESS_EQUAL",
#     ">=" : "MORE_EQUAL",
#     "+=" : "INCREMENT",
#     "-=" : "DECREMENT",
#     "->" : "TYPE_INFER"
# }

# # print(char[counter:counter+2])
# example = "function(x : int, y : int) = (x^2.0) + y*(3-1) -> int"
# print(len(example[53]))

class P:
    def __init__(self):
        self.a = self.A()
        self.b = self.B()

    class A:
        def __init__(self):
            self.test = ""

    class B:
        def __init__(self):
            self.test = ""


p = P()

testA = p.a
testB = p.b

testA.test = "Hello"

testB.test = "World"

print(testA.test)

print


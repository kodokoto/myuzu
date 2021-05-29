from lexer import Lexer
class AST:
    def __init_(self):
        self.types = [] 
        
    # def init_Node(self):
        
    class function_def:
        def __init__(self):
            self.name = ""
            self.arguments = []
            self.argument_types = []
            self.body = ""
            self.return_type = ""

    # class 


    

# function defenition (lambda)
# | name(arguments) = expression 
# 
# strongly typed function defenition (lambda)
# | name(arguments : type) = body -> type 
#
# function call
# | name(arguments)
# 
# variable defenition
# | name = expression
# 
# expression
# 
# 
# 
# 
# 
# 
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokenize()
        self.current_token = self.tokens[0]
        self.previous_token = self.current_token

    def parser_eat(self, token_type):
        if self.current_token.type == token_type:
            print()




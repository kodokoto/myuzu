from lexer import Lexer

        
class DefenitionAST:
    def __init__(self, name, arguments, argument_types=None, return_type=None):
        self.name = name
        self.arguments = arguments
        self.argument_types = argument_types
        self.return_type = return_type


class FunctionAST:
    def __init__(self, defenition, body):
        self.defenition = defenition 
        self.body = body
    # clas

# class CallAST:



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
        self.tokens = lexer.init_lex()
        self.index = 0
        self.current_token = self.tokens[index]

    def parse(self):
        if current_token.type == "TOKEN_ID" and self.tokens[self.index+1].type == "LPAREN":
            if self.func_lookahead(self.index):
                return self.func_def()
            else: return self.func_call()
               
    def check_token(self, expected_type, expected_value=None):
        if self.current_token.type != token_type:
            raise ParseError(f"Expected token type: {expected_type}, got: {self.current_token.type}")
        self.next_token()

    def next_token(self):
        self.index += 1
        self.current_token = self.tokens[index]

    def func_def(self):
        name = self.check_token.value
        self.check_token("TOKEN_ID")
        self.check_token("LPAREN")
        arguments = []
        argument_types = []
        while self.current_token.type != "RPAREN":
            if self.current_token.type == "TOKEN_ID" and self.tokens[self.index+1] == "COLON":
                arguments.append(self.current_token.type)


    def parse_args():
        arguments = []
        argument_types = []


    def func_call(self):

    def func_lookahead(self, index):
        while self.tokens[index] != "RPAREN":
            index+=1
        if self.tokens[index+1] = "EQUAL":
            return True
        else: return False




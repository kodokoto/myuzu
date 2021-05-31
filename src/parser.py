from lexer import Lexer, 

        
class FunctionDeclerationAST:
    def __init__(self, name, arguments, argument_types, return_type=None):
        self.name = name
        self.arguments = arguments
        self.argument_types = argument_types
        self.return_type = return_type

class FunctionDefenitionAST:
    def __init__(self, decleration, body):
        self.decleration = decleration 
        self.body = body
    # clas

class FunctionCallAST:

class NUmberAST:
    def __init__(self, value, val_type=None):
        self.value = value
        self.val_type = val_type

class VariableAST:
    def __init__(self, name, val_type=None):
        self.name = name
        self.val_type = val_type

class BinaryExpressionAST:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self. lhs = lhs
        self.rhs = rhs

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
        self.type_tokens = ["INT_DECL", "STR_DECL", "BOOL_DECL", "FLOAT_DECL"]
        self.op_tokens = {
    ':' : "COLON",
    ',' : "COMMA",
    '.' : "PERIOD",
    '=' : "EQUALS",
    '+' : "PLUS",
    '-' : "MINUS",
    '*' : "MULT",
    '/' : "DIV",
    '^' : "EXPO",
    '%' : "MODULO",
    '(' : "RPAREN",
    ')' : "LPAREN",
    '[' : "RSQUARE",
    ']' : "LSQUARE",
    '{' : "RCURLY",
    '}' : "LCURLY",
    '<' : "LESS_THAN",
    '>' : "MORE_THAN",
    "==" : "EQUAL_EQUAL",
    "!=" : "BANG_EQUAL",
    "<=" : "LESS_EQUAL",
    ">=" : "MORE_EQUAL",
    "+=" : "INCREMENT",
    "-=" : "DECREMENT",
}
    }

    def parse(self):
        if current_token.type == "TOKEN_ID" and self.tokens[self.index+1].type == "LPAREN":
            if self.check_if_func_decl(self.index):
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
        decleration = self.func_decl()
        body = self._parse_expression()
        return FunctionDefenitionAST(decleration, body)

    def func_decl(self):
        # store name, arguments, argument_types and an optional return type
        name = self.check_token.value
        self.check_token("TOKEN_ID")
        self.check_token("LPAREN")
        arguments = []
        argument_types = []
        return_type = None
        # While we are inbetween the brackets
        while self.current_token.type != "RPAREN":
            # If we have TOKEN_ID followed by COLON then we know there is a type decleration
            if self.current_token.type == "TOKEN_ID" and self.tokens[self.index+1] in self.type_tokens:
                arguments.append(self.current_token.type)
                # if that the token following the COLON is a valis type decleration, store the type, else return an error
                argument_types.append(self.tokens[self.index+1].value) if self.tokens[self.index+2].type in self.type_tokens else raise ParseError(f"Expected Type Decleration token, instead got: {self.tokens[self.index+2].type}")
                self.next_token()
                self.next_token()
                self.check_token("COMMA") # make sure there is a comma separating the arguments
            # if there is no COLON token after the TOKEN_ID, there is no type decleration
            elif self.current_token in self.type_tokens and self.tokens[self.index+1].type == "TOKEN_ID":
                arguments.append(self.current_token.type)
                # if that the token following the COLON is a valis type decleration, store the type, else return an error
                argument_types.append(self.tokens[self.index+1].value) if self.tokens[self.index+2].type in self.type_tokens else raise ParseError(f"Expected Type Decleration token, instead got: {self.tokens[self.index+2].type}")
                self.next_token()
                self.next_token()
                self.check_token("COMMA") # make sure there is a comma separating the arguments
    
            elif self.current_token.type == "TOKEN_ID":
                arguments.append(self.current_token.type)
                argument_types.append(None)
                self.next_token()
                self.check_token("COMMA")
            #If there is no TOKEN_ID, then the token is invalid 
            else: raise ParseError(f"Unexpected token: {self.current_token.type}")
        self.check_token("RPAREN")

        # If there is a -> return type decleration, store it

        if self.current_token.type in self.type_tokens:
            return_type = self.current_token.value
            self.next_token()
            return FunctionDeclerationAST(name, arguments, argument_types, return_type)
        else: return FunctionDeclerationAST(name, arguments, argument_types)

    def func_call(self):
        name = self.check_token.value
        self.check_token("TOKEN_ID")
        self.check_token("LPAREN")
        arguments = []
        # Store all the arguments in the brackets
        while self.current_token.type != "RPAREN":
            if self.current_token.type == "TOKEN_ID":
                arguments.append(self.current_token.type)
                self.next_token()
                self.check_token("COMMA")
            else: raise ParseError(f"Unexpected token: {self.current_token.type}")
        self.check_token("RPAREN")
        return FunctionCallAST(name, arguments)
           

    def check_if_func_decl(self, index):
        # make sure that this is the beggining of a line
        if self.tokens[index-1].type == "EOL" or self.tokens[index-1].type == "INDENT":
            # if there is an EQUALS token after RPAREN it must be a declarative function decleration
            while self.tokens[index].type != "RPAREN":
                index+=1
            if self.tokens[index+1].type == "EQUAL":
                return True
            # if there is a codeblock in the next line then it is an imperative function decleration
            # because we made sure that the call is at the beggining of a line we know that it cannot be
            # if fuction(x)
            #   //code
            while self.tokens[index].type != "EOL":
                index+=1
            if self.tokens[index+1].type == "INDENT":
                return True
            else return False
        else: return False

    def primary(self):

    def expression(self):
        lhs = self.primary()
        return self.binop_rhs(0, lhs)



from lexer import Lexer

class Span():
    def __init__(self, start, end=None):
        self.start = start
        self.end = end
    def __repr__(self) -> str:
        if self.end != None:
            return f"from: {self.start.line}, {self.start.column} to: {self.end.line}, {self.end.column}"
        else: return f"from: {self.start.line}, {self.start.column}"
        
class NumberLiteral:
    def __init__(self, value):
        self.value = value

class StringLiteral:
    def __init__(self, value):
        self.value = value

class Identifier:
    def __init__(self, name, span):
        self.name = name
        self.span = span

class TypedIdentifier:
    def __init__(self, _id, _type, span):
        self.id = _id
        self.type = _type
        self.span = span

class AssignmentExpression:
    def __init__(self, name, expression, var_type=None):
        self.name = name
        self.var_type = var_type
        self.expression = expression

class BlockNode:
    def __init__(self, statements, span):
        self.statements = statements
        self.span = span

class StatementNode:
    def __init__(self, expression, span):
        self.expression = expression
        self.span = span

class FunctionSignature:
    def __init__(self, name, arguments, span, return_type=None):
        self.name = name
        self.arguments = arguments
        self.return_type = return_type
        self.span = span

class FunctionArgument:
    def __init__(self, span, identifier, _type=None):
        self.identifier = identifier
        self.type = _type
        self.span = span

class FunctionAST:
    def __init__(self, signature, body, span):
        self.signature = signature 
        self.body = body
        self.span = span

class CallExpressionAST:
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments



class BinaryExpressionAST:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.init_lex()
        self.index = 0
        self.current_token = self.tokens[self.index]
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

    def parse(self):
        if self.current_token.type == "TOKEN_ID" and self.tokens[self.index+1].type == "LPAREN":
            if self.check_if_func_signature(self.index):
                return self.func_def()
            else: return self.func_call()
        elif self.check_if_var_def():
            self.var_decl()
               
    def eat_token(self, expected_type):
        if self.current_token.type != expected_type:
            raise ParseError(f"Expected token type: {expected_type}, got: {self.current_token.type}, at line: {self.current_token.line}, column: {self.current_token.column}")
        self.next_token()

    def next_token(self, repetitions=1):
        for i in range(repetitions):
            self.index += 1
            self.current_token = self.tokens[self.index]

    def func_def(self):
        span_start = self.current_token.pointer
        decleration = self.func_signature()
        if self.current_token.type == "EQUALS":
            self.next_token()
            body = self._parse_expression()
        elif self.current_token.type == "EOL" and self.tokens[self.index+1].type == "INDENT":
            self.next_token(2)
            body = self._parse_block()
        else: raise ParseError(f"Expected indent or '=', instead of {self.current_token.value} ")
        return FunctionAST(decleration, body, Span(span_start, self.current_token.pointer))

    def func_signature(self):
        # store name, arguments, argument_types and the start of the signature
        span_start = self.current_token.pointer
        name = self.eat_token.value
        self.eat_token("TOKEN_ID")
        self.eat_token("LPAREN")
        arguments = []
        # While we are inbetween the brackets, append all arguments
        while self.current_token.type != "RPAREN":
            arguments.append(self.parse_id())
            self.eat_token("COMMA")
        self.eat_token("RPAREN")

        # If there is a return type decleration, store it

        if self.current_token.type in self.type_tokens:
            res = FunctionSignature(name, arguments, Span(span_start, self.current_token.span), self.current_token.value)
            self.next_token()
            return res
        else: return FunctionSignature(name, arguments, Span(span_start, self.current_token.span))

    def func_call(self):

        name = self.eat_token.value
        self.eat_token("TOKEN_ID")
        self.eat_token("LPAREN")
        arguments = []
        # Store all the arguments in the brackets
        while self.current_token.type != "RPAREN":
            if self.current_token.type == "TOKEN_ID":
                arguments.append(self.current_token.type)
                self.next_token()
                self.eat_token("COMMA")
            else: raise ParseError(f"Unexpected token: {self.current_token.type}")
        self.eat_token("RPAREN")
        return CallExpressionAST(name, arguments)
           
    def val_decl(self):
        if self.current_token.type in self.type_tokens:
            var_type = self.current_token.value
            self.next_token()
            name = self.current_token.value
            self.next_token()
        else:
            name = self.current_token.value
            self.next_token()
            if self.current_token.type in self.type_tokens:
                var_type = self.current_token.value
                self.next_token()
        self.next_token()
        expression = expression()

        return AssignmentExpressionNode(name, expression, var_type)

    def check_if_func_signature(self, index):
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

    def check_if_var_def(self, index):
        # int x = 0
        if self.tokens[index].type == "TOKEN_ID" and self.tokens[index+1].type in self.type_tokens and self.tokens[index+2].type == "EQUALS":
            return True
        # x int = 0    
        elif self.tokens[index].type in self.type_tokens and self.tokens[index+1].type == "TOKEN_ID" and self.tokens[index+2].type == "EQUALS":
            return True
        # x = 0
        elif self.tokens[index].type == "TOKEN_ID" and self.tokens[index+1].type == "EQUALS":
            return True
        else: return False



    def expression(self):
        lhs = self.primary()
        return self.binop_rhs(0, lhs)


    def parse_id(self):
        """
        Checks for any of the possible combinations
        x
        int x
        x int
        and returns the appropriate node
        """
        span_start = self.current_token.span
        if self.lookahead(["TOKEN_ID", self.type_tokens]):

            tmp = TypedIdentifier(self.current_token.span, Identifier(self.current_token.value, Span(span_start, self.tokens[self.index+1].span)), self.tokens[self.index+1].value)
            self.next_token(2)
            return tmp
        elif self.current_token.type == "TOKEN": 
            tmp = Identifier(self.current_token.value, Span(span_start))
            self.next_token()
            return tmp
        elif self.lookahead([self.type_tokens, "TOKEN_ID"]):
            tmp = TypedIdentifier(Span(span_start, self.tokens[self.index+1].span), self.tokens[self.index+1].value, self.current_token.value)
            self.next_token(2)
            return tmp
        else: raise ParseError(f"Expected a type decleration, instead received {self.current_token.type} at {self.current.token.span}") 

    def parse_statement(self):
        span_start = self.current_token.pointer
        if self.lookahead(["TOKEN_ID", "LPAREN"]):
            if self.check_if_func_signature(self.index):
                return self.func_def()
            else: return self.func_call()

        elif self.lookahead(["TOKEN_ID", self.type_tokens, "EQUALS"]) or self.lookahead([self.type_tokens, "TOKEN_ID", "EQUALS"]):
            return self.var_decl()
        
        else: return self.expression_statement()


        return StatementNode(expression, Span(span_start, self.current_token.pointer))

    def parse_block(self):
        span_start = self.current_token.pointer
        statements = []
        self.eat_token("INDENT")
        parse_statements("DEDENT")
        self.eat_token("DEDENT")
        return BlockNode(statements, Span(span_start, self.current_token.pointer))

    def parse_statements(self, end_token):
        span_start = self.current_token.pointer
        statements = []
        while self.current_token != None and self.current_token.type != end_token:
            statements.append(parse_statement())

    def expression_statement(self):
        expression = self.expression()
        self.eat_token("EOL")
        return ExpressionStatement()

    def binary_expression():
        left = self.current_token.

    def lookahead(self, tokens):
        return all(True if self.tokens[self.index+token_num] in token else False for token, token_num in enumerate(tokens))
    
# <statement> := <expression> 
#               | <if_else_statement> 
#               | <for_loop> 
#               | <while_loop>
#               | <function_declaration>

# <simple_stmt> := <expression>
#               | <assignment>
#               | <ternary_op>
#               | <list_comp>
#               | <return_statement> 


# <compound_stmt>

# <expression> := <term> <operator> <expression>
#               | <term>


# <term> := <literal> 
#           | <identifier> 
#           | <paren_exp> 
#           | <function_call>

# <literal> := <number> 
#           | <string> 
#           | <bool> 

# <assignment> := <type_token> <identifier> "=" (<expression> | <simple_stmt>)
from lexer import Lexer, Token
import json
from json import JSONEncoder

class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class ParseError(Exception): pass

class Span:
    def __init__(self, start, end=None):
        self.start = start
        self.end = end
    def __repr__(self) -> str:
        if self.end != None:
            return f"from: {self.start.line}, {self.start.column} to: {self.end.line}, {self.end.column}"
        else: return f"from: {self.start.line}, {self.start.column}"


class Program:
    def __init__(self, block):
        self.block = block

class NumericLiteral:
    def __init__(self, span, value):
        self.value = value
        self.span = span

class StringLiteral:
    def __init__(self, span, value):
        self.value = value
        self.span = span


class Identifier:
    def __init__(self, span, id_name):
        self.id = id_name
        self.span = span

class Parameter:
    def __init__(self, span, id_name, id_type=None):
        self.id = id_name
        self.type = id_type
        self.span = span
    def __str__(self):
        json.dumps({self.__class__.__name__ :{"identifier": self.id, "type": self.type}})

class BinaryExpression:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        # self.span = span

# <function_declaration> := <funtcion_protopype> <body>
class FunctionDefenition:
    def __init__(self, span, proto, body):
        self.prototype = proto
        self.body = body
        self.span = span

# <function_prototype> := <identifier> "(" <signature>+ ")" "->" <return_type>
class FunctionPrototype:
    def __init__(self, span, name, parameters, return_type=None):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.span = span
    def __str__(self):
        json.dumps({self.__class__.__name__: {"name": self.name, "proto": self.parameters, "return type": self.return_type}})

class FunctionCall:
    def __init__(self, span, name, arguments=None):
        self.name = name
        self.arguments = arguments
        self.span = span

class StatementBlock:
    def __init__(self, span, statements):
        self.statements = statements 
        self.span = span

class Statement:
    def __init__(self, span, statement):
        # can be expression, function call, if statement
        self.statement = statement
        self.span = span

class ReturnStatement:
    def __init__(self, span, expression):
        self.expression = expression
        self.span = span
class AssignmentStatement:
    def __init__(self, span, name, expression, variable_type=None):
        self.name = name
        self.expression = expression
        self.variable_type = variable_type
        self.span = span

class IfStatement:
    def __init__(self, span, conditional, block, _else=None):
        self.conditional = conditional
        self.block = block
        self._else = _else 

class ForLoop:
    def __init__(self, span, body, iterable, identifiers):
        self.body = body
        self.iterable = iterable
        self.identifiers = identifiers # list of identifiers
        self.span = span

class ListComprehention:
    def __init__(self, span, expression, iterable, identifiers, filterExpression=None):
        self.expression = expression
        self.iterable = iterable
        self.identifiers = identifiers
        self.filter = filterExpression
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.init_lex()
        self.tokens.append(Token("EOF", ""))
        print(self.tokens)
        self.index = 0
        self.current_token = self.tokens[self.index]
        self.presedence_map = {
                            "EXPO" : 80,
                            "MULT" : 40,
                            "DIV"  : 40,
                            "PLUS" : 20,
                            "MINUS" : 20,

        }
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
                            '%' : "MODULO"
                            }
        self.brace_tokens = {
                            '(' : "LPAREN",
                            ')' : "RPAREN",
                            '[' : "RSQUARE",
                            ']' : "LSQUARE",
                            '{' : "RCURLY",
                            '}' : "LCURLY"
                            }
        self.logic_op_tokens = {
                            '<' : "LESS_THAN",
                            '>' : "MORE_THAN",
                            "==" : "EQUAL_EQUAL",
                            "!=" : "BANG_EQUAL",
                            "<=" : "LESS_EQUAL",
                            ">=" : "MORE_EQUAL",
                            "+=" : "INCREMENT",
                            "-=" : "DECREMENT",
                        }


# Utility

    def lookahead(self, tokens):
        return all(True if self.tokens[self.index+token_num].type in token else False for token_num, token in enumerate(tokens))

    # checks then consumes
    def eat_token(self, expected_type):
        if self.current_token.type != expected_type:
            raise ParseError(f"Expected token type: {expected_type}, got: {self.current_token.type}, at: {self.current_token.pointer}")
        self.next_token()

    # blindly consumes
    def next_token(self, repetitions=1):
        for i in range(repetitions):
            if self.current_token != "EOF":
                self.index += 1
                self.current_token = self.tokens[self.index]

    def check_if_function_prototype(self, index):
        print("Check if function", self.current_token.value )

        # make sure that this is the beggining of a line
        try:
            last_token = self.tokens[index-1].type
        except IndexError: last_token = None
        print(last_token)
        if last_token == "EOL" or last_token == "DEDENT" or last_token == None:
            print(1)
            # if there is an EQUALS token after RPAREN it must be a declarative function decleration
            while True:
                if self.tokens[index].type == "RPAREN":
                    break
                index+=1
            if (self.tokens[index+1].type == "EQUALS" or
                self.tokens[index+1].type in self.type_tokens):
                print("fouund function")
                return True
            # if there is a codeblock in the next line then it is an imperative function decleration
            # because we made sure that the call is at the beggining of a line we know that it cannot be
            # if fuction(x)
            #   //code
            while self.tokens[index].type != "EOL":
                index+=1
            if self.tokens[index+1].type == "INDENT":
                return True
            else: return False
        else: return False

# Statements

    def parse_program(self):
        return Program(self.parse_statements())
    
    def parse_block(self):
        span_start = self.current_token.pointer
        self.eat_token("INDENT")
        statements = self.parse_statements("DEDENT")
        self.eat_token("DEDENT")
        return StatementBlock(Span(span_start, self.current_token.pointer), statements)

    def parse_statements(self, end_token=None):
        span_start = self.current_token.pointer
        statements = []
        while self.current_token.type != "EOF" and self.current_token.type != end_token:
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        if self.current_token.type=="TOKEN_ID" and self.check_if_function_prototype(self.index):
            return self.parse_function_defenition()
        elif self.lookahead([["TOKEN_ID"], self.type_tokens, ["EQUALS"]]) or self.lookahead([["TOKEN_ID"], ["EQUALS"]]):
            return self.parse_assignment_statement()
        elif self.current_token.type=="RETURN":
            return self.parse_return_statement()
        else: self.parse_expression()

    def parse_assignment_statement(self):
        span_start = self.current_token.pointer

        name = self.current_token.value
        self.next_token()
        if self.current_token.type == "EQUALS":
            self.next_token()
            expression = self.parse_expression()
            assignment = AssignmentStatement(Span(span_start, self.current_token.pointer), name, expression)
            self.eat_token("EOL")
            return  assignment
        else:
            variable_type = self.current_token.type
            self.next_token(2)
            expression = self.parse_expression()
            assignment = AssignmentStatement(Span(span_start, self.current_token.pointer), name, expression, variable_type)
            self.eat_token("EOL")
            return assignment

    def parse_return_statement(self):
        span_start = self.current_token.pointer
        self.next_token()
        expression = self.parse_expression()
        return_statement = ReturnStatement(Span(span_start, self.current_token.pointer), expression)
        self.eat_token("EOL")
        return return_statement

#   Function Defenition

    def parse_function_defenition(self):
        span_start = self.current_token.pointer
        prototype = self.parse_function_prototype()
        if self.current_token.type == "EQUALS":
            self.next_token()
            body = self.parse_expression()
            self.next_token()
        elif self.current_token.type == "EOL" and self.tokens[self.index+1].type == "INDENT":
            self.next_token()
            body = self.parse_block()
        else: raise ParseError(f"Expected indent or '=', instead of {self.current_token.value} at: {self.current_token.pointer}")
        return FunctionDefenition(Span(span_start, self.current_token.pointer), prototype, body)

    def parse_function_prototype(self):
        # store name, arguments, argument_types and the start of the signature
        span_start = self.current_token.pointer
        name = self.current_token.value
        self.eat_token("TOKEN_ID")
        self.eat_token("LPAREN")

        # While we are inbetween the brackets, append all arguments
        arguments = []
        while self.current_token.type != "RPAREN":
            arguments.append(self.parse_parameter())
            if self.current_token.type!="RPAREN":
                self.eat_token("COMMA") 
        self.eat_token("RPAREN")

        # If there is a return type decleration, store it

        if self.current_token.type in self.type_tokens:
            res = FunctionPrototype(name, arguments, Span(span_start, self.current_token.pointer), self.current_token.value)
            self.next_token()
            return res
        else: return FunctionPrototype(name, arguments, Span(span_start, self.current_token.pointer))

    def parse_parameter(self):
        span_start = self.current_token.pointer
        if self.lookahead([["TOKEN_ID"], self.type_tokens]):
            id_name = Identifier(self.current_token.pointer, self.current_token.value)
            self.next_token()
            id_type = self.current_token.type
            end_span = self.current_token.pointer
            self.next_token()
            return Parameter(Span(span_start, end_span), id_name, id_type)
        else:
            id_name = self.current_token.value
            self.eat_token("TOKEN_ID")
            return Parameter(Span(span_start), id_name)

# Expressions

    # expression :=
    def parse_expression(self):
        lhs = self.parse_unary()
        return self.parse_binexp_rhs(0, lhs)

    def parse_unary(self):
        # if self.current_token.type in self.unary_op:
        return self.parse_primary()

    def parse_primary(self):
        if self.current_token.type == "TOKEN_ID":
            return self.parse_identifier_expression()
        elif self.current_token.type == "NUMBER":
            number = NumericLiteral(Span(self.current_token.pointer), self.current_token.value)
            self.next_token()
            return number
        elif self.current_token.type == "LPAREN":
            return self.parse_parenthesis()
        else:
            raise ParseError(f"Expected a literal or an expression not {self.current_token.type} at: {self.current_token.pointer}")
    
    def parse_identifier_expression(self):
        if self.lookahead([["TOKEN_ID"], ["LPAREN"]]):
            return self.parse_function_call()
        else:
            span = Span(self.current_token.pointer)
            id_name = self.current_token.value
            self.next_token()
            return Identifier(span, id_name)

    def parse_parenthesis(self):
        self.next_token()
        expression = self.parse_expression()
        self.eat_token("RPAREN")
        return expression

    def parse_function_call(self):
        span_stat = self.current_token.pointer

        name = self.current_token.value
        self.next_token(2)
        arguments = []
        while self.current_token.type != "RPAREN":
            arguments.append(self.parse_expression())
            if self.current_token.type!="RPAREN":
                self.eat_token("COMMA")
        span_end = self.current_token.pointer 
        self.eat_token("RPAREN")
        return FunctionCall(span, name, arguments) if len(arguments) else FunctionCall(span, name)

    def check_precedence(self):
        """Get the operator precedence of the current token."""
        try:
            return self.presedence_map[self.current_token.type]
        except KeyError:
            return -1

    def parse_binexp_rhs(self, precedence, lhs):
        # print("binop")
        while True:
            current_precedence = self.check_precedence()
            # print("current prec" ,current_precedence)
            # handles non operators
            if current_precedence < precedence:
                # print("exit")
                return lhs
            op = self.current_token.value
            # print("op", op)
            self.next_token()
            rhs = self.parse_unary()
            # print("lhs", lhs.id)
            # print("rhs", rhs.id)
            next_precedence = self.check_precedence()
            # print("next precedence", next_precedence)
            if current_precedence < next_precedence:
                rhs = self.parse_binexp_rhs(current_precedence + 1, rhs)

            lhs = BinaryExpression(op, lhs, rhs)
    
    

    

# testBinExp = BinaryExpression('+', 'x', 'y')
# param1 = Parameter(1, "x", "int")
# param2 = Parameter(1, "y", "int")
# testFuncProto = FunctionPrototype(1, "add", [param1, param2], "int")
# testFuncDef = FunctionDefenition(1, testFuncProto, testBinExp)

# print(json.dumps(testFuncDef, indent=4, cls=EmployeeEncoder))


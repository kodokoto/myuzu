example = 'function(name : string multiplier : x) = true if string == "Hello" else false -> bool'


single_operators = {
    ':' : "COLON",
    ',' : "COMMA",
    '.' : "PERIOD",
    '=' : "EQUALS",
    '+' : "PLUS",
    '-' : "MINUS",
    '*' : "MULT",
    '/' : "DIV",
    '^' : "EXPO",
    '(' : "RPAREN",
    ')' : "LPAREN",
    '[' : "RSQUARE",
    ']' : "LSQUARE",
    '{' : "RCURLY",
    '}' : "LCURLY",
    '<' : "LESS_THAN",
    '>' : "MORE_THAN",
    }

double_operators = {
    "==" : "EQUAL_EQUAL",
    "!=" : "BANG_EQUAL",
    "<=" : "LESS_EQUAL",
    ">=" : "MORE_EQUAL",
    "+=" : "INCREMENT",
    "-=" : "DECREMENT",
    "->" : "TYPE_INFER"
}

keywords = {
    "if"     : "IF",
    "elif"   : "ELSE_IF",
    "else"   : "ELSE",
    "for"    : "FOR",
    "in"     : "IN",
    "while"  : "WHILE",
    "true"   : "TRUE",
    "false"  : "FALSE",
    "null"   : "NULL",
    "or"     : "OR",
    "and"    : "AND",
    "return" : "RETURN",
    "class"  : "CLASS",
    "int"    : "INT_DECL",
    "string" : "STR_DECL",
    "bool"   : "BOOL_DECL"
} 

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        return f"\n{self.type} : {self.value}"

class Lexer:
    def __init__(self, line):
        self.line = line
        self.cursor = 0
        self.charachter = self.line[self.cursor]


    def advance(self):
        if self.cursor < len(self.line)-1:
            self.cursor+=1
            self.charachter = self.line[self.cursor]
        else: self.cursor+=1

    # def checkIndent(self):

    def collect_id(self):
        value = ""
        while self.cursor < len(self.line) and self.charachter.isalpha():
            value+=self.charachter
            self.advance()
        if value in keywords:
            return Token(keywords[value], value)
        return Token("TOKEN_ID", value)   

    def collect_number(self):
        value = ""
        while self.cursor <= len(self.line) and (self.charachter.isnumeric() or self.charachter == '.'):
            value+=self.charachter
            self.advance()
        if value[-1] == '.': a = a[:-1]
        value = float(value) if ('.' in value) else int(value)
        return Token("NUMBER", value)

    def collect_string(self):
        value = ''
        while self.cursor < len(self.line):
            
            self.advance()
            if self.charachter != '"':
                value += self.charachter
            else:
                self.advance()
                break
        return Token("STRING", value)

    def tokenize(self):
        self.tokens = []
        while self.cursor < len(self.line):
            # Token IDs & Keywords
            if self.charachter.isalpha():
                self.tokens.append(self.collect_id())
            # Numbers
            elif self.charachter.isnumeric():
                self.tokens.append(self.collect_number())
            # Double Operators
            elif self.charachter == '"':
                self.tokens.append(self.collect_string())

            elif self.line[self.cursor:self.cursor+2] in double_operators:
                self.tokens.append(Token(double_operators[self.line[self.cursor:self.cursor+2]], self.line[self.cursor:self.cursor+2]))
                self.advance()
                self.advance()
            # Single Operators
            elif self.charachter in single_operators:
                self.tokens.append(Token(single_operators[self.charachter], self.charachter))
                self.advance()
            else: self.advance()
        return self.tokens
            

            
lexer = Lexer(example)

print(lexer.tokenize())




            



    



    







    
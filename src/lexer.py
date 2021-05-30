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
    '%' : "MODULO",
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
    "->" : "RETURN_TYPE"
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
    "bool"   : "BOOL_DECL",
    "float"  : "FLOAT_DECL"
} 

class Token:
    def __init__(self, type_, value, val_type=None):
        self.type = type_
        self.value = value
        self.val_type =val_type

    def __repr__(self) -> str:
        return f"\n{self.type}"

class Lexer:
    def __init__(self, content):
        self.content = content
        

    def init_lex(self):
        self.lines = self.content.split("\n")

        self.separate_lines = [line for line in self.lines if line != ""]
        self.all_tokens = []
        # self.line_count = 0
        tmp_lvl = 0
        # while self.line_count < len(self.separate_lines)-1:
        for i in self.separate_lines:
            tmp_tok, tmp_lvl  = self.tokenize(i, tmp_lvl)
            self.all_tokens.append(tmp_tok)
        return [item for sublist in self.all_tokens for item in sublist if item.type!="COMMENT"]
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

    def tokenize(self, line, level):
        self.line = line.replace('    ', '\t')
        self.cursor = 0
        self.charachter = self.line[self.cursor]
        self.level = level
        self.tokens = []
        while self.cursor < len(self.line):
            # Token IDs & Keywords
            if self.charachter == '#':
                return [Token("COMMENT", "useless")], level
            elif level<self.line.count('\t'):
                self.tokens.append(Token("INDENT", '\t'))
                level += 1
                self.advance()
            elif level>self.line.count('\t'):
                self.tokens.append(Token("DEDENT", '\t'))
                level-=1
                self.advance()
            elif self.charachter.isalpha():
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
        self.tokens.append(Token("EOL", ""))
        return self.tokens, level
    



            


    



    







    

# Dictionary containing all single operators
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
    '(' : "LPAREN",
    ')' : "RPAREN",
    '[' : "RSQUARE",
    ']' : "LSQUARE",
    '{' : "RCURLY",
    '}' : "LCURLY",
    '<' : "LESS_THAN",
    '>' : "MORE_THAN",
    }

# Dictionary containing all double operators
double_operators = {
    "==" : "EQUAL_EQUAL",
    "!=" : "BANG_EQUAL",
    "<=" : "LESS_EQUAL",
    ">=" : "MORE_EQUAL",
    "+=" : "INCREMENT",
    "-=" : "DECREMENT",
    "->" : "RETURN_TYPE"
}

# Dictionary containing all keywords
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

# Token Object holds the Token type (i.e MODULO), value (i.e %) and pointer (LineColumn object)
class Token:
    def __init__(self, type_, value, pointer=None):
        self.type = type_
        self.value = value
        self.pointer = pointer

    def __repr__(self):
        return f"\n{self.type}"

# LineColumn object holds the line where the token is held, and column of that line.
class LineColumn:
    def __init__(self, line, column):
        self.line = line
        self.column = column
    def __str__(self):
        return f"line: {self.line} column: {self.column}"

# Lexer object holds content, the current line number and the current column
class Lexer:
    def __init__(self, content):
        self.content = content
        self.lineno = 0
        self.column = 1
        
    def init_lex(self):
        """
        init_lex starts the lexing process by splitting the content into lines, then tokenizing each line
        """
        self.lines = self.content.split("\n")
        # filter out all empty lines
        self.separate_lines = [line for line in self.lines if line != ""]
        # token list
        self.all_tokens = []
        # initialize token level, the level dictates how nested the block of lines is
        tmp_lvl = 0
        for i in self.separate_lines:
            tmp_tok, tmp_lvl  = self.tokenize(i, tmp_lvl)
            self.all_tokens.append(tmp_tok)
        
        # return tokens and filter out all comments
        return [item for sublist in self.all_tokens for item in sublist if item.type!="COMMENT"]

    def advance(self):
        if self.cursor < len(self.line)-1:
            self.cursor+=1
            self.charachter = self.line[self.cursor]
            self.column += 1
        else: self.cursor+=1

    # look forward and find the group of alphabetic characters
    # if the group of charechters matches a keyword, return a keyword token else return an identifier token
    def collect_id(self):
        value = ""
        while self.cursor < len(self.line) and self.charachter.isalpha():
            value+=self.charachter
            self.advance()
        if value in keywords:
            return Token(keywords[value], value, LineColumn(self.lineno, self.column))
        return Token("TOKEN_ID", value, LineColumn(self.lineno, self.column))   

    # look forward and collect every numeric charechter, return a number token
    def collect_number(self):
        value = ""
        while self.cursor <= len(self.line) and (self.charachter.isnumeric() or self.charachter == '.'):
            value+=self.charachter
            self.advance()
        if value[-1] == '.': value = value[:-1]
        value = float(value) if ('.' in value) else int(value)
        return Token("NUMBER", value, LineColumn(self.lineno, self.column))

    # collect all charachters inside of "", return a string token
    def collect_string(self):
        value = ''
        while self.cursor < len(self.line):
            
            self.advance()
            if self.charachter != '"':
                value += self.charachter
            else:
                self.advance()
                break
        return Token("STRING", value, LineColumn(self.lineno, self.column))

    # loop through each charechter and depending on the chaechter type, return a specific token.
    def tokenize(self, line, level):
        self.lineno += 1
        self.column = 0
        self.line = line.replace('    ', '\t')
        self.cursor = 0
        self.charachter = self.line[self.cursor]
        self.level = level
        tokens = []
        while self.cursor < len(self.line):
            # Token IDs & Keywords
            if self.charachter == '#':
                return [Token("COMMENT", "useless", LineColumn(self.lineno, self.column))], level
            elif level<self.line.count('\t'):
                tokens.append(Token("INDENT", '\t', LineColumn(self.lineno, self.column)))
                level += 1
                self.advance()
            elif level>self.line.count('\t'):
                tokens.append(Token("DEDENT", '\t', LineColumn(self.lineno, self.column)))
                level-=1
                self.advance()
            elif self.charachter.isalpha():
                tokens.append(self.collect_id())
            # Numbers
            elif self.charachter.isnumeric():
                tokens.append(self.collect_number())
            # Double Operators
            elif self.charachter == '"':
                tokens.append(self.collect_string())

            elif self.line[self.cursor:self.cursor+2] in double_operators:
                tokens.append(Token(double_operators[self.line[self.cursor:self.cursor+2]], self.line[self.cursor:self.cursor+2], LineColumn(self.lineno, self.column)))
                self.advance()
                self.advance()
            # Single Operators
            elif self.charachter in single_operators:
                tokens.append(Token(single_operators[self.charachter], self.charachter, LineColumn(self.lineno, self.column)))
                self.advance()
            else: self.advance()
        tokens.append(Token("EOL", "", LineColumn(self.lineno, self.column)))
        return tokens, level
    



            


    



    







    
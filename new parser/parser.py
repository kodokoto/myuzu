# <function_declaration> := <funtcion_protopype> <body>

class func_def:
    def __init__(self, span, proto, body):
        self.prototype = proto
        self.body = body
        self.span = span

# <function_prototype> := <identifier> "(" <signature>+ ")" "->" <return_type>

class func_proto:
    def __init__(self, span, name, signature, retun_type, access_spec=None):
        self.name = name
        self.signature = signature
        self.return_type = return_type
        self.span = span

# <function_signature> := (<type_token> <identifier>)+

class func_sig:
    def __init__(self, span, id_types, ids):
        self.id_types = id_types
        self.ids = ids
        self.span = span

# <body> := <statement>+

class body:
    def __init__(self, span, statements):
        self.statements = statements
        self.span = span

class expression:
    def __init__(self, span, lhs, rhs, op):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        self.span = span

def parse_simple_stmt(token):
    if token.type== 

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

def parse_statement(token):



from lexer import Lexer
from parser import Parser
import json
from json import JSONEncoder

class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return {o.__class__.__name__: o.__dict__}

def main():
    with open('examples/test.example', 'r') as file:
        content = file.read()
    lexer = Lexer(content)
    parser = Parser(lexer)
    parsed = parser.parse_program()
    json_out = json.dumps(parsed, indent=4, cls=EmployeeEncoder)
    with open('ast', 'w') as f:
        f.write(json_out)
    with open('tokens', 'w') as f2:
        f2.write(str(lexer.init_lex()))
main()
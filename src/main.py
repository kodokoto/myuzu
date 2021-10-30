from lexer import Lexer
from parser import Parser
import json
from json import JSONEncoder

class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def main():

    content = ''
    with open('examples/test.example', 'r') as file:
        content = file.read()
    lexer = Lexer(content)
    parser = Parser(lexer)
    parsed = parser.parse_program()
    print(json.dumps(parsed, indent=4, cls=EmployeeEncoder))
    with open('tokens', 'w') as f:
        f.write(str(lexer.init_lex()))

main()
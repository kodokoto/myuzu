from lexer import Lexer
from parser import Parser


def main():

    content = ''
    with open('examples/hello_world.mu', 'r') as file:
        content = file.read()

    lexer = Lexer(content)
    parser = Parser(lexer)

main()
#include <iostream>
#include "lexer.hpp"
#include <vector>



void tokenize(std::string input) {
    std::vector<Token> tokens;
    int cursor = 0;
    char current;
    while (cursor < input.length()) {
        current = input.at(cursor);
        if isNumeric(current)

        std::cout << current << std::endl;
        cursor++;
    }
}

int main() {
    std::string expression;
    std::cin >> expression;
    tokenize(expression);
}


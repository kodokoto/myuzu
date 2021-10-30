#include "lexer.hpp"
#include <memory>

class Span {

public:
    Span(LineColumn start, LineColumn end) {
        LineColumn Start = start;
        LineColumn End = end;
    }
};

class NumericLiteral {
public:    
    NumericLiteral(Span span, float value) {
        float Value = value;
        Span Span = span;
    }
};

class StringLiteral {
public:
    StringLiteral(Span span, std::string value) {
        std:: string Value = value;
        Span Span = span;
    };
};

class Identifier {
public:
    Identifier(Span span, std::string name, std::string type) {
        std::string Name = name;
        std::string Type = type;
        Span Span = span; 
    };    
};

// <function_declaration> := <funtcion_protopype> <body>
class Literal {
public: 
    virtual ~Literal() {};
};

class Expression {
public:
    virtual ~Expression() {}   
};

class BinaryExpression : public Expression {
    Expression LHS, RHS;

public: 
    BinaryExpression(Span span, char op, Expression lhs, Expression rhs) {
        char OP = op;
        Expression LHS = lhs;
        Expression RHS = rhs;
        Span Span = span;
    };
};


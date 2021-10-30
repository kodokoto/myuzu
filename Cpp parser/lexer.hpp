#include <string>
// using std::string;

class LineColumn {

public:
    int Line, Column;

    LineColumn(int line, int column) {
        Line = line;
        Column = column;
    }
};

class Token {

public:
    std::string Type, Value;
    
    Token(std::string type, std::string value, LineColumn pointer) {
        Type = type;
        Value = value;
        LineColumn Pointer = pointer;
    }
};



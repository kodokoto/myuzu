data Pointer

data Token = _type | value | pointer

data 

newtype Parser a = P (String -> [(a, string)])





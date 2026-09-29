import re
from enum import Enum, auto


class TokenType(Enum):
    LEFT_SQUARE_BRACKET = auto()
    RIGHT_SQUARE_BRACKET = auto()

    LOGICAL_NOT = auto()

    UNARY_MINUS = auto()
    UNARY_PLUS = auto()

    POWER = auto()
    REMAINDER = auto()

    BITWISE_SHIFT_LEFT = auto()
    BITWISE_SHIFT_RIGHT = auto()

    DIVIDE = auto()
    TIMES = auto()
    MINUS = auto()
    PLUS = auto()

    BITWISE_OR = auto()
    BITWISE_AND = auto()
    BITWISE_XOR = auto()

    SLOPPY_EQUAL = auto()
    STRICT_EQUAL = auto()
    SLOPPY_NOT_EQUAL = auto()
    STRICT_NOT_EQUAL = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_THAN_OR_EQUAL = auto()
    GREATER_THAN_OR_EQUAL = auto()

    LOGICAL_OR = auto()
    LOGICAL_AND = auto()

    IF = auto()
    ELSE = auto()

    ASSIGN = auto()
    TIMES_ASSIGN = auto()
    DIVIDE_ASSIGN = auto()
    REMAINDER_ASSIGN = auto()
    POWER_ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    BITWISE_OR_ASSIGN = auto()
    BITWISE_AND_ASSIGN = auto()
    BITWISE_XOR_ASSIGN = auto()

    LEFT_PARENTHESES = auto()
    RIGHT_PARENTHESES = auto()

    IDENTIFIER = auto()
    NUMBER = auto()


TOKEN_SPEC = [
    (TokenType.NUMBER,   r"\d+"),
    (TokenType.PLUS,     r"\+"),
    (TokenType.MINUS,    r"-"),
    (TokenType.TIMES,    r"\*"),
    (TokenType.DIVIDE,   r"/"),
]


def tokenize(code: str) -> [int]:
    return []

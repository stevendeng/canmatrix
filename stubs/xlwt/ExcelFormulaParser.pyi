# Stubs for xlwt.ExcelFormulaParser (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .ExcelMagic import *
from . import antlr
from typing import Any

class FormulaParseException(Exception): ...

SKIP: Any
INVALID_TYPE: Any
EOF_TYPE: Any
EOF: Any
NULL_TREE_LOOKAHEAD: Any
MIN_USER_TYPE: Any
TRUE_CONST: int
FALSE_CONST: int
STR_CONST: int
NUM_CONST: int
INT_CONST: int
FUNC_IF: int
FUNC_CHOOSE: int
NAME: int
QUOTENAME: int
EQ: int
NE: int
GT: int
LT: int
GE: int
LE: int
ADD: int
SUB: int
MUL: int
DIV: int
POWER: int
PERCENT: int
LP: int
RP: int
LB: int
RB: int
COLON: int
COMMA: int
SEMICOLON: int
REF2D: int
REF2D_R1C1: int
BANG: int
CONCAT: int

class Parser(antlr.LLkParser):
    tokenNames: Any = ...
    rpn: bytes = ...
    sheet_references: Any = ...
    xcall_references: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def formula(self) -> None: ...
    def expr(self, arg_type: Any) -> None: ...
    def prec0_expr(self, arg_type: Any) -> None: ...
    def prec1_expr(self, arg_type: Any) -> None: ...
    def prec2_expr(self, arg_type: Any) -> None: ...
    def prec3_expr(self, arg_type: Any) -> None: ...
    def prec4_expr(self, arg_type: Any) -> None: ...
    def prec5_expr(self, arg_type: Any) -> None: ...
    def primary(self, arg_type: Any) -> None: ...
    def sheet(self): ...
    def expr_list(self, arg_type_list: Any, min_argc: Any, max_argc: Any): ...

def mk_tokenSet_0(): ...

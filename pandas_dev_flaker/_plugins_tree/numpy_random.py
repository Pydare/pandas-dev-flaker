import ast
from typing import Iterator, Tuple

from pandas_dev_flaker._data_tree import State, register

MSG = "PDF020 found import from numpy.random"


@register(ast.ImportFrom)
def visit_ImportFrom(
    state: State,
    node: ast.ImportFrom,
    parent: ast.AST,
) -> Iterator[Tuple[int, int, str]]:
    if (
        node.module is not None
        and node.module.split(".")[:2] == ["numpy", "random"]
        or (
            node.module == "numpy"
            and "random" in {name.name for name in node.names}
        )
    ):
        yield node.lineno, node.col_offset, MSG


@register(ast.Import)
def visit_Import(
    state: State,
    node: ast.Import,
    parent: ast.AST,
) -> Iterator[Tuple[int, int, str]]:
    if ["numpy", "random"] in [
        name.name.split(".")[:2] for name in node.names
    ]:
        yield node.lineno, node.col_offset, MSG

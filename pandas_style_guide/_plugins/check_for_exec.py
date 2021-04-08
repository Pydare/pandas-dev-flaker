import ast
from pandas_style_guide._data import register

MSG = 'PSG001 do not use exec'
@register(ast.Call)
def check_for_exec(state, node, parent):
    if isinstance(node.func, ast.Name):
        if node.func.id == 'exec':
            yield (node.lineno, node.col_offset, MSG)
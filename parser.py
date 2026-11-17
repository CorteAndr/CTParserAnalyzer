import ast
import builtins
from collections import defaultdict
from computational_thinking import ProgElement


def get_ast(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    return tree


NODE_CATEGORIES = {
    ast.If: (ProgElement.SELECTION,),
    (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp): (ProgElement.ITERATION,),
    (ast.Assign, ast.AugAssign) : (ProgElement.VARIABLES, ProgElement.EXPRESSIONS,),
    (ast.Tuple, ast.List, ast.Set, ast.Dict): (ProgElement.DATA_STRUCTS,),
    ast.Return: (ProgElement.PARAMETERS_RETURNS,),
    ast.FunctionDef: (ProgElement.FUNCTIONS_PROCEDURES,),
    ast.Assert: (ProgElement.TESTING,),
}


def get_structures(file_path):

    ast_tree = get_ast(file_path)

    structures = defaultdict(set)

    for node in ast.walk(ast_tree):
        body = getattr(node, "body", None)

        # Direct relation
        for node_type, categories in NODE_CATEGORIES.items():
            if isinstance(node, node_type):
                for category in categories:
                    structures[category].add(node.lineno)

        # Conditional relations

        # A sequence starts where a block contains at least two statements.
        if not isinstance(node, ast.If):
            for statements in (
                body,
                getattr(node, "orelse", None),
                getattr(node, "finalbody", None),
            ):
                if isinstance(statements, list) and len(statements) >= 2:
                    structures[ProgElement.SEQUENCE].add(statements[0].lineno)
            
        # Check if a function has arguments
        if isinstance(node, ast.FunctionDef):
            if len(node.args.args) > 0:
                structures[ProgElement.PARAMETERS_RETURNS].add(node.lineno)
        # With ...
        elif isinstance(node, ast.With):
            for item in getattr(node, "items", None):
                if getattr(item, "optional_vars", None):
                    structures[ProgElement.VARIABLES].add(node.lineno)
        # For introduces an argument
        elif isinstance(node, ast.For):
            if isinstance(node.target, ast.Name) and node.target.id != '_':
                structures[ProgElement.VARIABLES].add(node.lineno)
        # Function calls
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else None
            # Function without a name/error?
            if name is None:
                pass
            # Function call to output
            elif name in {"print", "write"}:
                structures[ProgElement.OUTPUT].add(node.lineno)
            # Function call to input
            elif name in {"input", "read"}:
                structures[ProgElement.INPUT].add(node.lineno)
            # Function call to function with test_ in the name
            elif any(subs in name for subs in {'test_', '_test'}):
                structures[ProgElement.TESTING].add(node.lineno)
            # Conversion functions used for data types
            elif name in {'int', 'float', 'str', 'bool'}:
                structures[ProgElement.DATA_TYPES].add(node.lineno)
            elif name in {'open'}:
                if len(node.args) > 1:
                    if isinstance(node.args[1], ast.Constant):
                        if node.args[1].value in {'w', 'a'}:
                            structures[ProgElement.OUTPUT].add(node.lineno)
                        elif node.args[1].value == 'r':
                            structures[ProgElement.INPUT].add(node.lineno)
                else:
                    structures[ProgElement.INPUT].add(node.lineno)


            # Not a standard python function
            elif not callable(getattr(builtins, name, None)): 
                structures[ProgElement.FUNCTION_CALL].add(node.lineno)

    return structures

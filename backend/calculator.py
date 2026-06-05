import math
import ast

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    """Return cosine of angle x (in degrees) with improved precision.
    Rounds the result to 10 decimal places and treats values near zero as 0.0.
    """
    result = math.cos(math.radians(x))
    if abs(result) < 1e-10:
        return 0.0
    return round(result, 10)

def tan(x):
    return math.tan(math.radians(x))

# Safe functions mapping for evaluator
SAFE_FUNCTIONS = {
    'sin': sin,
    'cos': cos,
    'tan': tan
}

def safe_eval(expression: str) -> float:
    """
    Safely evaluate a mathematical expression containing numbers, basic operators,
    exponentiation (^), and trigonometric functions (sin, cos, tan).
    """
    if not expression.strip():
        raise ValueError("Expression is empty")
        
    # Replace ^ with ** for python AST power node representation
    expression_clean = expression.strip().replace('^', '**')
        
    try:
        node = ast.parse(expression_clean, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid syntax in expression: {e.msg}")

    def eval_node(node):
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"Unsupported constant value: {node.value}")
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            if isinstance(node.op, ast.Add):
                return add(left, right)
            elif isinstance(node.op, ast.Sub):
                return subtract(left, right)
            elif isinstance(node.op, ast.Mult):
                return multiply(left, right)
            elif isinstance(node.op, ast.Div):
                return divide(left, right)
            elif isinstance(node.op, ast.Pow):
                return left ** right
            else:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            elif isinstance(node.op, ast.UAdd):
                return +operand
            else:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in SAFE_FUNCTIONS:
                if len(node.args) != 1:
                    raise ValueError(f"Function {node.func.id} expects exactly 1 argument")
                arg = eval_node(node.args[0])
                return SAFE_FUNCTIONS[node.func.id](arg)
            else:
                raise ValueError(f"Unsupported function or call: {getattr(node.func, 'id', 'unknown')}")
        else:
            raise ValueError(f"Unsupported expression node: {type(node).__name__}")

    try:
        result = eval_node(node)
        if not isinstance(result, (int, float)):
            raise ValueError("Result of calculation is not a number")
        return float(result)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise ValueError(f"Evaluation error: {str(e)}")
        raise e


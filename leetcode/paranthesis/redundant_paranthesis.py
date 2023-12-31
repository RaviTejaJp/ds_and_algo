from __future__ import annotations


def solution(equation: str) -> bool:
    """We are trying to check if we have redundant parenthesis in the equation
    i.e.
    (a+b)  => no redundant parenthesis => False
    ((a+b)) => redundant parenthesis => True

    Args:
        equation (str): _description_

    Returns:
        bool: _description_
    """
    stack: list = []
    map = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for char in equation:
        if char in map:
            temp = None
            operator_flag = False
            while temp != map[char]:
                if stack:
                    temp = stack.pop()
                    if temp in '+-*/%^':
                        operator_flag = True
                else:
                    print(stack)
                    return 'Not Valid Parenthesis Equation'
            if operator_flag:
                pass
            else:
                return True
        else:
            stack.append(char)
    for item in stack:
        if item in map or item in map.values():
            return 'Not Valid Parenthesis Equation'
    return False


inputs = []
inputs.append('((a+b))')
inputs.append('((a+b)')
inputs.append('{[(a+b) + c]+d}+e')
inputs.append('((a+b)+(c))')

for input in inputs:
    print(f"Redundant Parenthesis present in '{input}' -- {solution(input)}")

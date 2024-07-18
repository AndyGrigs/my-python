def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
  
    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for problem in problems:
        parts = problem.split()
        if parts[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
    for i, problem in enumerate(problems):
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        if operator == '+':
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))
        
        width = max(len(operand1), len(operand2)) + 2

        if i > 0:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            if show_answers:
                answers_line += "    "
        
        first_line += operand1.rjust(width)
        second_line += operator + operand2.rjust(width - 1)
        dashes_line += '-' * width
        if show_answers:
            answers_line += answer.rjust(width)

        if show_answers:
            arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
        else:
            arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}"
    
    return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
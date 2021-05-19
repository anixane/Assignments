def InfixToPrefix(strr):

    def isOperator(op):
        if op in ['^','/','+','*','-']: return True
        return False

    if not strr: return None
    operandStack, operatorStack = [],[]
    for char in strr:
        if len(operatorStack)==0 and isOperator(char): 
            operatorStack.append(char)
        elif len(operatorStack)==0 or char == '(': 
            operandStack.append(char)
        elif char == ')':
            item = operandStack.pop()
            operandStack.pop()
            operandStack.append(item)
        elif isOperator(char): operatorStack.append(char)
        else:
            if operandStack[-1]=="(":
                operandStack.append(char)
                continue
            leftOperand = operandStack.pop()
            rightOperand = char
            operator = operatorStack.pop()
            result = operator+leftOperand+rightOperand
            operandStack.append(result)
    while operatorStack:
        rightOperand = operandStack.pop()
        leftOperand = operandStack.pop()
        operator = operatorStack.pop()
        result = operator+leftOperand+rightOperand
        operandStack.append(result)
    print(operandStack)

strr = "A+(B-C)*D"
strr2 = "A-(B/C)+E-(D/F)"
InfixToPrefix(strr)
InfixToPrefix(strr2)
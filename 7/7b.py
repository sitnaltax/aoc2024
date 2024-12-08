class Equation:
    def __init__(self, testValue, operands, operators):
        self.testValue = testValue
        self.operands = operands
        self.operators = operators

    def evaluate(self):
        result = self.operands[0]
        for i in range(len(self.operators)):
            if self.operators[i] == "+":
                result += self.operands[i + 1]
            elif self.operators[i] == "*":
                result *= self.operands[i + 1]
            else:
                result = int(str(result) + str(self.operands[i + 1]))

        return result == self.testValue

fstream = open("input.txt", 'r')
line = fstream.readline()
equations = []
while line:
    fragments = line.split(":")
    equations.append(Equation(int(fragments[0]), list(map(int, fragments[1].strip().split(" "))), []))
    line = fstream.readline()

#Recursively checks if the equation is solvable by adding or multiplying an operand
def checkIsEquationSolvable(equation):
    if len(equation.operators) == len(equation.operands) - 1:
        return equation.evaluate()
    else:
        newEquation1 = Equation(equation.testValue, equation.operands, equation.operators + ["+"])
        newEquation2 = Equation(equation.testValue, equation.operands, equation.operators + ["*"])
        newEquation3 = Equation(equation.testValue, equation.operands, equation.operators + ["|"])

        return checkIsEquationSolvable(newEquation1) or checkIsEquationSolvable(newEquation2) or checkIsEquationSolvable(newEquation3)
    
runningTotal = 0
for equation in equations:
    if checkIsEquationSolvable(equation):
        runningTotal += equation.testValue

print(runningTotal)
        
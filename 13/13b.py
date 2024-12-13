import pdb
import re
import numpy as np

# %ADJUSTMENT = 0
ADJUSTMENT = 10000000000000

class Machine:
    def __init__(self, x_a, y_a, x_b, y_b, goal_x, goal_y):
        self.x_a = x_a
        self.y_a = y_a 
        self.x_b = x_b
        self.y_b = y_b
        self.goal_x = goal_x + ADJUSTMENT
        self.goal_y = goal_y + ADJUSTMENT

    def __repr__(self):
        return f"Machine({self.x_a}, {self.y_a}, {self.x_b}, {self.y_b}, {self.goal_x}, {self.goal_y})"
    
    # Returns the best number of times to press A and B such that the goal is reached
    # A counts 3x as much as B
    def calculate_optimum(self):
        # The goals will be very high, so this needs to be solved as a linear system
        buttons = np.array([[self.x_a, self.x_b], [self.y_a, self.y_b]])
        goals = np.array([self.goal_x, self.goal_y])
        solution = np.linalg.solve(buttons, goals)

        if (solution[0] < 0 or solution[1] < 0):
            return 0
        print(self)
        print(solution)

        if (solution[0].round(3).is_integer() and solution[1].round(3).is_integer()):
            print(solution[0].round(3), solution[1].round(3))
            # pdb.set_trace()

            return (solution[0].round(3) * 3) + solution[1].round(3)

        return 0 

machines = []
fstream = open("input.txt", 'r')
line = "start"

# Returns two strings of digits from the input
def capture_digits(input):
    pattern = r'(\d+)[^\d]+(\d+)'
    results = re.findall(pattern, input)[0]
    return (results[0], results[1]) 

while line:
    line = fstream.readline()
    (x_a, y_a) = capture_digits(line)
    line = fstream.readline()
    (x_b, y_b) = capture_digits(line)
    line = fstream.readline()
    (goal_x, goal_y) = capture_digits(line)
    line = fstream.readline() #skip the blank line
    machines.append(Machine(int(x_a), int(y_a), int(x_b), int(y_b), int(goal_x), int(goal_y)))

total_tokens = 0
for machine in machines:
    total_tokens += machine.calculate_optimum()
print(total_tokens)


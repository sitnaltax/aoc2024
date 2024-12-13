import re

class Machine:
    def __init__(self, x_a, y_a, x_b, y_b, goal_x, goal_y):
        self.x_a = x_a
        self.y_a = y_a
        self.x_b = x_b
        self.y_b = y_b
        self.goal_x = goal_x
        self.goal_y = goal_y

    def __repr__(self):
        return f"Machine({self.x_a}, {self.y_a}, {self.x_b}, {self.y_b}, {self.goal_x}, {self.goal_y})"
    
    # Returns the best number of times to press A and B such that the goal is reached
    # A counts 3x as much as B
    def calculate_optimum(self):
        for b_presses in range(101):
            necessary_a_presses = (self.goal_x - self.x_b * b_presses) / self.x_a
            if not necessary_a_presses.is_integer():
                continue
            # now see if that makes the y coordinate match
            if self.y_a * necessary_a_presses + self.y_b * b_presses != self.goal_y:
                continue
            return (necessary_a_presses * 3) + b_presses

        #This could hypothetically fail if a is a multiple of b, so check that if this doesn't work

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
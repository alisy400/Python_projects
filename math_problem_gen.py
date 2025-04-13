import random
import time
import start

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10


def generating_operation():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    Operator = random.choice(OPERATORS)

    expr = str(left) + " " + Operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


WRONG = 0
print("enter to start")
print("--------------------")

start.time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generating_operation()
    while True:
        guess = input("problem #" + str(i + 1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        WRONG += 1

end_time = time.time()
total_time = round(end_time - start.time, 2)

print("--------------------")
print("Nice work!! You finished in", total_time, "seconds")

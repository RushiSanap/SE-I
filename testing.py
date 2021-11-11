from math import exp
from SE import evaluate
from random import randint, choice

ops = ["+", "-", "*", "/", "%", "^"]

maxOps = 10
maxNum = 10

for i in range(15):
    op_br = 0
    cl_br = 0


    currOps = randint(1, maxOps)
    expr  = ""
    expr += str(randint(1, maxNum))

    for j in range(currOps):
        op = choice(ops)

        expr += " " + op
        n = randint(0,1)
        if n == 0 :
            op_br += 1
            expr += " " + "("

        if op == '^':
            expr += " " + str(randint(0, 4))
        else:
            expr += " " + str(randint(1, maxNum))

        if n == 1 and cl_br < op_br :
            cl_br += 1
            expr += " " + ")"

    for k in range( op_br - cl_br):
        expr += " " + ")"

    expr_1 = expr.replace("^", "**")
    flag = 0

    try:
        ans = eval( expr_1)
        flag = 1
    except:
        pass

    if( flag == 1 ):
        if evaluate(expr) == ans :
            print("\nSuccessful for Test case no.", i+1)
        else:
            print("\nFail for Testcase no.", i+1)
            print("Expression:", expr)
            print("Your output:", evaluate(expr)," Expected Output:", ans )    
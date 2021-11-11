from random import randint, choice, uniform
from sys import argv
from random import randint, choice

argc = len(argv)
if argc < 2:
    print("usage: python3 testing.py filename custom_expression(optional)")
    exit()

filename = argv[1]
try:
    customExpr = argv[2]
# if custom input not given
except:
    customExpr = None
# import the evaluate function from filename
exec("from " + filename + " import evaluate")

def testExpr(expr: str) -> bool:
    flag = 0
    try:
        ans = eval(expr.replace("^", "**"))
        flag = 1
    except:
        return None
    
    if( flag == 1 ):
        if format(evaluate(expr), ".4f") == format(ans, ".4f") :
            return True
        else:
            return False

if customExpr != None:
    success = testExpr(customExpr)
    if success == None:
        print("Invalid expression")
        exit()
    if success:
        print("Successful")
    elif not success:
        print("Failed")
        print("Expression:", customExpr)
        print("Your output:", evaluate(customExpr)," Expected Output:", eval(customExpr))
    exit()

ops = ["+", "-", "*", "/", "%"]#, "^"]

maxOps = 10
maxNum = 10

i = 0
while i < 15:
    op_br = 0 # open bracket
    cl_br = 0 # closed bracket

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
            # uniform()
            expr += " " + str(randint(1, maxNum))

        if n == 1 and cl_br < op_br :
            cl_br += 1
            expr += " " + ")"

    for k in range( op_br - cl_br):
        expr += " " + ")"

    success = testExpr(expr)
    if success == True:
        print("\nSuccessful for Test case no.", i+1)
        i += 1
    elif success == False:
        print("\nFail for Testcase no.", i+1)
        print("Expression:", expr)
        print("Your output:", evaluate(expr)," Expected Output:", eval(expr))
        i += 1
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

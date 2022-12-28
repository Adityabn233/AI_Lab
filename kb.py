variable={'p':0,'q':1, 'r':2}
priority={'~':3,'v':1,'^':2}

def _opertn(i, val1, val2):
    if i == '^':
        return val2 and val1
    return val2 or val1
   
def isOprnd(c):
    return c.isalpha() and c != 'v'

def isLeftPar(c):
    return c == '('

def isRightPar(c):
    return c == ')'

def isEmpty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[-1]

def hasLessOrEqualPriority(c1, c2):
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False

def toPostfix(infix):
    stack = []
    postfix = ''
    for c in infix:
        if isOprnd(c):
            postfix += c
        else:
            if isLeftPar(c):
                stack.append(c)
            elif isRightPar(c):
                operator = stack.pop()
                while not isLeftPar(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    while (not isEmpty(stack)):
        postfix += stack.pop()

    return postfix

def evaluatePostfix(exp, comb):
    stack = []
    for i in exp:
        if isOprnd(i):
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_opertn(i, val2, val1))
    return stack.pop()

def CheckEntailment():
    kb=(input("Input the rule here: "))
    query=(input("Enter the query: "))
    combinations=[[True,True,True],
                  [True,True,False],
                  [True,False,True],
                  [True,False,False],
                  [False,True,True],
                  [False,True,False],
                  [False,False,True],
                  [False,False,False]]
    postfix_kb=toPostfix(kb)
    postfix_q=toPostfix(query)
    print("**** Truth Table reference ****")
    for combination in combinations:
        eval_kb=evaluatePostfix(postfix_kb,combination)
        eval_q=evaluatePostfix(postfix_q,combination)          
        print(eval_kb ,eval_q)
        if(eval_kb==True):
            if(eval_q==False):
                print("The Knowledge base does not entail the query..")
                return False
    print("The knowledge base Entails the query..")

if __name__ == "__main__":
    CheckEntailment()

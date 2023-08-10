def a_recursion(p):
    if (p>0):
        result=p + a_recursion(p - 1)
        print(result)
    else:
        result=0
    return result

a_recursion(7)

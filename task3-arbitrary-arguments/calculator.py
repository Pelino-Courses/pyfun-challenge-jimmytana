""""
calculator.py
simple calculator that add,divide,substract,mulitply using *args,and **kwags.

"""
def ad(*args):
    return sum(args)
def substract(*args):
    if len(args)< 2:
        raise ValueError("substraction needs two numbers.")
    result=args[0]
    for num in args[1:]:
        result-=num
    return result
def multiply(*args):
    result=1
    for num in args:
        result*=num
    return result
def divide(*args):
    if len (args)<2:
        raise ValueError("divide needs at least two numbers.")
    result=args[0]
    for num in args[1:]:
        if num== 0:
            raise ZeroDivisionError("cannot divide by zero")
        result /=num
    return result
def calculate(*args,**kwargs):
    """" perform calculation on given numbers.
    parameters:
    *args
    **kwargs
    we need to add ,substract,divide and multiply
    """
    if not isinstance(arg,(int,float)):
        raise TypeError("all arguments shuld be numbers.")
    operation=kwargs.get('operation')
    if operation =='add':
        return add(*args)
    elif operation=='substract':
        return substract(*args)
    elif operation=='multiply':
        return multiply(*args)
    elif operation=='divide':
        return divide(*args) 
    else :
        raise ValueError("invalid operation")
    if __name__=="__main__":
        test_cases=[(10,5,2),(100,10),(8,2,0),('a',2)]
        operations=['add','substract','multiply','divide']
        for op in operations:
            print("\noperation;{op}")
            for case in  operations:
                try :
                    result=calculate(*case,operation=op)
                    print(f"calculate{case},operation='{op}=>{result}")
                except Exception as e:
                    print(F"Error with input{case}:{e}") 
                    
        
    
     
        
    
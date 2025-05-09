"""
a calculator that performs basic arithmetic operation(addition,substraction,multiplication,division)
using arbitray positional and keyword arguments.
"""
def add(*args):
    """
    returns the addition of arguments passed
    """


    return sum(args)
def substract(*args):
    """
    returns the difference of the entered areguments
    """
    if len(args) < 2:
        raise ValueError("substraction needs two numbers.")
    result=args[0]
    for num in args[1:]:
        result-=num
    return result
def multiply(*args):
    """
    return the product of all arguments
    """
    result=1
    for num in args:
        result*=num
    return result
def divide(*args):
    """
    returns the result of division
    """
    if len (args)<2:
        raise ValueError("divide needs at least two numbers.")
    result=args[0]
    for num in args[1:]:
        if num== 0:
            raise ZeroDivisionError("cannot divide by zero")
        result /=num
    return result
def calculate(*args,**kwargs):
    """
    returns:float or int as the resurt of an arthimetic expression
    raises value error if invalid operation is specified
    raises type error if provided arguments are not number
    zerodivisionerror if you divide an number with zero
    """
    
    if not all(isinstance(arg,int) for arg in args):
        raise TypeError("all arguments shuld be numbers.")
    print("The kwargs are: ",kwargs)
    if kwargs.get('add'):
        return add(*args)
    elif kwargs.get('subtract'):
        return substract(*args)
    elif kwargs.get('multiply'):
        return multiply(*args)
    elif kwargs.get('divide'):
        return divide(*args) 
    else :
        raise ValueError("invalid operation")
    
    
# print(calculate(3,4,5, operation="add"))
    
if __name__=="__main__":
    test_cases=[(10,5,2),(100,10),(8,2,0),('a',2)]
    operations = [
        {
        "add": False,
        "subtract": True,
        "multiply": False,
        "divide": False,
        
    },
        {
        "add": True,
        "subtract": False,
        "multiply": False,
        "divide": False,
        
    },
        {
        "add": False,
        "subtract": False,
        "multiply": False,
        "divide": True,
        
    },
        {
        "add": False,
        "subtract": False,
        "multiply": True,
        "divide": True,
        
    },
    ]
    for op in operations:
        print("\noperation: {op}")
        for case in  test_cases:
            try :
                result=calculate(*case, **op)
                print(f"calculate{case},operation='{op}=>{result}")
            except Exception as e:
                print(F"Error with input{case}:{e}") 
                
    
    
     
        
    
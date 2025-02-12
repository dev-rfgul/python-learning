# create a decorator which tell the fuction which called it along with the  args


def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg)for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f" calling func{ func.__name__} with args {args_value} and key value {kwargs_value}")
        return func(*args, **kwargs)
        
    
    
    return wrapper







@debug
def greet(name,greeting="hello"):
    print(f"{greeting} , {name}")
    
greet("fahad", greeting="hanji")
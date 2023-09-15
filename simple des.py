from functools import wraps

def squares(func):
    @wraps(func)
    def inner(*args,**kwargs):
        for i in args:
            if i == 0 :
                raise ValueError("argument cant be zero")
        return func(*args,*kwargs)
    return inner

@squares
def qs(a,b):
    '''returns first argument raisded by the seccond'''
    return a ** b

print(qs(5,2))

from functools import wraps


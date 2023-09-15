def squares(a,b):
    if (a,b) != 0 :
        return a ** b
    else:
        raise ValueError("argument cant be zero")


new_squares = squares(0,0)

print(new_squares)
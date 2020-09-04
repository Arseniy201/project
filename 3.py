def my_func(*args):
    arg1 = int(input('Enter first num'))
    arg2 = int(input('Enter second num'))
    arg3 = int(input('Enter third num'))
    if arg1>=arg3 and arg2>=arg3:
        return arg1 +arg2
    elif arg1>arg2 and arg1<arg3:
        return arg1+arg3
    else:
        return arg2+arg3

print(my_func())
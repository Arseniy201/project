def my_func(x, y, z):
    my_list = [x, y, z]
    min_1 = min(my_list)
    my_list.remove(min_1)
    print(sum(my_list))
my_func(6, 7, -9)

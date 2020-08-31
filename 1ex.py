my_list=[12, 45.6789, False, [5, 6], -77, (2, 1)]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
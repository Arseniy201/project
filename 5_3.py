with open('5_3_приложение', 'r') as file_1:
    rich = []
    poor = []
    my_list = file_1.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        rich.append(i[1])
    print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, rich)) / len(rich)}')
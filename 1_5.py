cash = int(input('Введите выручку: '))
trouble = int(input('Введите издержки: '))

if cash < trouble:
    print('Работа в убыток')
else:
    print(f'Работа с прибылью, рентабельность составит {(cash - trouble) / cash} ')

workrs = int(input('Введите количество сотрудников '))

print(f'Прибыль на одного сотрудника {(cash - trouble) / workrs}')
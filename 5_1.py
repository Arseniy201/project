file = open('first.txt', 'w')
line = input('enter string \n')

while line:
    file.write(line)
    line = input('enter string \n')
    if not line:
        break
file.close()
file = open('first.txt', 'r')
content = file.readlines()
print(content)
file.close()
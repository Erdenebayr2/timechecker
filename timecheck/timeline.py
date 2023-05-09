import xlsxwriter

with open("time.txt","r") as file:
    content = file.read().split(" ")
    content = [element for element in content if element != '']
    x = []
    for el in content:
        x += el.split("\n")
    print(x)
    for i in range(0,len(x)-2):
        if x[i] == x[i+2]:
            x[i+2] = x[i+2]+'({})'.format(1)
        elif x[i] == x[i+2]:
            x[i+2] = x[i+2]+'({})'.format(2)
        else:
            continue
    # print(x)
    dict = {}
    for i in range(0,len(x), 2):
        key = x[i].strip(':')
        value = x[i+1]
        dict[key] = value
    print(dict)

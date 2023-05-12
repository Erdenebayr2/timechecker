import xlsxwriter

with open("time.txt","r") as file:
    content = file.read().split("\n")
    content = [element for element in content if element != '']
    contentx = [[item] for item in content]
    listuud = []
    new_listuud = []
for i in range(0,len(contentx)):
    lists = contentx[i][0].split(" ")
    lists = [element for element in lists if element != '']
    listuud.append(lists)
for sublist in listuud:
    for item in sublist:
        new_listuud.append(item)
print(new_listuud)

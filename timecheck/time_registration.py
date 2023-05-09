import xlsxwriter

with open("time.txt","r") as file:
    content = file.read().split("\n")
    content = [element for element in content if element != '']
    contentx = [[item] for item in content]
    dict = {}
for i in range(0,len(content)):
    lists = contentx[i][0].split(" ")
    lists = [element for element in lists if element != '']
    for z in range(0,len(lists),2):
        lists[z] = lists[z]+'({})'.format(z)
    print(lists)
    
    for i in range(0,len(lists), 2):
        key = lists[i].strip(':')
        value = lists[i+1]
        dict[key] = value
print(dict)

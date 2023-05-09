import xlsxwriter

data = [
    {
        'co':'00000001',
        '2023-02-01':'14:45:30',
        '2023-02-01':'15:45:30',
        '2023-02-03':'04:45:30',
        '2023-02-03':'09:15:30',
    },
        {
        'co':'00000002',
        '2023-02-01':'14:45:30',
        '2023-02-01':'15:45:30',
        '2023-02-03':'04:45:30',
        '2023-02-03':'09:15:30',
    },
        {
        'co':'00000016',
        '2023-02-01':'14:45:30',
        '2023-02-01':'15:45:30',
        '2023-02-03':'04:45:30',
        '2023-02-03':'09:15:30',
    },
]
# with open("time.txt","r") as file:
#     content = file.read().split(" ")
#     content = [element for element in content if element != '']
#     x = []
#     for el in content:
#         x += el.split("\n")
#     print(x)

workbook = xlsxwriter.Workbook("timecheck.xlsx")
worksheet = workbook.add_worksheet("firstSheet")

worksheet.write(0,0,'co')
worksheet.write(0,1,'2023-02-01')
worksheet.write(0,2,' ')
worksheet.write(0,3,'2023-02-03')
worksheet.write(0,4,' ')

for index, entry in enumerate(data):
    worksheet.write(index+1, 0, entry["co"])
    worksheet.write(index+1, 1, entry["2023-02-01"])
    worksheet.write(index+1, 2, entry["2023-02-01"])
    worksheet.write(index+1, 3, entry["2023-02-03"])
    worksheet.write(index+1, 4, entry["2023-02-03"])

workbook.close()
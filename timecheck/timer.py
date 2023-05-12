data = ['2023-03-01', '00000002', '2023-03-01', '10:14:11', '2023-03-01', '17:26:47', '2023-02-01', '00000002', '2023-02-01', '14:45:30', '2023-02-01', '14:45:30', '2023-02-06', '00000002', '2023-02-06', '13:06:23', '2023-02-06', '14:47:54', '2023-02-08', '00000002', '2023-02-08', '14:04:42', '2023-02-08', '17:21:14']

# Create an empty list for each set of keys and values
keys1, keys2, keys3,keys4 = [], [], [], []
values1, values2, values3,values4 = [], [], [], []

# Iterate through the input list two items at a time
for i in range(0, len(data), 2):
    # Append the keys and values to the appropriate lists
    if data[i] == '2023-03-01':
        keys1.append(data[i])
        values1.append(data[i+1])
    elif data[i] == '2023-02-01':
        keys2.append(data[i])
        values2.append(data[i+1])
    elif data[i] == '2023-02-06':
        keys3.append(data[i])
        values3.append(data[i+1])
    elif data[i] == '2023-02-08':
        keys4.append(data[i])
        values4.append(data[i+1])

# Create a list of dictionaries with the keys and values
output = [
    dict(zip(keys1, values1)),
    dict(zip(keys2, values2)),
    dict(zip(keys3, values3)),
    dict(zip(keys4, values4))
]

print(output)

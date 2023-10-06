matrix = [
    [1,2,3,23],[4,5,6,32],[7,8,9,232]
]

transposed=[]
for i in range(4):
    lst =[]
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst) 

print(transposed)     
 


"""
transpose in list comprehension
"""
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9], [23, 32, 232]]
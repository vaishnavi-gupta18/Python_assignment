matrix = []
for i in range(5):
   row = []
   ele= input().split()
   for j in range(5):
      if ele[j] == '1':
          x=abs(2-i)
          y=abs(2-j)
      row.append(ele)
   matrix.append(row)
print(x+y)

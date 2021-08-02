a = input()
a = a.lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for i in vowels :
    a = a.replace(i, '')
c = ''
for i in range(0,len(a)) :
    c = c + '.' + a[i]
print(c)

n = int(input())
c = input().split()
sum = 0
for i in range(n):
    c[i]=int(c[i])
    sum+=c[i]
c.sort(reverse=True)
s = 0
for i in range(n):
    s+=c[i]
    if(s > (sum/2)):
        print(i+1)
        break


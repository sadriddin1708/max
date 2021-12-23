ls = []
n = int(input('ELementlar sonini kiriting: '))

for i in range(n):
    a = int(input())
    ls.append(a)

print(ls)

kichik = min(ls)

print (kichik)
print ("{0} - o\'rinda turibdi".format(ls.index(kichik))) 

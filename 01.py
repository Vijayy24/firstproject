# list comprehension

"""ll = [i*i for  i in range (1,6)]
print(ll)

ll2 = [val for val in ll if val%2 ==0]

print(ll2)

n1 = [12,15,12,78,78,74,90]
n2 = [15,14,12,32,74,85,90]

n3= [x for x in n1 if x not in n2]

print(n3  )

for s in n1:
    if s  in n2:
        print(s)

birthday = {'vijay':'july 24','chandru':'oct 1','shankar':'now 5',}

while True:
    name = input('Enter name of you want....')
    if name in birthday:
        print(birthday[name]+ 'of his birthday ' + name)
        if name == '':
            break


    else:
            print('the birth date do not exit ...')

            bday = input('please update his birth date:  ')
            birthday[name] = bday
            print('your birthday database updated')


print('hi there\nhow are you\nnice to meet you')
print(r'hi there\n how are you\n nice to meet you')
"""
"""def isPhoneNumber(text):
    if len(text) != 12:
         return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
         return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

x= isPhoneNumber(784-747-8547)

print(x)


name = ['vijat','sherin','chandry','shankar']
l = [nam for nam in name]
print(l)



# Tuple:
t = (10,20,30,21,40,50,60,70,80,90,100)

t2 = (t[2:5])

t3  = t + t2
print(t[2:10:2])
print(t[-8:1])
print(t3)

print(sorted(t3,reverse=True))
print(sum(t3))
print(max(t3))
print(min(t3))

a, b, c, d = 12, 14, 15, 18
t = a, b, c, d
p, q, r, s = t

print(p)


x = eval(input("x:"))
print(x)"""


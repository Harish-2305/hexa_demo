#i/p=ASsasewWssadaweersdl
#o/p=aSsAsEwWssAdAwEErsdl
"""s=input()
a=""
b=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in b:
        if  i.islower():
            a+=i.upper()
        else:
            a+=i.lower()
    else:
        a+=i
print(a)"""

"""s=input()
a=""
b=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in b:
        a+=i.swapcase()
    else:
        a+=i
print(a)"""

#i/p=Pro Soccer or Pro Soccer
#o/p=reccoS orP or reccoS orp

"""a=input()
b=a[ : :-1]
fc=a[0].swapcase()
print(b[0:len(b)-1]+fc)"""

#i/p=Hello World
#o/p=El OLhLOwRD

"""s=input()
a=""
b=""
for i in range(len(s)):
    if i%2==0:
        a+=s[i].swapcase()
    else:
        b+=s[i].swapcase()
print(b+a)"""


#changing to upper or smaller without using lower and upper function
"""a=input()
b=""
for i in a:
    if ord(i)>=97:
        b+=chr(ord(i)-32)
    else:
        b+=chr(ord(i)+32)
print(b)"""

#to found the letter in string
"""a=input()
b=input()
if b in a:
    print("Found")
else:
    print("Not found")"""
"""print("found") if a.find(b) else print("Not found")"""

"""def check(a,b):
    if (a.find(b)==0):
        print("found")
    else:
        print("not found")
a=input()
b=input()
check(a,b)"""

#i/p=i am it student
#o/p=student it am i
"""a=input()
b=a.split(' ')
for i in range(len(b)-1,-1,-1):
    print(b[i],end=" ")"""

#changing lower vowels to upper
"""a=input()
b=0
d=''
c=['a','e','i','o','u']
for i in a:
    if i in c:
        d+=i.upper()
    else:
        d+=i
print(d)"""

"""a=input()
b=0
d=''
e=''
c=['a','e','i','o','u']
for i in a:
    if i not in c:
        d+=i
    else:
        e+=i
print(d)"""

#i am it student
#student it am i
"""a=input()
b=''
c=''
d=" "
for i in range(len(a)-1,-1,-1):
    b+=a[i]
for i in range(len(b)):
    if b[i]!=' ':
        c+=b[i]
    if b[i]==' 'or i == len(b)-1:
        d=""
        for j in range(len(c)-1,-1,-1):
            d+=c[j]
        c=""
        print(d,end=" ")"""

#amadm
#madam(palindrome) else not
"""def pal(s):
    a=[]
    for i in range(len(s)):
        if(s[i] in a):
            a.remove(s[i])
        else:
            a.append(s[i])
    if(len(s)%2==0 and len(a)%2==0 or len(s)%2==1 and len(a)%2==1):
        return True
    else:
        return False
s=input()
if(pal(s)):
    print("yes")
else:
    print("no")"""


"""n=int(input())
cit=()
for i in range(n):
    c=input()
    cit+=(c,)
print(cit)
s=input()
for i in cit:
    if(i.find(s)!=-1):
        print(i)"""

#i/p= i am student
#o/p =student.am.i
"""a=input()
b=a.split()
for i in range(len(b)-1,-1,-1):
    if i==0:
        print(b[i])
    else:
        print(b[i],end=".")"""
#i/p= i am it student
#o/p= 2 (the words between the first and last)
"""s=input()
c=0
for i in s:
    if i==" ":
        c+=1
print(c-1)"""

"""a=input()
b=input()
d=''
for i in a:
    if i not in b:
      d+=i
print( "NA" if d=="" else d)"""

"""a=input()
if a.istitle():
    print("yes")
else:
    print("no")"""

#i/p- a=xAbcyAAbcbAcbAbccz b=Abc  o/p=xyz
"""a=input()
b=input()
c=""
for i in a:
    if i.lower() not in b and i.upper() not in b:
        c+=i
print(c)"""

"""a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[i]<=a[j]:
            a[i],a[j]=a[j],a[i]
print(a)"""


#i/p=pdajras qxcpf
#o/p=program is fun
a=input()
b=['a','e','i','o','u']
c=a.split()
print(c)
for i in range(len(c)):
    c[i]=c[i][ : :-1]
    if i%2==0:
        for j in c[i]:
            if j in b:
                print(chr(ord(j)+17),end="")
            else:
                print(chr(ord(j)-3),end="")
    else:
        d=[]
        for j in c[i]:
            d.append(j)
        for j in range (len(d)):            
            if d[j] in b:
                print(chr(ord(d[j])+17),end="")
            elif j==len(d)-1 or j==len(d)-2:
                print(chr(ord(d[j])-3),end="")
            else:
                print(chr(ord(d[j])+3),end="")
                
    print(end=" ")

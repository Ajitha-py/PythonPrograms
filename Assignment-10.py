
'''
x=open('nthinfo.txt','w')
x.write('hello')
x.close()
'''

#1.Write a program to fetch all data from the file?
'''
x=open('nthinfo.txt','r')
y=x.read()
print(y)
'''
#2.Write a program to read the first line from the file?
'''
x=open('nthinfo.txt','r')
y=x.readline().replace('\n','').split(',')

print(y)
'''
#3.Write a program to read the last line from the file?
'''
x=open('nthinfo.txt','r')
y=x.readlines()

print(y[-1])
'''
#4Write a program read the 3rd line from file?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
print(y[3])
'''
#5.Write a program count total number of characters in the file?
'''
x=open('nthinfo.txt','r')
y=x.read()
print(len(y))
'''
#6.write a program to count total number of commas in the file?
'''
x=open('nthinfo.txt','r')
y=x.read()
count=0
for i in y:
    if ',' in i:
        count=count+1
print(count)
'''
#7.Write a program to number of words in the first line?
'''
x=open('nthinfo.txt','r')
y=x.readline().split(',')

print(len(y))
'''     
#8.Write a program total number of line in the file?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
print(len(y))
'''
#9.Write a program count total number of 'Sai' name in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
count=0
for i in y:
    if i=='Sai':
        count= count+1
print(count)
'''
#10.Write a program to fetch the first word in the eatch line?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
    st=i.split(',')
    print(st[0])

'''
#11.Write a program to fetch the last word from each line?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
    st=i.split(',')
    print(st[-1])
'''
#12.Write a program to fetch all words which start with'a' character?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
print(y)
for i in y:
    if 'a' in i:
        print(i)
'''
#13.Write a program to fetch all words which ends with an vowel?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')

for i in y:
    if i[-1] in 'aeiou':
        print(i)
'''
#14.Write a program to fetch all words which hAS either 'a' or 'i'character in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
for i in y:
    if 'a' or 'i' in i:
        print(i)
'''
#15.Write a program to fetch all words which contains only 5 character in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
for i in y:
    if len(i)==5:
        print(i)
'''
#16.Write a program to fetch all words which does not contains vowels except i in the file?

'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
for i in y:
    if 'i' in i and 'a' not in i and 'u' not in i and 'e' not in i and 'o' not in i:
        print(i)

'''
#17.Write a program to fetch all words which ends witn uppercase character in the fil?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i[-1].isupper()==True:
        print(i)
'''
#18.Write a program to count total number of character in the file excluding commas and \n?
'''
x=open('nthinfo.txt','r')
y=x.read()
count=0
for i in y:
    if ',' not in i and '\n' not in i:
        count=count+1
print(count)
'''
#19.Write a program to count total number of words in the file?

'''
x=open('nthinfo.txt','r')
y=x.read()
print(len(y))
'''
#20.Write a program to fetch all even number words from every line the file?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
print(y[::2])
'''
#21.Write a program to fetch all words which ends with 'bha'in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i.endswith('bha')==True:
        print(i)
'''
#22.Write a program to display all TCS employees?
'''
x=open('nthinfo.txt','r')
y=x.readline().replace('\n','').split(',')
for i in y:
    if 'TCS' not in i:
        print(i)
'''
#23.Write a program to display the company name of chinna employee?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
     st=i.split(',')
     if 'Chinna' in st:
         print(st[0])
   '''
#24.Write a program to fetch the 2nd from 3rd line in the file?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
z=y[2]
st=z.split(',')
print(st[1])
'''
#25.Write a program to fetch the first character from each word in the 3rd line?
'''
x=open('nthinfo.txt','r')
y=x.readlines()[2]
n=y.split(',')
for i in n:
    print(i[0])
'''
#26.Write a program to fetch the first and last character of each word in the last line?
'''
x=open('nthinfo.txt','r')
y=x.readlines()[-1]
z=y.split(',')
for i in z:
    print(i[0]+i[-1])
'''
#27.Write a program to fetch the all chacters(except 1st and last char)of each word in the 2nd line?
'''
x=open('nthinfo.txt','r')
y=x.readlines()[1]
z=y.split(',')
for i in z:
    print(i[1:-1])
'''
#28.Write a program to count total number of words whichwith 'S' character?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
count=0
for i in y:
    if 'S' in i[0]:
        
        print(i)
        count=count+1
print(count)
'''
#29.Write a program to fetch the all duplicates names in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().split(',')
lst=[]
for i in y:
    if i not in lst:
        lst.append(i)
    else:
        print(i)
'''
#30.Write a program to count all vowel in the file?(Note:output must be in dict)
'''
x=open('nthinfo.txt','r')
y=x.read()
v='aeiouAEIOU'
d={}.fromkeys(v,0)
for i in y:
    if i in d:
        d[i]=d[i]+1
print(d)
'''
#31.Write a program to reverse all words in the file?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
for i in y:
    print(i[::-1])
   '''
#32.Write a program to fetch all words which contains two or more then 'a' character?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i.count('a')>=2:
        print(i)
   '''
#33.Write a program to fetch all words which starts and ends with 'a' character?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i[0] in'Aa' and i[-1] in 'Aa':
        print(i)

'''
#34.Write a program to fetch word which has more number of 'a' character?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
lst=[]
for i in y:
    lst.append(i.count('a'))

for i in y:
    if max(lst)==i.count('a'):
        print(i)
'''
#35.write a program to fetch all company names which starts with vowel?
'''
x=open('nthinfo.txt','r')
y=x.readlines()

for i in y:
    st=i.split(',')[0]
    
    if st[0] in 'aeiouAEIOU':
        print(st)
   '''
#36.Write a program to display company name which contains saroj employee?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
    st=i.split(',')
    if 'Saroj' in st:
        print(st[0])
   '''
#37.Write a program to count all words which starts and ends with consonants?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
v='aeiouAEIOU'
count=0
for i in y:
    if i[0] not in v  and i[-1] not in v:
        count=count+1
print(count)
'''
#38.Write a program to fetch all company names which does not contain venkat employee?
'''  
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
    st=i.split(',')
    if 'Saroj' not in st:
        print(st[0])
'''
#39.Write a program to display company name where Narayana is working?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
    st=i.split(',')
    if 'Narayana'  in st:
        print(st[0])
'''
#40.Write a program to display the first word and last word from each line in dict format?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
lst=[]
for i in y:
    n=i.split(',')
    lst.append(n[0]+' '+ n[-1])
d={}.fromkeys(lst)
print(d)
'''
#41.Write a program to fetch all names whose name with 'a' in NTH company?
'''
x=open('nthinfo.txt','r')
y=x.readlines()


for i in y:
    n=i.split(',')
    if 'NTH' in n:
        for j in n:
            if j[0] in 'aA':
                print(j)
        
   '''



#42.Write a program to fetch total number of employees in CTS Company?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
lst=[]
for i in y:
    
    if 'CTS' in i.split(','):
        print(i)
        for j in i.split(',')[1:]:
            lst.append(len(j))
print(len(lst))
   '''     




#43.Write a program to fetch all companies where Venkat employee is working?
'''
x=open('nthinfo.txt','r')
y=x.readlines()
for i in y:
     st=i.split(',')
     if 'Venkat' in st:
         print(st[0])
'''
#44.Write a program to fetch all companies names which name starts with vowel?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')
lst=[]
for i in y:
    st=lst.append(i.split(','))
    if 'aeiou' in st:
        print(st)
'''


#45.Write a program to fetch to all palindrome names from the file?
'''
x=open('nthinfo.txt','r')
y=x.read().replace('\n',',').split(',')

for i in y:
    if i.lower()==i.lower()[::-1]:
        print(i)
   ''' 

#46.Write a program to fetch all companies names where  palindrome named employees working?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
for i in y:
    for j in i.split(','):
    
        if j.lower()==j.lower()[::-1]:
            print(j)
            print(i.split(',')[0])
'''
#47.Write a program to fetch to fetch lenghtiest company name?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
lst=[]
for i in y:
    lst.append(len(i.split(',')[0]))

for i in y:
   if  max(lst)==len(i.split(',')[0]):
       print(i.split(',')[0])
   ''' 

#48.Write a program to fetch to lenghtiest employee name in ABC company?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
lst=[]
for i in y:
    if 'ABC' in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))            
for i in y:
    if 'ABC' in i.split(','):
        for j in i.split(',')[1:]:
            if max(lst)==len(j):
                print(j)
   '''             

#49.Write a program to fetch to shortest employee name in the WIPRO company?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
lst=[]
for i in y:
    if 'WIPRO' in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))
for i in y:
    if 'WIPRO' in i.split(','):
        for j in i.split(',')[1:]:
            if min(lst)==len(j):
                print(j)
'''
#50.Write a program to count total number of employees in each company(in dict format)?
'''
x=open('nthinfo.txt','r')
y=x.read().split('\n')
lst=[]
for i in y:
    lst.append(i.split(',')[0])
d={}.fromkeys(lst,0)
for i in y:
    for j in i.split(','):
        if j in d:
            d[j]=len(i.split(',')[1:])
print(d)
            
'''















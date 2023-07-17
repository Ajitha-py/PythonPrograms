
#1.Write:
'''
x=open('nth.txt','w')
x.write('hello')
x.close()
'''
#2. read()
'''
x=open('nth.txt','r')
y=x.read()
print(y)
'''

#3.write a program read the last line from the file?
'''
print(open('nth.txt').readlines()[-1])

#o/p:CTS,Tarun,Satya,Renu,Anil,Sunil'''

#4.WAP to read the 2nd line from the file?
'''
print(open('nth.txt').readlines()[1])

#o/p:WIPRO,Nani,Srinu,Tarun,Ganga,Vikash
'''
#5.WAP to read the all lines from  lines from file?
'''
print(open('nth.txt').readlines())

#o/p.['TCS,Sai,Nani,Satya,Rajesh\n',
'WIPRO,Nani,Srinu,Tarun,Ganga,Vikash\n',
'INFOSYS,Hari,Giri,Siri,Teja,Prasad\n',
'CTS,Tarun,Satya,Renu,Anil,Sunil']
'''
#6.WAP to read first word from the second line?
'''
x=open('nth.txt','r')
y=x.readlines()
z=y[1]
st=z.split(',')
print(st[0])
'''
#7.WAP to read last word  from the last line?
'''x=open('nth.txt','r')
y=x.readlines()
z=y[3]
st=z.split(',')
print(st[-1])
'''
#8.WAP to read the first character from second word in the third line?
'''x=open('nth.txt','r')
y=x.readlines()
z=y[2]
st=z.split(',')
st3=st[2]
print(st3[0])'''
#9.WAP to read last word from the third line?
'''x=open('nth.txt','r')
y=x.readlines()
z=y[2]
st=z.split(',')
print(st[-1])
'''
#10.WAP to read all the words which starts with vowels?
'''x=open('nth.txt','r')
y=x.readlines()
vowels='aeiouAEIOU'
for i in y:
    z=i.split(',')
    for j in z:
        if j[0] in vowels:
            print(j)
   '''     
#11.WAP to read all the words which has only 4 characters?        
'''x=open('nth.txt','r')
y=x.readlines()
for i in y:
    z=i.split(',')
    for j in z:
        if len(j)==4:
            print(j)'''
#or
'''
x=open('nth.txt','r')
y=x.read().split(',')
for i in y:
    if len(i)==4:
        print(i)
   '''     

#12 WAP to read all words which starts and ends with consonants?
'''x=open('nth.txt','r')
y=x.readlines()
v='aeiouAEIOU'
for i in y:
    z=i.split(',')
    for j in z:
        if j[0] not in v and j[-1] not in v:
            print(j,end='\n')
   '''
#or
'''
x=open('nth.txt','r')
y=x.read().split(',')
v='aeiouAEIOU'
for i in y:
    if i[0] not in  v and i[-1] not in v:
        print(i)
   '''         

#13.WAP to read all the words  which contain u  character?
'''
x=open('nth.txt','r')
y=x.readlines()

for i in y:
    z=i.split(',')
    for j in z:
        if 'u' in j:
            print(j)
        
 #or
 '''
'''
x=open('nth.txt','r')
y=x.read().split(',')
for i in y:
    if 'u' in i:
        print(i)
        '''
#14.WAP to read first word from each line?
'''
x=open('nth.txt','r')
y=x.readlines()
for i in y:
    print(i[0])
    '''


#15.WAP to read last word from each line?
'''
x=open('nth.txt','r')
y=x.readlines()
for i in y:
     st=i.split(',')
     print(st[-1])
     
   ''' 
  


#16.WAP to read the last character of 3rd word 2nd line
'''
x=open('nth.txt','r')
y=x.readlines()
z=y[2]
st=z.split(',')
st2=st[2]
print(st2[-1])
'''
#17.WAP to read the biggest word in the file?
'''x=open('nth.txt','r')
y=x.readlines()
lst=[]
for i in y:
    st=i.split(',')
    for j in st:
        lst.append(len(j))
print(lst)
for i in y:
    st=i.split(',')
    for j in st:
        if max(lst)==len(j):
            print(j)
            '''
#.18 WAP to read the shortest word in the file?
'''x=open('nth.txt','r')
y=x.readlines()
lst=[]
for i in y:
    st=i.split(',')
    for j in st:
        lst.append(len(j))
print(lst)
for i in y:
    st=i.split(',')
    for j in st:
        if min(lst)==len(j):
            print(j)
'''
#20.WAP to COunt total Number of Character in the file(excluding , and \n)
'''x=open('nth.txt','r')
y=x.read()
count=0
for i in y:
    if ',' not in i and '\n' not in i:
        count=count+1
print(count)
'''
#19.WAP to count total number of words in the file?
'''
x=open('nth.txt','r')
y=x.readlines()
count=0
for i in y:
    st=i.split(',')
    for j in st:
        count=count+1
print(count)
'''
#21.WAP to count number of employee with name Tarun?
'''
x=open('nth.txt','r')
y=x.read().split(',')
count=0
for i in y:
    if i=='Tarun':
        count=count+1
print(count)

'''

#22.WAP COunt total number of commas in the file?
'''
x=open('nth.txt','r')
y=x.read()
print(y)
count=0
for i in y:
    if i==',':
        count=count+1
print(count)

'''
#23.WAP to COunt total number of \n in the file?
'''
x=open('nth.txt','r')
y=x.read()
count=0
for i in y:
    if i=='\n':
        count=count+1
print(count)
'''
#24.WAP to read all the employee of tcs company?
'''
x=open('nth.txt','r')
y=x.readline().split(',')
print(y[1:])
'''
#25.WAP to Disply the company name of ganga employee?
'''x=open('nth.txt','r')
y=x.read().split(',')
print(y)
for i in y:
    if i=='ganga':
        print(i)
'''
#26.WAP to read all words which are uppercase?
'''
x=open('nth.txt','r')
y=x.read().replace('\n',',').split(',')

for i in y:
    if i.isupper()==True:
        print(i)
'''

#27 WAP to display Which are repeated?
'''
x=open('nth.txt','r')
y=x.read().split(',')
lst=[]
for i in y:
    if i not in lst:
        lst.append(i)
    else:
        print(i)
'''

#28.WAP to COunt employee names whose name startwith's' character?
'''
x=open('nth.txt','r')
y=x.read().split(',')

count=0
for i in y:
    if i[0]=='S':
        count=count+1
print(count)
'''
#29.WAp to display company name which has less number of employee?

'''
x=open('nth.txt','r')
y=x.read().split(',')
'''

#30.WAP to Disply count all vowels in the file?

'''
x=open('nth.txt','r')
y=x.read()
v='aeiouAEIOU'
d={}.fromkeys(v,0)
for i in y:
    if i in d:
        d[i]=d[i]+1
print(d)
'''
        

        

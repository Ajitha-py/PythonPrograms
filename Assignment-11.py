
'''
x=open('empdata.txt','w')
x.write('hello')
x.close()
'''
x=open('empdata.txt','r')
y=x.read()
print(y)

#1.Write a pattern to verify whether the given mobile number is valid or not?
'''
import re
mobile=input('enter mobile number:')
m=re.fullmatch('[6-9]\d{9}',mobile)
if m==None:
    print('mobile number is invalid')
else:
    print('mobile number is valid')
   ''' 
#1.Write a program to fetch all employees name?
'''
x=open('empdata.txt','r')
y=x.read()

import re
z=re.findall('[Mr]{2}[s]?[.][A-Za-z]{1,}',y)
print(z)
'''
#2.Write a program to fetch all mobile numbers from file?
'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('[6-9]\d{9}',y)
print(z)
'''

#3.write a program to fetch all PAN number from file?
'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('[A-Z]{5}\d{4}[A-Z]{1}',y)
print(z)
'''
#4.write a program to fetch all email ids from file?
'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+', y)
print(z)
'''
#5.Write a program fetch the registration numbers from file?
'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('[A-Z]{2}\s?\d{2}\s?[A-Za-z]{1,}\s?\d{4}',y)
print(z)
'''

#6.write a program to fetch all compamy names?
'''
x=open('empdata.txt','r')
y=x.read()
import re
print([i.replace(' Company','') for i in re.findall('[A-Za-z]{1,} Company',y)])
'''
#7.Write a program fetch all date of births?

'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('\d{1,2}/\d{1,2}/\d{4}',y)
print(z)
'''
#8.Write a program to fetch company name Mr.Sai?
'''
x=open('empdata.txt','r')
y=x.readlines()

import re
for i in y:
    if 'Mr.Sai' in i:
        print(i)
        for j in re.findall('[A-Za-z]{1,} Company',i):
            print(j)
            s=j.replace(' Company','')
            print(s)


                
        print([j.replace(' Company','') for j in re.findall('[A-Za-z]{1,} Company',i)])

'''
#9.Write a Program to fetch emailid of Mr.Rohan?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mr.Rohan' in i:
        
        for j in re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+',i):
            print([j])
'''
#10.Write a program to fetch employee name who is using 9090909090?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if '9090909090' in i:
        for j in re.findall('[A-Za-z]{2}[.]\s[A-Za-z]{1,}',i):
            print(j)

'''
#11.Write a program to fetch PAN number of Mr. Satya?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mrs. Satya' in i:
        for j in re.findall('[A-Z]{5}\d{4}[A-Z]{1}',i):
            print([j])

'''
#12.Write a Program to fetch contact number of both Nani and Satya?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mr. Nani' in i or 'Mrs. Satya' in i:
        print([j for j in re.findall('[6-9]\d{9}',i)])
   '''
#13.WAP to fetch emp names of infosys and TCS company?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Infosys' in i  or 'TCS' in i:
        print([j  for j in re.findall('[A-Za-z]{1,3}[.]\s[A-Za-z]{1,}',i)])

'''
#14.WAP to fetch DOB of TCS employee?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'TCS' in i:
        print([j for j in re.findall('\d{1,2}/\d{1,2}/\d{4}',i)])
'''
#15.WAP fetch birth year of Mr.Nani?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mr. Nani' in i:
        print([j.replace('/','') for j in re.findall('/\d{4}',i)])
'''
#16.WAp to fetch the emp name whose mobile number starts with 8?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if re.findall('[8]\d{9}',i):
        print([j  for j in re.findall('[A-Za-z]{2}[.]\s[A-Za-z]{1,5}',i)])
'''
#17.Write a program to fetch odisha emp name?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if re.findall('[OD]\s?\d{2}\s?[A-Za-z]{1,}\s?\d{4}',i):
        print([j  for j in re.findall('[A-Za-z]{1,3}[.]\s[A-Za-z]{1,5}',i)])
'''
#18.Write a program to fetch youngest employee name
'''
import re
x=open('empdata.txt','r') 
y = max([int(i.replace('/','')) for i in re.findall('/\d{4}',x.read())])

z = open('empdata.txt','r').readlines()

for i in z:
    if str(y) in i:
        print(re.findall('Mr[s]?. [A-Za-z]{1,}',i))
    
'''

#19Write a Program to fetch all male employee?
'''
x=open('empdata.txt','r')
y=x.read()
import re
z=re.findall('[A-Z][a-z][.]\s[A-Za-z]{1,}',y)
print(z)
'''
#20.write a program to fetch total count of female employee?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
count=0
for i in y:
     if re.findall('[A-Za-z]{3}[.]\s[A-Za-z]{1,}',i):
         count=count+1
print(count)
'''
#22.Write a program contact number of Telagana Employee?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if re.findall('[TS]\s?\d{2}\s?[A-Za-z]{1,}\s?\d{4}',i):
                  print(re.findall('[6-8]\d{9}',i))
'''
#21.Write a program to fetch all employees names who born in january?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if re.findall('\d{1,2}/[0]?[1]/\d{4}',i):

        print([j  for j in re.findall('[A-Za-z]{1,3}[.]\s[A-Za-z]{1,5}',i)])


'''
#23.Write a program to fetch company name and Mobile Number of Wipro employee?
'''
x=open('empdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Wipro Company' in i:
        print((re.findall('([6-9]\d{9})', i)),re.findall('[A-Za-z]{1,3}[.]\s[A-Za-z]{1,}',i))
'''
#24.Write a Program to fetch emp name who born in leaf year?
'''
import re
x=open('empdata.txt','r').readlines()
lst=[]
for i in x:
    if re.findall('/\d{4}',i):
        lst.extend([i.replace('/','') for i in re.findall('/\d{4}',i)])
l=0
for i in x:
    if lst[l] in i and int(lst[l])%4==0:
        y=re.findall('Mr[s]?. [A-Za-z]{1,}', i)
        
        print(y)
    l=l+1
   ''' 
#25.Write a program to fetch all details of emp whose name not ends with vowels?







data= '''Mr.Narayana Trainer is teaching Python Language
since 5 years in both online mode and offline mode,
He also teaches Java Language very rarely.
Python course fee 3000Rs and Java course fee 2000Rs.
Mr.Roshan Trainer is also teaching SAP Course and MSBI Course.
'''
#1.Write a Program to fetch Trainers name?

import re


print([i.replace(' Trainer','') for i in re.findall('[A-Za-z]{1,} Trainer',data)])

#2.what are the languages that Mr.Marayana teach?

import re

print([i.replace(' Language','') for i in re.findall('[A-Za-z]{1,} Language',data)])

#3What are the mode that Mr.Narayana teach?

import re

print([i.replace(' mode','')for i in re.findall('[A-Za-z]{1,} mode',data)])

#4.what are the fee structure of both Python and java?

print([i  for i in re.findall('\d{4}+Rs',data)])

#5.what are the courses that Mr.Rohan teach?

import re

print([i.replace(' Course','') for i in re.findall('[A-Za-z]{1,} Course',data)])













































































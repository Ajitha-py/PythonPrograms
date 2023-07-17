
'''
x=open('testdata.txt','w')
x.write('hello')
x.close()
'''


x=open('testdata.txt','r')
y=x.read()
print(y)


#1. Write a pattern to get employee name who is working in TCS.
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'TCS' in i:
        print(re.findall('[a-zA-Z]{2}[.]\s?[a-zA-Z]{1,}\s?[A-Za-z]{8}',i))
'''
#2. Write a pattern to get employee name whose email id contains django?

x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'django' in i:
        print(re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+',i))
        
#3. Write a pattern to get employee name who born before 1990?

'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if '1990' in i:
        print(re.findall('[A-Za-z]{3}[.]\s?[A-Za-z]{1,}',i))
  '''      
#4. Write a pattern to get employee name who belongs to Andhra Pradesh?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'AP' in i:
        print(re.findall('[A-Za-z]{3}[.]\s?[A-Za-z]{1,}'),i)
'''


#5. Write a pattern to get employee name whose mobile number not starts with 90?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
print(re.findall(['[90]\d{0-8}'],y))
 '''
#6. Write a pattern to get employee name who contains orkut account?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
   if re.findall([A-Za-z]{1,}[\.][A-Za-z]{1,}@[A-Za-z]{1,}[.][A-Za-z]{1,}) in i:
       print(re.findall([A-Za-z]{3}[.]\s?[A-Za-z]{1,}),i)
'''
#7. Write a pattern to get employee name who born in March Month?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
     if re.findall('\d{2}[-][0][3][-]\d{4}',i):
          print(re.findall('Mr[s]?. [A-Z]?[a-z]{1,}\s?[a-z]{1,}',i))
'''  

#8. Write a pattern to get Company Name of Mr. Rajesh?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mr.Rajesh' in i:
        print(re.findall(i.replace(' company',' '),'[A-Za-z]{1,} company',i)))
   '''     
#9. Write a pattern to get Mobile Number of Mrs. Sravya?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mrs.Sravya' in i:
        print(re.findall('[6-9]\d{0-9}',i))
'''
#10. Write a pattern to get Company Names of all male employees?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
for i in y:
    if 'Mr' in i:
        print(re.findall('[A-Za-z]{2}[.][A-Za-z]{1,}',i))
   '''   
#11. Write a pattern to count total number of employees working in TCS?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
m=0
for i in y:
    if 'TCS' in i:
        m=re.findall('[A-Za-z]{2}[.]\s?[A-Za-z]{1,}\s?',i)
print(m)                     
   '''     

#12. Write a pattern to count total number of female employees?
'''
x=open('testdata.txt','r')
y=x.readlines()
import re
c=0
for i in y:
    if re.findall('[A-Za-z]{1,3}[.]\s?[A-Za-z]{1,}',i):
        c=c+1
print(c)
''' 

        
#13. Write a pattern to get date of birth of youngest employee?
'''
x=open('testdata.txt','r')
y=x.read()
import re
z=max([i.replace('-','') for i in re.findall('-\d{4}',y)])


x=open('testdata.txt','r')
y=x.readlines()
for i in y:
     if str(z) in i:
          print(re.findall('\d{2}[-]\d{2}[-]\d{4}',i))
  '''   

#14. Write a pattern to get the age of Mrs. Sonia?
'''
import re
import datetime as dt
today=dt.datetime.today()

x=open('testdata.txt','r')
y=x.readlines()

for i in y:
     if 'Mrs. Sonia' in i:
         n=[j.replace('-','')  for j in re.findall('-\d{4}',i)]
         print(n)
         for k in n:
              print(int(today.year)-int(k))
         
'''
'''
import datetime as dt
today=dt.datetime.today()
current_year=today.year
print(current_year)
x=current_year-2001
print(x)



print(today.year)
print(today.date)
print(today.month)
print(today.day)
print(today.second)
print(today.microsecond)
'''
#15. Write a pattern to get the age of oldest employee?
'''
import datetime as dt
import re


x=open('testdata.txt','r')
y=x.read()
today=dt.datetime.today()


z=min([i.replace('-','') for i in re.findall('-\d{4}',y)])
print(int(today.year)-int(z))
'''
        


'''
today=dt.datetime.today()
last=dt.datetime.last()
current_year=today.year
previous_year=last.year
print(current_year-previous_year)

'''












'''
import re
s = 'https://www.geeksforgeeks.org/'


obj1 = re.findall('(\w+)://',s)
print(obj1)

obj2 = re.findall('://www.([\w\-\.]+)', 
                  s)
print(obj2)




mobile number:'[6-9]\d{0-9}'

emailid:'[A-Za-Z0-9._+-]@[A-Za-z]+\.[A-Za-z]+'

                      '[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+'

'''









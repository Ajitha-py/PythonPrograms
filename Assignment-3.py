emp={
    'emp1':{'name':'Sai','salary':20000,'company':['TCS','Capgemini','Infosys'],'hTown':'Hyd'},
    'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Bangalor'},
    'emp3':{'name':'Satya','salary':40000,'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
    'emp4':{'name':'Rohit','salary':25000,'company':['Infosys','TCS','Defteam'],'hTown':'Pune'},
    'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','DeepCompute'],'hTown':'Hyd'},
    'emp6':{'name':'Sanjay','salary':45000,'company':['Wipro','Infosys','Defteam'],'hTown':'Mumbai'}
}
#1.Write a program to diplay the salary of sai?
'''
for i in emp:
    print(emp[i])
    if emp[i]['name']=='Sai':
        print(emp[i]['salary'])
        '''
#2.Write a program to display the home town of Nani?
'''
for i in emp:
    if emp[i]['name']=='Nani':
        print(emp[i]['hTown'])
   '''
#3.Write a program to display employee name who is working in pune?
'''
for i in emp:
    if emp[i]['hTown']=='Pune':
        print(emp[i]['name'])
'''

#4.write a program to display all companies name of satya?
'''
for i in emp:
    if emp[i]['name']=='Satya':
        print(emp[i]['company'])

'''
#5.Write a program to display all employees names who worked in TCS?
'''
for i in emp:
    if  'TCS' in emp[i]['company']:
        print(emp[i]['name'])
'''

#6.WAP to display all employees names who did not work in infosys?
'''
for i in emp:
    if 'Infosys' not in emp[i]['company']:
        print(emp[i]['name'])

'''
#7.WAP to Display all employee names?
'''
for i in emp:
    print(emp[i]['name'])
'''
#8.WAp to display the sum of all salaries?
'''
count=0
for i in emp:
    
    if emp[i]['salary']:
        count=count+emp[i]['salary']
print(count)
'''
#9.WAP to diplay the latest company of rohith?
'''
for i in emp:
    if emp[i]['name']=='Rohit':
        print(emp[i]['company'][-1])
'''
#10.WAP to diplay total companies count of satya?
'''
for i in emp:
    if emp[i]['name']=='Satya':
        print(len(emp[i]['company']))      

'''
#11.WAP to display employess names who are working in hyd?
'''
for i in emp:
    if emp[i]['hTown']=='Hyd':
        print(emp[i]['name'])
'''
#12.WAP to display the employee names who is  working in HCL?
'''
for i in emp:
    if 'HCL' in  emp[i]['company']:
        print(emp[i]['name'])
'''
#13.WAP to Display all employees whose name starts with 's'Character?
'''
for i in emp:
    if  emp[i]['name'].startswith('S'):
        print(emp[i]['name'])
'''
#14.WaP to display all employees whose name ends with vowel?
'''
for i in emp:
    if  emp[i]['name'].endswith(('a','e','i','o','u')):
        print(emp[i]['name'])

'''
#15.WAp to Display employee names who worked in DeepComputer?
'''
for i in emp:
    if 'DeepCompute' in emp[i]['company']:
        print(emp[i]['name'])
'''
#16.WAP to display the employee name who worked only in two companies?
'''
for i in emp:
    if len(emp[i]['company'])==2:
        print(emp[i]['name'])

   '''
#17.WAP to Display the Salary of pune employee?
'''
for i in emp:
    if emp[i]['hTown']=='Pune':
        print(emp[i]['salary'])

   '''
#18.WAP to display the location of employee who is taking 20000salary?
'''
for i in emp:
    if emp[i]['salary']==20000:
        print(emp[i]['hTown'])
        
'''
#19.WAP to display the salaries of Sai and Nani?
'''
for i in emp:
    if emp[i]['name']=='Sai':
        print(emp[i]['salary'])
        
    elif emp[i]['name']=='Nani':
        print(emp[i]['salary'])
'''
#20.Write A Program to display the name and salary of Bangalore employee?
'''
for i in emp:
    if emp[i]['hTown']=='Bangalor':
        print(emp[i]['name'],emp[i]['salary'])
'''
    


    

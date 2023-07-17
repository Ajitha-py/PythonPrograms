#1. Write a program to check whether a specific player is available in team or not, if not available then append in the team
'''
player=input('enter player name:')
team = ['Kohli', 'Dhoni', 'Sachin', 'Surya']

if player=='Kohli' or player=='Dhoni' or player=='Sachin' or player=='Surya':
    print('player is available in the team')
else:
    team.append(player)
    print(team)
   ''' 

#2. Write a program to check which language is learning by student. If he is learning Python
#then tell him/her that he/she is learning updated skill otherwise tell him/her to learn python
'''
n=input('which language is learning.')
if n=='python':
    print('please update your {} skills'.format(n))
else:
    print('please learn python course')
'''
#3. Write a program to check whether the given number is divisible by 10 or not?
'''
n=eval(input('enter the value:'))
if n%10==0:
    print('{} given number is divisible by 10'.format(n))
else:
    print('{} given number is not divisible'.format(n))
   ''' 

#4. Write a program to check what type of value is given by user?
'''
n=eval(input('enter your type of value:'))
if type(n)==int:
       print('entered value is int value')
elif type(n)==float:
    print('entered value is float value')
elif type(n)==bool:
    print('entered value is Bool Value')
elif type(n)==complex:
    print('entered value is complex value')

else:
    print('entered correct data type value')
'''

#
'''
lst=[10,'python',20,'kavya',30,'ajitha']
st1=[]
for i in lst:   
    if type(i) is str:
        st1.append(i)
print(st1)
'''
#5. Write a program to check whether a given string is available or not in the string?
'''
n=input('enter the given string:')
substring=input('enter the substring:')
if substring in n:
    print('string is available')
else:
    print('string is not avialble')
'''
#6. Write a program for following requirement: Monday, Tuesday, Wednesday, Thursday -->
#You can wear School Uniform Friday --> You can wear Civil Dress Saturday -->
#You can wear white and white Sunday --> Its your choice
'''
weekdays=input('enter week days:')
if weekdays=='Monday' or weekdays=='Tuesday' or weekdays=='Wednesday' or weekdays=='Thursday':
    print('you can wear school')
elif weekdays=='Friday':
    print('you can wear Civil Dress')
elif weekdays=='Saturday':
    print('you can wear white and white')
else:
    print('its your choice')
'''

#7. Write a program for following requirement: you need to ask user to enter name, gender.
#if gender is male then ask him to enter age. if age is more then 30 then ask him to marry.
#if gender is female then ask her to enter age. if age is more then 25 then ask her to marry.
'''
name=input('enter your Name:')
gender=(input('enter your Gender:'))
if gender=='male':
    age=eval(input('enter your age:'))
    if age>30:
             print('please ask to get marry.')
    else:
         print('wait for some time,')
elif gender=='female':
    age=eval(input('enter your age:'))
    if age>25:
        print('please to get marry')
    else:
        print('wait for some time.')
'''

#8. Write a program for following requirement: 0 to 5 --> You are an Infant 6 to 16 --> You are school going kid 17 to 22 -->
#You are college going kid 23 to 30 --> You need to settle in life and get marry 31 to 45 -->
#You need to work and earn money 46 to 60 --> You need to do business 61 and above -->
#You need to take rest. below 0 --> Invalid Age, please check once
'''
n=eval(input('please enter any number:'))
if n>0 and n<5:
    print('{} you are an infant'.format(n))
    
elif n>6 and n<16:
    print('{}you are school going kid'.format(n))
elif n>17 and n<22:
    print('{} you are college going kid'.format(n))
elif n>23 and n<30:
    print('{}you need to settle in life and get marry'.format(n))
elif n>31 and n<45:
    print('{} you need to work and earn money'.format(n))
elif n>46 and n<60:
    print('{} you need to business'.format(n))
elif n>65:
    print('{} you need to take rest'.format(n))
else:
    print('{} Invalid Age'.format(n))

'''


#9. Write a Python Program to find BMI(Body Mass Index)? Take height (in cms) and weight (in kgs) from user.
#Calculate BMI by using height and weight. Note: Convert cms into metres BMI = Weight(in kg) /
#Height*Height(in metre) if BMI between 0 and 18.5, display "Underweight",
#if BMI between 18.5 and 24.9, display "Normal Weight" if BMI between 25.0 and 29.9, display "Pre-Obesity"
#if BMI between 30.0 and 40.0, display "Obesity" if BMI between 40.
#and above, display "Extremly Obesity".
'''
height=eval(input('enter your height in centi meters:'))
weight=eval(input('enter your weight in kgs:'))
print('welcome to BMI calculator:')
BMI = weight/height*height
print(BMI)
            
if BMI>0 and BMI<18.5:
    print('underweight',BMI)
    
elif BMI>18.5 and BMI<24.9:
    print('Normal Weight',BMI)
    
elif BMI>25.0 and BMI<29.9:
    print('Pre-Obesity',BMI)
    
elif BMI>30.0 and BMI<40.0:
    print('obesity',BMI)
    
elif BMI>40.0:
    print('Extremly Obesity',BMI)
''' 





#10. Write a Python Program to take any one number from user, that number must be between 1 and 10.

#If the number is below 1 or more than 10 then display "Please enter any number between 1 and 10".
#If the number between 1 and 10 then check it whether the number divisible by 2 or not.
#If the number divisible by 2 then display "You have entered even number."
#If the number is not divisible by 2 then display "You have entered odd number."

'''
n=eval(input('please enter any number'))

if n<1 and n>10:
    print('{}Please enter any number between 1 and 10'.format(n))
elif n>0 and n<10:
       if n%2==0:
        print('{} given number is divisiable 2 and even number'.format(n))
       else:
           print('{} given number is not divisible by 2 and odd number'.format(n))
else:
    print('please enter between 1 to 10')
   '''     


'''
a=eval(input('enter first number'))
b=eval(input('enter second number'))
c=eval(input('enter third number'))
if a>b and a>c:
    print('the highest number is {}'.format(a))
elif b>a and b>c:
    print('the highest number is {}'.format(b))
elif c>a and c>b:
    print('the highest number is{}'.format(c))
else:
    print('given the proper number')
'''






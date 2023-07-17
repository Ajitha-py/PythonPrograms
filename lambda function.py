#1.write a lambda Expression tofilter even numbers from list?
lst=[5,8,3,7,9,12]
'''
print(list(filter(lambda i: i%2==0,lst)))
'''
#2.WA lambda Expression tofilter all number which are divisible by both 3 and 6?
lst=[12,15,21,30,24]
'''
print(list(filter(lambda i: i%3==0 and i%6==0,lst)))
'''
#3.WA lambda Expression tofilter all words which starts with Uppercase?
lst=['Python','django','Narayana','Hyderabad']
'''
print(list(filter(lambda i:i[0].isupper(),lst)))
'''
#4.Write a lambda Expression to filter all words which contains only 6 characters?
st='python is simple and easy lanugage'
'''
print(list(filter(lambda i:len(i)==6,st.split())))
'''
#5.Write a lambda Expression to filter all words which are palindrome?
'''
names=['Python','madam','django','malayalam']

print(list(filter(lambda i: i==i[::-1],names)))
'''
#6.write a lambda Express to filter all words which not contains 'm' character?
'''
names=['python','madam','django','malayalam']

print(list(filter(lambda i: 'm' not in i,names)))
'''
#7.Write a lambda Expression to filter all vowels from given string?
'''
st='python'
print(list(filter(lambda i: i in 'aeiou',st)))
'''
#8.Write a lambda expression to filter the biggest word in the list?
'''
names=['python','madam','django','malayalam']
print(list(filter(lambda i: len(i)==max(len(i) for i in names),names)))
'''
#9.write a lambda expression to filter the smallest pallindrom word in the list?
'''
names=['python','madam','django','malayalam']

x= [i for i in names if i==i[-1::-1]]
print(x)



print(list(filter(lambda i: len(i)==min([len(i) for i in [i for i in names if i==i[-1::-1]]]),x)))
'''
#10.Write a lambda Expression to filter all bool values from list?
'''
lst=['python',10,False,2+3j,True]
print(list(filter(lambda i: type(i) is bool,lst)))
'''
#11.Write a lambda Expression to filter all duplicate word given string?
'''
st='python is easy lanuguage because python is easy to understand'

print(list(set((filter(lambda i:st.count(i)>=2,st.split())))))
'''

#MAP Function():

#1.WA Lambda Expression to add 5 and each element in the list?
'''
lst=[10,20,30,40,50]
print(list(map(lambda i:i+5,lst)))
'''
#2.Write a lambda Expression to find the square of each element?
'''
lst=[3,5,6,3,8]
print(list(map(lambda i:i*i,lst)))
'''
#3.Write a lambda expression to fetch the first character from each word?
'''
st='python narayana tech house'
print(list(map(lambda i: i[0],st.split())))

'''
#4.Write a lambda Expression to find the length of each word?
'''
st='python narayana tech house'

print(list(map(lambda i:len(i),st.split())))
'''
#5.Write a lambda expression to fetch all word except first and last character?
'''
st='python narayana tech house'

print(list(map(lambda i:  i[1:-1],st.split())))
'''
#6.Write a lambda expression to fetch  first and last character from each word?
'''
st='python narayana tech house'

print(list(map(lambda i:  i[0]+i[-1],st.split())))
'''
#7.write a lambda expression to find the cubes of all odd number?
'''
lst=[2,3,5,4,6]

x=[i  for i in lst if i%2!=0]
print(list(map(lambda i:i**3,x)))
'''
#8.Write a lambda Function to display the next number of each even number?
'''
lst=[2,True,'a',4,7,2+3j]
x=[i  for i in lst if type(i) is int and i%2==0]
print(list(map(lambda i:i+1,x)))
'''
#9.Write lambda expression to find the length of each word which starts with vowel?
'''
st='Python is easy language because python is to understand'

x=[len(i) for i in st.split() if i[0] in 'aeiouAEIOU']
print(list(map(lambda i: i,x)))
'''
#10.Write a lambda expression to find the length of top 3 biggest words in string?
'''
st='Python is easy language because python is to understand'

x=sorted([len(i) for i in st.split()])[-3:]


print(list(map(lambda i: i,x)))
'''
#11.Write a lambda expression to reverse the three smallest words in string?
st='Python is easy language because python is to understand'
a=sorted(set([i[-1::-1] for i in st.split()]))[-3::]
print(a)

















         


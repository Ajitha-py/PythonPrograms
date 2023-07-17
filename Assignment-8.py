#1.Write a Comprehension to fetch all even number from list?
'''
lst=[10,11,13,14,9,8]
print([i for i in lst if i%2==0])
'''
#2.1.Write a Comprehension to fetch all string values from list?
'''
lst=[10,'a',True,'b',False]
print([i  for i in lst if type(i)==str])
'''
#3.1.Write a Comprehension to fetch all5 divisibles from list?
'''
lst=[12,15,27,20,5]
print([i for i in lst if i%5==0])
'''
#4.Write a Comprehension to count total number of int values in the list?
'''
lst=[10,'a',20,True,30,'b',40]
print(len([i for i in lst  if type(i)==int]))
'''
#5.Write a Comprehension to count total number of characters in the string(including space)?
'''
st='python language'
print(len([i for i in st]))
'''
#6.Write a Comprehension to count total number of words in the string.
'''
st='python narayana tech house hyd'
print(len([i for i in st.split()]))
'''
#7.1.Write a Comprehension to fetch all vowels from the string?
'''
st='python language'
print([ i  for i in st if i in 'aeiou'])

'''
#8.1.Write a Comprehension to count total number of vowels.
'''
st='python narayana'
print(len([i for i in st if i in 'aeiou']))
'''
#9.1.Write a Comprehension to count total number of character in the string(excluding spce)?
'''
st='python is a simple language'
print(len([i for i in st  if i.isspace()!=True]))
'''
#10.Write a Comprehension to count total number of consonants in the string?
'''
st='python language'
print(len([i for i in st if i not in 'aeiou']))
'''
#11.Write a Comprehension to fetch all words which starts with vowel from given string?
'''
st='python is simple and easy language'
print( [i for i in st.split() if i[0] in'aeiou'])
'''
#12.Write a Comprehension to fetch all words which ends with consonant in the given string?
'''
st='python is simple and easy language'
print( [i for i in st.split() if i[-1] not in'aeiou'])

'''
#13.Write a Comprehension to fetch all words which 'a' two or more then two times?
'''
st='python is simple and easy language'
print([i for i in st.split() if i.count('a')>=2])
'''
#14.Write a Comprehension to count number of characters of each word in the string?
'''
st='python is simple and easy language'
print([len(i) for i in st.split()])
'''
#15.Write a Comprehension to fetch the first and last character from each word in the string?
'''
st='python is simple and easy language'
print([ i[0]+i[-1] for i in st.split() ]) 

'''
#16.Write a Comprehension to fetch all the words which contain 'a' character in the string?
'''
st='python is simple and easy language'
print([i for i in st.split() if 'a' in i])
'''
#17.Write a Comprehension to fetch all the words which does not contain 'e' character in string?
'''
st='python is simple and easy language'
print([i for i in st.split() if 'e' not in i])
'''
#18.Write a Comprehension to fetch all the words which contain only 4 or lessthen 4 characters?
'''
st='python is simple and easy language'
print([i  for i in st.split() if len(i)<=4])
'''
#19.Write a Comprehension to fetch all the words which contain odd number of characters in the string?
'''
st='python is simple and easy language'
print([i  for i in st.split() if len(i)%2!=0])

'''
#20.Write a Comprehension to fetch all the words which starts and ends with vowel in the string?
'''
st='python is number one language'
print([i for i in st.split() if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''
#21.Write a Comprehension to fetch all palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']

print([i for i in names if i==i[::-1]])

'''
#22.Write a Comprehension to fetch all non palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']

print([i for i in names if i!=i[::-1]])
'''
#23.Write a Comprehension to fetch all palindrome words which starts with 'm' character?
'''
names=['madam','python','dad','language','eye','malayalam']

print([i for i in names if i.startswith('m')==True])
'''
#24.Write a Comprehension to fetch all palindrome words which more then 3 character?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i==i[::-1] and len(i)>3])
'''
#25.Write a Comprehension to fetch all longest palindrome word?

names=['madam','python','dad','language','eye','malayalam']

print([i for i in names if i==i[-1::-1] and len(i)==max([len(i) for i in names if i==i[-1::-1]])])


'''
name=['python','madam','django','malayalam','language','dad']
lst=[]
for i in name:
    if i==i[-1::-1]:
        lst.append(len(i))
for i in name:
    if i==i[-1::-1] and len(i)==min(lst):
        print(i)
print([i for i in name if i==i[-1::-1] and len(i)==min([len(i) for i in name if i==i[-1::-1]])])

'''















    

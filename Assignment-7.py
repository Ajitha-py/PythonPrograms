#1.Write a program to fetch all even numbers from list?
'''
lst=[10,11,13,14,9,8]
newlst=[]
for i in lst:
    if i%2==0:
        newlst.append(i)
print(newlst)
'''
#2.WAP to fetch all string values from list?
'''
lst=[10,'a',True,'b',False]
newlst=[]
for i in lst:
    if type(i)==str:
        newlst.append(i)
print(newlst)
'''
#3.WAP to fetch all 5 divisiables from list?
'''
lst=[12,15,27,20,5]
newlst=[]
for i in lst:
    if i%5==0:
        newlst.append(i)
print(newlst)
'''
#4.WAP to count total number of int values in the list?
'''
lst=[10,'a',True,30,'b',40]
count=0
for i in lst:
    if type(i)==int:
        count=count+1
print(count)
'''
#5.WAP to count total number of character in the string(including space)?
'''
st='python language'
print(len(st))
or
st='python language'
count=0

for i in st:
     count=count+1
print(count)
'''
#6.WAP to count number of total number of words in the string?
'''
st='python narayana tech house hyd'
x=st.split()
count=0
for i in x:
    count=count+1
print(count)
'''
#7.WAP to Fetch all vowels from the string?
'''
st='python language'
v='aeiou'
newlst=[]
for i in st:
    if i in v:
        newlst.append(i)
print(newlst)
   '''
#8.WAP to count total number of vowels:
'''
st='python narayana'
v='aeiou'
count=0
for i in st:
    if i in v:
        count=count+1
print(count)
'''
#9.WAP to count total number of character in the (excluding space)?
st='python lanuage'
'''
x=st.split()
st1=''.join(x)
print(len(st1))
or
count=0
for i in st1:
    count=count+1
print(count)
or
count=0
for i in st:
    if i.isspace()!=True:
        count=count+1
print(count)
'''
#10.WAP to count total number of consonants in the string?
'''
st='python lanuage'
v='aeiou'
count=0
for i in st:
    if i not in v:
        count=count+1
print(count)
'''
#11.WAP to fetch all words which starts with vowel from given string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if i[0]in 'aeiou':
        newlst.append(i)
print(newlst)
   '''
#12.WAP to fetch all words which ends with cononent in the given string/
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if i[-1] not in 'aeiou':
        newlst.append(i)
print(newlst)
'''
#13.WAP to fetch all words which 'a' two or more then two times?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if i.count('a')>=2:
        newlst.append(i)
print(newlst)
'''
#14.WAP to count number of characters of each word in the string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    newlst.append(len(i))
print(newlst)
'''
#15.WAP to fetch the first and last character from each word in the string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    newlst.append(i[0]+i[-1])
print(newlst)
'''
#16.WAP to fetch all words which contains 'a' character in the string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if 'a' in i:
        newlst.append(i)
print(newlst)
'''
#17.WAP to fetch all words which does not contain 'e' character in string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if 'e' not in i:
        newlst.append(i)
print(newlst)
'''
#18.WAP to fetch all words which contains only 4 or lessthen 4 character?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if len(i)<=4:
        newlst.append(i)
print(newlst)
'''
#19.WAP to fetch all words which contain odd number of character in the string?
'''
st='python is simple and easy language'
x=st.split()
newlst=[]
for i in x:
    if len(i)%2!=0:
        newlst.append(i)
print(newlst)
'''
#20.WAP to fetch all words which starts and ends with vowel in the string?
'''
st='python is number one language'
x=st.split()
newlst=[]
v='aeiou'
for i in x:
    if i[0] in v and i[-1] in v:
        newlst.append(i)
print(newlst)
'''
#21.WAP to fetch all palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
newlst=[]
for i in names:
    if i==i[::-1]:
        newlst.append(i)
print(newlst)
'''
#22.WAP to fetch all non palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
newlst=[]
for i in names:
    if i!=i[::-1]:
        newlst.append(i)
print(newlst)
'''
#23.WAP to fetch all  palindrome words which starts with 'm' character?
'''
names=['madam','python','dad','language','eye','malayalam']
newlst=[]
for i in names:
    if i==i[::-1] and 'm'in i[0]:
        newlst.append(i)
print(newlst)
'''
#24.WAP to fetch all  palindrome words which more then 3 character?
'''
names=['madam','python','dad','language','eye','malayalam']
newlst=[]
for i in names:
    if i==i[::-1] and len(i)>3:
        newlst.append(i)
print(newlst)
   '''
#25.WAP to longest palindrome word?
'''
names=['madam','python','dad','language','eye','malayalam']
newlst=[]
for i in names:
    if i==i[::-1]:
        newlst.append(len(i))
#print(newlst)  #[5, 3, 3, 9]
for i in names:
    if max(newlst)==len(i):
        print(i)
   '''     

    









    
    
    
































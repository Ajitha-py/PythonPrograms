
#1.
'''
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*' ,end=' ')
    print()
 '''
#2.
'''
n=int(input("Number of Rows:"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print('*',end=' ')
    k=k+2
    print()
'''
#9.
'''
n=int(input("Number of Rows:"))
for i in range(1,n+1):
      for j in range(1,i):
          print('5',end=' ')
      print()

 '''  
#6
'''
n=int(input('Number of Rows:'))
for i in range(1,n+1):
      for j in range(1,i+1):
          print(j,end=' ')
      print()
'''

#4.
'''
n=int(input('Number of Rows: '))
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
   '''
#5
'''
n=5
for i in range(1,n+1):
    for j in  range(1,n+2-i):
        print(j, end='')
    print()
'''
#3 didnt understand:
'''
n=5
for i in range(0,n):
    for j in range(1,n-i-1):
        print(end=' ')
        
        for j in range(0,i+1):
            print('*',end=' ')
        print()
'''
#8
'''
n=int(input('number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n, end=' ')
    print()
   '''          

#7.
'''
n=int(input('number of rows:'))
for i in range(1,n):
    for j in range(1,n+2-i):
        print(n+1-i,end=' ')
    print()

n=int(input('number of rows:'))
for i in range(n):
    print('* '*(i+1))


n=int(input('number of rows:'))
for i in range(n):
    for j in range(i+1):
        print(n,end=' ')
    print()
'''


#4.
'''
n=int(input('number of rows:'))
for i in range(n):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

'''
#6.
'''
n=int(input('number of rows:'))
for i in range(n):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
#9.
'''
n=int(input('number of rows:'))

for i in range(n):
    for j in range(1,i+1):
        print(n,end=' ')
    print()
   '''
#5
n=5
'''
for i in range(n):
    print((str(i+1)+ ' ')*(n-i))

for i in range(n):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


for i in range(1,n):
    for j in range(1,n+1-i):
        print(i,end=' ')
    print()

'''
#15
'''
n=int(input('number of rows:'))
for i in range(n):
    for j in range(1 ,0,-1):
        print(j,end=' ')
    print()
'''

#16
'''
n=int(input('number of rows:'))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()

'''
#18.i
'''
n=int(input('number of rows:'))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#17
'''
n=int(input('number of rows:'))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()
'''
#8.
'''
n=int(input('number of rows:'))
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print(n, end=" ")
    print()


'''
#10.
'''
n=int(input('number of rows'))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=" ")
        for k in range(1,i+1):
            print(n,end=" ")
        print()

'''
#12.
'''
n=int(input('number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n,end=" ")
    for k in range(1,i+i):
        print(' ' ,end=' ')
    for m in range(1,n-i+2):
            print(n,end=' ')
        
    print()

'''
#13
'''
1 1 1 1
2 2 2
3 3
4
n=int(input('number of rows:'))
for i in range(n):
    print(' '*(n-i)+(i+1)*(i+1))


    
    for j in range(1,n-i):
        print(' ',end='')
        for k in range(1,(i+1)*(i+1)):
            print(i,end=' ')
    print()
'''

        


#5.
lst=[10,12,13,14,16,80,90,45,67,87,45,100,1]
s=0
for i in lst:
    if i>s:
        s=i
        
        
    
print(s)
    
    














    
    





    

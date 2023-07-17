movies = {
    'actors':{
        'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
            'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
        'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
            'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
        'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},
            'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'50%'},
        'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
            'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
        'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2,
            'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
    },
    'actress':{
        'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},
            'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
            'sRate':'40%'},
        'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
            'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
            'sRate':'30%'},
        'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
            'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
            'sRate':'60%'},
        'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':5,
            'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
        'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
            'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
 }
}

#1.Writea program to display all actors name?
'''
for i in movies['actors']:
    print(i)
    '''
#2.Write a program to display all actress name?
'''
for i in movies['actress']:
    print(i)
'''
#3.whi is darling?
'''
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Darling':
        print(i)
'''
#4.What are the total number of Nandhi awards won by actors?
'''
sum=0
for i in movies['actors']:
    sum=sum+movies['actors'][i]['awards']['nandi']
    print(sum)
'''
#5 what is the name of prince?
'''
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
        print(i)
        '''
#6.What are the total number of awards won by Ram Charan?
'''
sum=0
for i in movies['actors']:
    if i=='ramcharan':
        sum=movies['actors'][i]['awards']['nandi']+movies['actors'][i]['awards']['cinemaa']+movies['actors'][i]['awards']['siima']
        print(sum)
'''
#7.which actor won more number of Nandi Awards?
'''
lst=[]
for i in movies['actors']:
    lst.append(movies['actors'][i]['awards']['nandi'])
for i in movies['actors']:
    if movies['actors'][i]['awards']['nandi']==max(lst):
        print(i)
'''
#8.what is the success rate of prince?
'''
for i in movies['actors']:
    if movies['actors'][i]['knownAs'] in'Prince':
        print(movies['actors'][i]['sRate'])
        '''
#9 which artist has more number of Hits?
'''
lst=[]
for i in movies:
     print(i)
     for j in movies[i]:
         print(j)
         lst.append(movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']+movies[i][j]['hits']['flops'])
print(lst)
for i in movies:
    for j in movies[i]:
        if max(lst)==movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']+movies[i][j]['hits']['flops']:
            print(j)
            '''
#10.who is milky beauty?
'''        
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Milky Beauty':
        print(i)         
    '''
 #11.what is the nick name of Rashmika?
'''
for i in movies['actress']:
    if 'rashmika' in i:
         print(movies['actress'][i]['knownAs'])
         '''
#12.What is the actress names who did not win at least one nandi award?
'''
lst=[]
for i in movies['actress']:
    print(i)
    if 'nandi' in movies['actress'][i]['awards']:
        lst.append(movies['actress'][i]['awards']['nandi'])
        print(lst)
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi']>1:
        print(i)
  '''
#13.what are the total number of Siima awards won by all artists?
'''
sum = 0
for i in movies['actors']:
    sum += (movies['actors'][i]['awards']['siima'])

for i in movies['actress']:
    sum += (movies['actress'][i]['awards']['siima'])
print(sum)
'''
#14.what is the aritist name who has more success rate?
'''
print([max([(movies['actors'][i]['sRate'], i) for i in movies['actors']] + [(movies['actress'][j]['sRate'], j) for j in movies['actress']])[1]])
  '''
#15.what is the age of actor who has more super hit movies?
'''
print([movies['actors'][i]['age'] for i in movies['actors'] if  movies['actors'][i]['hits']['super'] == max(movies['actors'][i]['hits']['super'] for i in movies['actors'])])
    
'''
#16.what is the actress name who married?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        print(i)
'''
#17.who is tallest actress?

'''
for i in movies['actress']:
    if i==movies['actress'][i]['height']:
        print(max(i))
'''
#18.who is youngest artist?
'''
print(min([(movies['actors'][i]['age'],i) for i in movies['actors']] + [(movies['actress'][i]['age'],i) for i in movies['actress']])[1])

'''
#19.who is unmarried actor?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']!='married':
        print(i)
'''
#20.which is smallest actor?
'''
print(min([(movies['actress'][i]['age'],i) for i in movies['actress']])[1])
'''
#21.what is the age of butter milky?
'''
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Milky Beauty':
              print(movies['actress'][i]['age'])
'''
#22.which actress has more flops?
'''
print(max([(movies['actress'][i]['hits']['flops'],i) for i in movies['actress']])[1])

'''
#23.what are the total number of flops of all of all actress?
'''
for i in movies['actress']:
    if i in movies['actress'][i]['hits']['flop']:
        print(sum(i))

    or

print(sum([movies['actress'][i]['hits']['flops'] for i in movies['actress']]))
'''
#24.what are the age of sam and kaj?
'''
for i in movies['actress']:
    if  movies['actress'][i]['knownAs'] == 'samantha' or movies['actress'][i]['knownAs'] =='kajal':
              print(movies['actress'][i]['age'])
              '''

'''
print([movies['actress'][i]['age'] for i in movies['actress'] if movies['actress'][i]['knownAs']=='Sam' or movies['actress'][i]['knownAs']=='Kaj'])
'''
#25.which actress own highest total number of awards?
'''
lst = []
for i in movies['actress']:
    lst.append(movies['actress'][i]['awards']['nandi'] + movies['actress'][i]['awards']['cinemaa'] + movies['actress'][i]['awards']['siima'])
print(max(lst))

for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi'] + movies['actress'][i]['awards']['cinemaa'] + movies['actress'][i]['awards']['siima'] == max(lst):
        print(i)
'''
#26.who is tallest artist?
'''
print([i for i in movies['actress'] if movies['actress'][i]['age'] == min(movies['actress'][i]['age'] for i in movies['actress'])])

'''
#27.what are the total number of industry hits of who has more success rate?
'''
print(max([(movies['actors'][i]['age'],i) for i in movies['actors'] if movies['actors'][i]['mStatus'] == 'single'])[1])
   '''
#28.what is success rate of youngest actress?
'''
print([movies['actress'][i]['sRate'] for i in movies['actress']if movies['actress'][i]['age'] == min(movies['actress'][i]['age'] for i in movies['actress'])])
'''
#29.who is youngest married actress?
'''
print([i for i in movies['actress'] if movies['actress'][i]['age'] == min(movies['actress'][i]['age'] for i in movies['actress'])])
'''
#30.who is oldest unmarried actor?
'''
for i in movies['actors']:
    if movies['actors'][i]['mStatus']=='single':
        print(i)
        '''
#31.who are the high successful actor and actress?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
print(lst)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(lst):
            print(j)
            '''
#32.Totally how many unmarried artists are acting in movies?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']=='single':
            print(j)

   '''
#33.Which actress is having more industry hit movies?
'''
st = []
for i in movies['actress']:
     st.append(movies['actress'][i]['hits']['industry'])



for i in movies['actress']:
     if max(st)==movies['actress'][i]['hits']['industry']:
         print(i)
'''
#34.which actress does not have atleast one industry hit also?
'''
st=[]
for i in movies['actress']:
    st.append(movies['actress'][i]['hits']['industry'])
print(st)
for i in movies['actress']:
    if min(st)==movies['actress'][i]['hits']['industry']:
        print(i)

'''
#35.what are total number of industry and super hits of tallest actress?
'''
st=[]
s=0
for i in movies['actress']:
    st.append(movies['actress'][i]['height'])
print(st)
for i in movies['actress']:
      if max(st)==movies['actress'][i]['height']:
          s=s+(movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super'])
print(s)
'''
#36.which actress is having lengthiest nick name?
'''
st=[]
for i in movies['actress']:
    st.append(len(movies['actress'][i]['knownAs']))
print(st)
for i in movies['actress']:
    if max(st)==len(movies['actress'][i]['knownAs']):
        print(i)
'''
#37.who are the youngest unmaried artist?
'''
st=[]
for i in movies['actress']:
    st.append(movies['actress'][i]['age'])
print(st)
for i in movies['actress']:
    if min(st)==movies['actress'][i]['age']:
        print(i)

'''
#38.what are the total number of industry hits and super hitsof actress who got more siima awards?

'''
st=[]
for i in movies['actress']:
    st.append(movies['actress'][i]['awards']['siima'])
for i in movies['actress']:
    if max(st)==movies['actress'][i]['awards']['siima']:
        print(movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super'],i)
'''
#39.what are the ages of Darling and milky Beauty?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Darling' :
            print(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Milky Beauty':
            print(movies[i][j]['age'])
            
'''
#40.What are names of actors whose nickname contain star?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs'].endswith('Star')==True:
            print(j)

'''

#41.what is the total remuneration of all actor?
'''
lst=[]
s=0
for i in movies['actors']:
    lst.append(movies['actors'][i]['remuneration'])
    s=s+movies['actors'][i]['remuneration']
print(s)
'''
#43.What is the highest remuneration of an unmarried actress?
'''
lst=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='single':
        lst.append(movies['actress'][i]['remuneration'])
print(lst)
for i in movies['actress']:
    if  max(lst)==movies['actress'][i]['remuneration']:
        print(i)
'''
#44.what is the names of artists who has more remuneration?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['remuneration'])
print(lst)
for i in movies:
    for j in movies[i]:
        if max(lst)==movies[i][j]['remuneration']:
            print(j)

'''
#45.what is the remuneration of high successful Actress?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['sRate'])
print(lst)


for i in movies['actress']:
    if max(lst)==movies['actress'][i]['sRate']:
        print(movies['actress'][i]['remuneration'])
    
'''
#46.what is the remuneration of acress who has more industry hits?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['hits']['industry'])
print(lst)
for i in movies['actress']:
    if max(lst)==movies['actress'][i]['hits']['industry']:
        print(movies['actress'][i]['remuneration'])
'''
#47.what are the ages of an actors whose remuneration is more then 90 croes?
'''
for i in movies['actors']:
    if movies['actors'][i]['remuneration']>90:
        print(movies['actors'][i]['age'])
   '''
#48.what are the total number of industry hits of both prince and Butter Milky Beauty?
'''
lst=[] 
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Prince' or movies[i][j]['knownAs']=='Butter Milky Beauty':
            lst.append(movies[i][j]['hits']['industry'])
print(sum(lst))
'''
#49.What is the age of Laughing Queen?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Laughing Queen':
         print(movies[i][j]['age'])
         '''
#50.what are the total number of awards won by an actor who has less successful rate?
'''
lst=[]
s=0
for i in movies['actors']:
      lst.append( movies['actors'][i]['sRate'])
print(lst)
for i in movies['actors']:
    if max(lst)==movies['actors'][i]['sRate']:
        print(movies['actors'][i]['awards']['nandi']+movies['actors'][i]['awards']['cinemaa']+movies['actors'][i]['awards']['siima'])
        
   '''         








    

    

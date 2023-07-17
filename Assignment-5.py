players = {
 'player1':{'name':'Sachin', 'matches':{'test':200,'odi':463},'scores':{'test':248,'odi':200},
 'wickets':{'test':46, 'odi':154}, 'age':49, 'shirt':10, 'role':'top-order','location':'Bombay'},
 
 'player2':{'name':'Kohli', 'matches':{'test':102, 'odi':262}, 'scores':{'test':254, 'odi':183},
 'wickets':{'test':0, 'odi':4}, 'age':33, 'shirt':18, 'role':'top-order','location':'Delhi'},
 
 'player3':{'name':'Rohit', 'matches':{'test':44, 'odi':231}, 'scores':{'test':212, 'odi':264}, 
 'wickets':{'test':2, 'odi':8}, 'age':35, 'shirt':45, 'role':'opening','location':'Nagpur'},
 
 'player4':{'name':'Sehwag','matches':{'test':104,'odi':251}, 'scores':{'test':319, 'odi':219},
 'wickets':{'test':40, 'odi':96}, 'age':43, 'shirt':44, 'role':'opening', 'location':'Delhi'},
 
 'player5':{'name':'Zaheer Khan', 'matches':{'test':92, 'odi':200}, 'scores':{'test':75, 'odi':34},
 'wickets':{'test':311, 'odi':282}, 'age':43, 'shirt':41, 'role':'Bowler','location':'Bombay'},

 'player6':{'name':'Dhoni', 'matches':{'test':90, 'odi':350}, 'scores':{'test':224, 'odi':183},
 'wickets':{'test':0, 'odi':1}, 'age':41,'shirt':7, 'role':'keeper','location':'Ranchi'}
 }
#1.Write a program to display all players names?
'''
for i in players:
      print(players[i]['name'])
'''
#2. Write a program to display ages of players?
'''
for i in players:
    print(players[i]['age'])
'''

#3. Write a program to display the youngest player name?
'''
newlst=[]
for i in players:
     newlst.append(players[i]['age'])
print(newlst)
for i in players:
    if  min(newlst)==players[i]['age']:
        print(players[i]['name'])
  '''      



#4. Write a program to display player name who played more test matches?
'''
newlst=[]
for i in players:
      newlst.append( players[i]['matches']['test']+players[i]['matches']['odi'])
print(newlst)

for i in players:
    if max(newlst)==players[i]['matches']['test']+players[i]['matches']['odi']:
        print(players[i]['name'])
   '''  





#5. Write a program to display player name and number of test matches who has taken 0 wickets in test matches? 
'''
newlst=[]
for i in players:
    newlst.append(players[i]['wickets']['test'])
print(newlst)

for i in players:
    if min(newlst)==players[i]['wickets']['test']:
        print(players[i]['name'])

        #or 
for i in players:
    if min(newlst)==players[i]['wickets']['test']:
        print(players[i]['name'])
'''
        


#6. Write a program to display player name who has taken more wickets in ODI?
'''
newlst=[]
for i in players:
    newlst.append(players[i]['wickets']['odi'])
print(newlst)
for i in players:
    if max(newlst)==players[i]['wickets']['odi']:
        print(players[i]['name'])
'''


#7. Write a program to display the players’ names that played highest number of ODI matches?
'''
newlst=[]
for i in players:
    newlst.append(players[i]['matches']['odi'])
print(newlst)
for i in players:
    if max(newlst)==players[i]['matches']['odi']:
        print(players[i]['name'])
   ''' 


#8. Write a program to display the player name that has highest total score of both test and ODIs?
'''
newlst=[]
for i in players:
    newlst.append(players[i]['wickets']['test']+players[i]['wickets']['odi'])
print(newlst)
for i in players:
    if max(newlst)==players[i]['wickets']['test']+players[i]['wickets']['odi']:
        print(players[i]['name'])
'''


#9. Write a program to display total number of matches of Kohli?

'''newlst=[]
for i in players:
    if players[i]['name']=='Kohli':
        newlst.append(players[i]['matches']['test']+players[i]['matches']['odi'])
print(newlst)
   ''' 
#10. Write a program to display the age of Rohit?
'''
for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['age'])
'''


#11. Write a program to display the total ODI scores of all players?
'''
newlst=[]
for i in players:
    newlst.append(players[i]['scores']['odi'])
print(newlst)
print(sum(newlst))
'''


#12. Write a program to display total number of wickets of Zaheer Khan?

'''
newlst=[]
for i in players:
    if players[i]['name']=='Zaheer Khan':
        newlst.append(players[i]['wickets']['test']+players[i]['wickets']['odi'])
print(newlst)
print(sum(newlst))

'''



#13. Write a program to display all opening batsman names?
'''
for i in players:
    if players[i]['role']=='opening':
        print(players[i]['name'])
    
'''


#14. Write a program to display player name that shirt number is highest number?
'''
newlst=[]
for i in players:
     newlst.append(players[i]['shirt'])
print(newlst)
for i in players:
    if max(newlst)==players[i]['shirt']:
        print(players[i]['name'])
'''


#15. Write a program to display all Bombay players?
'''
for i in players:
      if players[i]['location']=='Bombay':
          print(players[i]['name'])
   '''     




#16. Write a program to display the shirt number of Sachin?
'''
for i in players:
   if players[i]['name']=='Sachin':
       print(players[i]['shirt'])
   ''' 



#17. Write a program to display the role of Rohit in match?
'''
for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['role'])
'''



#18. What is the location of the player whose shirt number is 45?
'''
for i in players:
     if players[i]['shirt']==45:
         print(players[i]['location'])
'''


#19. Write a program to display all wickets of a player whose role is bowler?

'''newlst=[]
for i in players:
    if players[i]['role']=='Bowler':
       newlst.append(players[i]['wickets']['test']+players[i]['wickets']['odi'])
print(newlst)
print(sum(newlst))

'''
#20. Write a program to count total number opening players?
'''
count=0
for i in players:
    if players[i]['role']=='opening':
        count=count+1
print(count)
'''
#21. Write a program to display Bombay opening player name?
'''
for i in players:
    if players[i]['location']=='Bombay' and players[i]['role']=='opening':
        print(players[i]['name'])
    else:
        print('no one is their')
   '''     




#22. Write a program to display the roles of Delhi players?
'''
for  i in players:
    if players[i]['location']=='Delhi':
        print(players[i]['role'])
'''



#23. Write a program to display the role and location of Rohit?
'''
for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['role'],players[i]['location'])
'''



#24. Write a program to display total score of Bombay top-order player?
'''
newlst=[]
for i in players:
    if players[i]['location']=='Bombay' and players[i]['role']=='top-order':
        newlst.append(players[i]['scores']['test']+players[i]['scores']['odi'])
print(newlst)
print(sum(newlst))
   '''     
#25. Write a program to display all unique roles of players?
'''
newlst=[]
for i in players:
       newlst.append(players[i]['role'])
print(set(newlst))
'''
#26 Write a program to display shirt number of Delhi top-order player?
'''
for i in players:
    if players[i]['location']=='Delhi' and players[i]['role']=='top-order':
        print(players[i]['shirt'])
'''
#27. Write a program to display keeper name?
'''
for i in players:
    if players[i]['role']=='keeper':
        print(players[i]['name'])
'''
#28. Write a program to display the shirt number of Dhoni?
'''
for i in players:
    if players[i]['name']=='Dhoni':
        print(players[i]['shirt'])
'''
#29. Write a program to display players names who played less than 100 test matches?
'''
for i in players:
    if players[i]['matches']['test']<100:
        print(players[i]['name'])
'''


#30. Write a program to display total wickets of Ranchi player?
'''
for i in players:
    if players[i]['location']=='Ranchi':
        print(players[i]['wickets']['test']+players[i]['wickets']['odi'])
'''


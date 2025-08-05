x = int(input("Please enter an integer:"))
if x < 0:
     x = 0
     print("Negative changed to zero")
elif x == 0:
     print("Zero")
elif x == 50:
     print("Fifty")
else:
     print("More")
     
     
#For statements
words = ['Cat', 'window', 'defenestrate']
for i in words:
     print(i, len(i))
     
     #Set of key value pairs
users = {'Hans':'Active',
         'Eleonore': 'inactive',
         'kjjjqcq': 'active'}
for user, status in list(users.item()):
     if status == 'inactive':
          del users[user]
          
#stratergy
#active_users = {}
active_users = {user: status for user, 
                status in users.items() 
                if status == 'active'}

print(active_users)
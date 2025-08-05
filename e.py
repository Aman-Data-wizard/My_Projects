from enum import Enum
class color(Enum):
     RED = 'red'
     GREEN = 'green'
     BLUE = 'blue'
     
color = color(input('Enter the color of your choice:'))

match color:
     case color.RED:
           print('You have chosen red')
     case color.GREEN:
               print('Seen green')
     case color.BLUE:
               print('i feel blue :( today')
     
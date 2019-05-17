#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random
import gc
import weakref

'''
this is  a monopoly script written in python 3. 
'''


class Property:
    
    instances = []
    def __init__(self, object_name,board_position, property_name, property_cost, property_color, property_mortgage_value, property_rent):
        self.__class__.instances.append(weakref.proxy(self))
        self.object_name = object_name
        self.property_name = property_name
        self.board_position = board_position
        self.property_cost = property_cost
        self.property_color = property_color
        self.property_mortgage_value = property_mortgage_value
        self.property_rent = property_rent
        
    def property_with_houses(self, cost_of_house, cost_of_hotel,  rent_with_hotel, rent_with_1house, rent_with_2house, rent_with_3house, rent_with_4house):
        self.cost_of_house = cost_of_house
        self.cost_of_hotel = cost_of_hotel
        self.rent_with_hotel = rent_with_hotel
        self.rent_with_1house = rent_with_1house
        self.rent_with_2house = rent_with_2house
        self.rent_with_3house = rent_with_3house
        self.rent_with_4house = rent_with_4house
 



class Stations:
    instances = []
    def __init__(self, object_name,board_position,property_name, cost, rent):
        self.__class__.instances.append(weakref.proxy(self))
        self.property_name = property_name
        self.board_position = board_position
        self.cost = cost
        self.rent = rent
        
class Utilities:
    
    instances = []
    def __init__(self, object_name,board_position, property_name, cost):
        self.__class__.instances.append(weakref.proxy(self))
        self.property_name = property_name
        self.board_position = board_position
        self.cost = cost
        
class Chance_card:
    def __init__ (self, card_number, content, effect):
        self.content = content
        self.effect = effect
        self.card_number = card_number
        
class Community_chest:
    def __init__ (self, card_number, content, effect):
        self.content = content
        self.effect = effect
        self.card_number = card_number
        
class Player:
    def __init__(self, name, balance = 1500):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return self.name
        
    def debit(self, amount):
        if amount >  self.balance:
            self.balance = 'bankrupt!'
            return self.balance
            
        else:
            self.balance = self.balance - amount 
            return self.balance
                

        


'''
in this board list, i appended all the board postions on a monoploy board. 
i used the '.board_postion' attributes to represent the numbers which range from (1-39)
'''    
board = [brown1.board_position, brown2.board_position, blue1.board_position, blue2.board_position,blue3.board_position,pink1.board_position, 
pink2.board_position,pink3.board_position,orange1.board_position,orange2.board_position,orange3.board_position,red1.board_position,red2.board_position,red3.board_position,yellow1.board_position ,yellow2.board_position,yellow3.board_position ,green1.board_position ,green2.board_position,green3.board_position,purple1.board_position,purple2.board_position, station1.board_position, station2.board_position, station3.board_position, station4.board_position, utility1.board_position, utility2.board_position]        

player_position_1 =[]  

'''
i created the player_postiton_1 list to collect the return from the roll dice function. 
the sum of this list at any given time reflects what position the player is on the 
board. 
'''

def roll_dice():
    
    dice1 = [1,2,3,4,5,6]
    dice2 = [1,2,3,4,5,6]
    d1 = random.choice(dice1)
    d2 = random.choice(dice2)
    player_position_1.append(d1)
    player_position_1.append(d2)
    
    if d1 == d2:
        new_d1 = random.choice(dice1)
        new_d2 = random.choice(dice2)
        print(new_d1, new_d2)
    
    
    return d1, d2

def add_dice():
    return sum(player_position_1)    
    
def check_if_players_pass_go():
    if sum(player_position_1) > 41:
        print('yes')
        player_position_1.clear()    


'''
to know the exact property the player is on ant any given time, i created the board_num_expression = {}
it is an empty dictionary that i would update using the for loop below. 
the for loop grabs all the numbers in the board list i created above. 
it casts each of the numbers as strings and assigns them as keys with 
the values of the object of the property class. each key which is in essence
the board numerical representation will now have all the attributes of the board properties. 
'''        
        
        
board_num_expression = {}
for n in board:
    board_num_expression.update({str(n): n})
    
'''
after the loop above runs the disctionary will look something like
'board_num_expression = {'1': 1, .......}'. n i then update this dictionary
with the lines of code below where for instance key '1' which had the value of 1, 
will now have the value of the property class of which 'brown1' is the first object. 
'''


board_num_expression['1'] = Property('brown1',1,'Old kent road', 60, 'brown', 30, 2)
board_num_expression['3'] = Property('brown2',3,'White chapel road', 60, 'brown', 30, 4)
board_num_expression['6'] = Property('blue1',6,'Angel islington', 100, 'blue', 50, 6)
board_num_expression['8'] = Property('blue2',8,'Euston road', 100, 'blue', 50, 6)
board_num_expression['9'] = Property('blue3',9,'Pentonville', 120, 'blue', 60, 8)
board_num_expression['11'] = Property('pink1',11,'Pall mall', 140, 'pink', 70, 10)
board_num_expression['13'] = Property('pink2',13,'Whitehall', 140, 'pink', 70, 10)
board_num_expression['14'] = Property('pink3',14,'Northumberland Avenue', 160, 'pink', 80, 12)
board_num_expression['16'] = Property('orange1',16, 'Bow Street', 180, 'orange', 90, 14)
board_num_expression['18'] = Property('orange2',18, 'Marlborough Street', 180, 'orange', 90, 14)
board_num_expression['19'] = Property('orange3',19, 'Vine Street', 200, 'orange', 100, 16)
board_num_expression['21'] = Property('red1',21, 'The Strand', 220, 'red', 110, 18)
board_num_expression['23'] = Property('red2',23, 'Fleet Street', 220, 'red', 110, 18)
board_num_expression['24'] = Property('red3',24,'Trafalgar Square', 240, 'red', 120, 20)
board_num_expression['26'] = Property('yellow1',26,'Leicester Square', 260, 'yellow', 130, 22)
board_num_expression['27'] = Property('yellow2',27,'coventry street', 260, 'yellow', 130, 22)
board_num_expression['29'] = Property('yellow3',29,'Piccadily', 280, 'yellow', 140, 24)
board_num_expression['31'] = Property('green1',31,'Regent Street', 300, 'green', 150, 26)
board_num_expression['32'] = Property('green2',32,'Oxford Street', 300, 'green', 150, 26)
board_num_expression['34'] = Property('green3',34,'Bond Street', 320, 'green', 160, 28)
board_num_expression['37'] = Property('purple1',37,'Park Lane', 350, 'purple', 175, 35)
board_num_expression['39'] = Property('purple1',39,'Mayfair', 400, 'purple', 200, 50)

board_num_expression['5'] = Stations('station1',5,"King's Cross Station",200, 25)
board_num_expression['15'] = Stations('station2',15,"Marylebone Station",200, 25)
board_num_expression['25'] = Stations('station3',25,"Fenchurch St Station",200, 25)
board_num_expression['35'] = Stations('station4',35,"Liverpool Street Station",200, 25)

board_num_expression['12'] = Utilities('utility1',12,'Electric Company', 150)
board_num_expression['28'] = Utilities('utility2',28,'Water Works', 150)

def board_properties():
    '''
    this functions prints the properties on th emonopoly board. 
    i create a board_garb [] list. i use a for loop to get the keys 
    in the board_num_expression disctionary. i then create another for loop that 
    goes through the items in the list which are the keys in board_num_expressions
    . it then prints the key which is an obeject of the property class together with 
    the 'property name' method. 
    
    '''
    
    board_garb = []
    for n in board_num_expression.keys():
        board_garb.append(n)
    for n in board_garb:
        print(board_num_expression[n].property_name)

def board_position_check(list_):
    '''
    this functions simply checks where the player is 
    on th eboard. it does this by summing up the total number of throws of a player 
    . the result is what i saved in the player_postion list in the roll dice function. 
    when it sums up this number, it strings the sum and checks if the stringed
    sum is  akey in the board_num_expression dictinoary.  if the key exists, 
    it calls the board_num_expression['the key is here'] with the property name method. 
    '''
    
    if str(sum(list_)) in board_num_expression.keys():
        print('Player is on',board_num_expression[str(sum(list_))].property_name)
        
    
    
    
    
    
    
    
    
    


# In[27]:


roll_dice()


# In[28]:


player_position_1


# In[29]:


board_position_check(player_position_1)


# In[26]:


board_check()


# In[15]:


board


# In[14]:


board_num_expression


# In[18]:


for n in board:
    print(n.property_name)


# In[ ]:





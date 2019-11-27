import random
import gc
import weakref

'''
The locations on the standard British version of the board game Monopoly set in London are simulated in this program. 
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
                
player1 = Player('tony')       
 
brown1 = Property('brown1',1,'Old kent road', 60, 'brown', 30, 2)
brown2 = Property('brown2',3,'White chapel road', 60, 'brown', 30, 4)
blue1 = Property('blue1',6,'Angel islington', 100, 'blue', 50, 6)
blue2 = Property('blue2',8,'Euston road', 100, 'blue', 50, 6)
blue3 = Property('blue3',9,'Pentonville', 120, 'blue', 60, 8)
pink1 = Property('pink1',11,'Pall mall', 140, 'pink', 70, 10)
pink2 = Property('pink2',13,'Whitehall', 140, 'pink', 70, 10)
pink3 = Property('pink3',14,'Northumberland Avenue', 160, 'pink', 80, 12)
orange1 = Property('orange1',16, 'Bow Street', 180, 'orange', 90, 14)
orange2 = Property('orange2',18, 'Marlborough Street', 180, 'orange', 90, 14)
orange3 = Property('orange3',19, 'Vine Street', 200, 'orange', 100, 16)
red1 = Property('red1',21, 'The Strand', 220, 'red', 110, 18)
red2 = Property('red2',23, 'Fleet Street', 220, 'red', 110, 18)
red3 = Property('red3',24,'Trafalgar Square', 240, 'red', 120, 20)
yellow1 = Property('yellow1',26,'Leicester Square', 260, 'yellow', 130, 22)
yellow2 = Property('yellow2',27,'coventry street', 260, 'yellow', 130, 22)
yellow3 = Property('yellow3',29,'Piccadily', 280, 'yellow', 140, 24)
green1 = Property('green1',31,'Regent Street', 300, 'green', 150, 26)
green2 = Property('green2',32,'Oxford Street', 300, 'green', 150, 26)
green3 = Property('green3',34,'Bond Street', 320, 'green', 160, 28)
purple1 = Property('purple1',37,'Park Lane', 350, 'purple', 175, 35)
purple2 = Property('purple1',39,'Mayfair', 400, 'purple', 200, 50)

station1 = Stations('station1',5,"King's Cross Station",200, 25)
station2 = Stations('station2',15,"Marylebone Station",200, 25)
station3 = Stations('station3',25,"Fenchurch St Station",200, 25)
station4 = Stations('station4',35,"Liverpool Street Station",200, 25)

utility1 = Utilities('utility1',12,'Electric Company', 150)
utility2 = Utilities('utility2',28,'Water Works', 150)

brown1.property_with_houses(30, 150, 250, 10, 30, 90, 160)
brown2.property_with_houses(30, 150, 450, 20, 60, 180, 360)
blue1.property_with_houses(50, 250, 550, 30, 90, 270, 400)
blue2.property_with_houses(50, 250, 550, 30, 90, 270, 400)
blue3.property_with_houses(50, 250, 600, 40, 100, 300, 450)
pink1.property_with_houses(100, 500, 750, 50, 150, 450, 625) 
pink2.property_with_houses(100, 500, 750, 50, 150, 450, 625) 
pink3.property_with_houses(100, 500, 900, 60, 180, 500, 700) 
orange1.property_with_houses(100, 500, 950, 70, 200, 550, 750)
orange2.property_with_houses(100, 500, 950, 70, 200, 550, 750)
orange3.property_with_houses(100, 500, 1000, 80, 220, 600, 800)
red1.property_with_houses(150, 750, 1050, 90, 250, 700, 875)
red2.property_with_houses(150, 750, 1050, 90, 250, 700, 875)
red3.property_with_houses(150, 750, 1100, 100, 300, 750, 925)
yellow1.property_with_houses(150, 750, 1150, 110, 330, 800, 975) 
yellow2.property_with_houses(150, 750, 1150, 110, 330, 800, 975)
yellow3.property_with_houses(150, 750, 1200, 120, 360, 850, 1025) 
green1.property_with_houses(160, 800, 1275, 130, 390, 900, 1100) 
green2.property_with_houses(160, 800, 1275, 130, 390, 900, 1100)
green3.property_with_houses(160, 800, 1400, 150, 450, 1000, 1200) 
purple1.property_with_houses(200, 1000, 1500, 175, 500, 1100, 1300)
purple2.property_with_houses(200, 1000, 2000, 200, 600, 1400, 1700) 

board = [brown1.board_position, brown2.board_position, blue1.board_position, blue2.board_position,blue3.board_position,pink1.board_position, 
pink2.board_position,pink3.board_position,orange1.board_position,orange2.board_position,orange3.board_position,red1.board_position,red2.board_position,red3.board_position,yellow1.board_position ,yellow2.board_position,yellow3.board_position ,green1.board_position ,green2.board_position,green3.board_position,purple1.board_position,purple2.board_position, station1.board_position, station2.board_position, station3.board_position, station4.board_position, utility1.board_position, utility2.board_position]        

player_position_1 =[]

def roll_dice():
    
    dice1 = [1,2,3,4,5,6]
    dice2 = [1,2,3,4,5,6]
    d1 = random.choice(dice1)
    d2 = random.choice(dice2)
    player_position_1.append(d1)
    player_position_1.append(d2)
    
    #if d1 == d2:
        #new_d1 = random.choice(dice1)
        #new_d2 = random.choice(dice2)
        #print(new_d1, new_d2)
    
    
    print(d1, d2)
    
if sum(player_position_1) > 40:
    player_position_1 = [sum(player_position_1 ) - 40]


def add_dice():
    return sum(player_position_1)    
    
def check_if_players_pass_go():
    if sum(player_position_1) > 41:
        print('yes')

board_num_expression = {}
for n in board:
    board_num_expression.update({str(n): n})

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

player_property_list = []

def board_check():
    board_garb = []
    for n in board_num_expression.keys():
        board_garb.append(n)
    for n in board_garb:
        print(board_num_expression[n].property_name)

def board_position_check(list_):
    
    if str(sum(list_)) in board_num_expression.keys():
        print('Player is on',board_num_expression[str(sum(list_))].property_name)
       
    '''
        if board_num_expression[str(sum(list_))].property_name not in player_property_list:
            #player_property_list.append(board_num_expression[str(sum(list_))])
        else:
            pass
    if sum(list_) > 40:
        list_ = [sum(list_) - 40]
        return list_
        if str(sum(list_)) in board_num_expression.keys():
            print('Player is on',board_num_expression[str(sum(list_))].property_name)
        
    '''
player_position_1 =[]
player_property_list = []
def property_assignemnt(list_):
    if str(sum(list_)) in board_num_expression.keys():
        if board_num_expression[str(sum(list_))] not in player_property_list:
            #print(board_num_expression[str(sum(list_))].property_name,'not in player_property_list')
            while True:
                player_choice = input(f" would you like to buy {board_num_expression[str(sum(list_))].property_name}? \n ")
                player_choice = player_choice.lower()
                if player_choice.startswith('y'):
                    player_property_list.append(board_num_expression[str(sum(list_))].property_name)
                    break
                elif player_choice.startswith('n'):
                    break
                else:
                    continue
    else:
        pass
    
roll_dice()
add_dice()
board_position_check(player_position_1)
property_assignemnt(player_position_1)
print(player_property_list)   

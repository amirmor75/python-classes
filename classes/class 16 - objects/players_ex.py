# כּימוּס הוא מאפיין חשוב בתכנות ובמיוחד בתכנות מונחה-עצמים המתייחס לאריזה של
# מידע עם הפעולות שפועלות על המידע הזה כיחידה אחת. כימוס מאפשר יצירת יחידת תוכנה בעלת
# ממשק מוגדר לשאר חלקי התוכנה

class Player():
    __name = None         # תכונה / attribute
    __health = 100
    __attack_power = 15
    __sheild = 5
    __password = 'aliidjfvbnr'
    
    def __init__(self, name, health=100,attack=15, sheild=5, ):
        self.name = name
        self.health = health
        self.attack_power = attack
        self.sheild = sheild

    def fight(self, other_player):  
        to_reduce_self  = (other_player.attack_power - self.sheild) if other_player.attack_power - self.sheild > 0  else 0
        self.health =  self.health - to_reduce_self
        to_reduce_other = (self.attack_power - other_player.sheild) if self.attack_power - other_player.sheild > 0  else 0
        other_player.health = other_player.health - to_reduce_other
    def print_health(self):
        print(self.health)
        
    def next_turn(self):
        self.health += 3
        


class Board():
    __tiles = 64
    __turns = 0
    
    def next_turn(self, players_lst):
        for p in players_lst:
            p.next_turn() #p.health -= 3
        
        
        
        
if __name__ == '__main__':
    Amir = Player() # Player(name = 'Amir Mor', email = 'A@gmail.com')             # פעולה בונה/ Constructor
    Amir.health = 70
    Ilay = Player(name = 'Amir Mor', email = 'I@gmail.com', sheild=7)   # פעולה בונה/ Constructor
    Amir.fight(Ilay)
    Amir.print_health()
    Ilay.print_health()
    Amir.fight(Ilay)
    Amir.print_health()
    Ilay.print_health()
    
    
    
    

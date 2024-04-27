#  הגדר מחלקת פסיכולוג, פיזיותרפיסט וקומיקאי.
# לכל אחד מהם יש עלות מתן שירות, רמת אושר, כמות כסף ,כמות אנרגיה ורמת חברותיות, אשר חסויים לשאר החברה.
# .כאשר לקוח מסויים צורך שירות, הוא משלם מכספו את כמות הכסף הנדרשת לבעל המקצוע,
# האושר שלו עולה בהתאם וכמות האנרגיה שלו עולה או יורדת בהתאם לשירות.  
# הגדר את האובייקטים המתאימים, ואת הפונקציות שלהם של צריכת שירות ומתן שירות. 
# הגדר לכל אובייקט פונקציה של שינה בלילה שמעלה לו את רמת האנרגיה.
# הגדר פגישה חברתית בין שני אובייקטים חברים שמעלה לשניהם את רמת האנרגיה בהתאם לרמת החברתיות של כל אובייקט


class worker ():
    def __init__(self,cost,happines,wallet,energy,friendly):
        self.__cost = cost
        self.__happines = happines
        self.__wallet = wallet
        self.__energy = energy
        self. __friendly = friendly
        
    def giving_service (self,cust):
        self._Wallet + self._cost
        self.__Energy - 13
        self.__Friendly - 1
        self.__Happines + 3
        return 
    
class Psy(worker):
    therapy_method = 'dynamic'
    
    def __init__(self,cost,happines,wallet,energy,friendly,therapy_method):
        worker.__init__(cost,happines,wallet,energy,friendly)
        self.therapy_method = therapy_method


# class Comic():
#     humor_type='black'
#     # x,y,z,t = 0,0,0,0
#     pass
# class Physioth():
#     sport_team = None
#     # x,y,z,t = 0,0,0,0
#     pass


    
    
     




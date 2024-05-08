class Song:
        
    class_variable1 = 7     # class variable
    
    def __init__(self,song_id,name , performer, lyrics, composer, genre, price, discount = 0 , order = 0 ):
        self.song_id = song_id      # instance variable
        self.name = name                # instance variable
        self.performer = performer      # instance variable
        self.lyrics =lyrics             # instance variable
        self.composer=composer          # instance variable
        self.genre = genre              # instance variable
        self.price = price
        self.discount = discount
        self.order = order
        
    def get_song_id(self): # getter for number 
        return self.song_id
    
    def get_name(self):     # getter for name 
        return self.name
    
    def get_performer(self):    # getter
        return self.performer
    
    def get_price(self):    # getter
        return self.price
    
    def get_discount(self):    # getter
        return self.discount
    
    def setter_name(self, name):    # setter
        self.name = name
    
    
    def set_discount(self, num):
        if num > 0 and num < 0.99:
            self.discount = num 
            return True
        return False
    def purchase(self):
        self.order += 1 
    
def purchase_song(song_lst, song_id):
    for song in song_lst:
        if song.get_song_id() == song_id:
            song.purchase()
            return (True, song.get_price() - song.get_discount() )
    return (False,0)

            
        
        
if __name__ == '__main__':
    song_id = 'SA23456'
    song_name = 'Photograph'
    performer = ('Ed Sheeran')
    lyrics = ('Ed Sheeran', 'Johnny McDaid', 'Martin Harrington', 'Tom Leonard')
    composers = ('Ed Sheeran', 'Johnny McDaid', 'Martin Harrington', 'Tom Leonard')
    genre = 'Folk-pop'
    price = 0.99
    s1 = Song(song_id, song_name, performer, lyrics, composers, genre, price)
    s2 = Song('SA1', 'soul', performer, lyrics, composers, genre, price)
    print(s1.get_number_id())
    print(s2.get_number_id())
    print(s1.class_variable1)
    print(s2.class_variable1)
    
    s1.name = 'nonono'
    print(s1.name)
    print(s2.name)

    Song.class_variable1 = 10
    print(s1.class_variable1)
    print(s2.class_variable1)
    
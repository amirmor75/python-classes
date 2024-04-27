class Door:
    height = 2.1
    width = 1.2
    material = None
    
    def __init__(self):
        self.height = 2.
    
    # def __init__(self, height, width):
    #     self.height = height
    #     self.width = width
    



if __name__ == '__main__':

    d1 = Door()
    # d1.height = 7
    Door.height = 1
    d2 = Door()   
    
    
    print(d1.height)
    print(d2.height)
    
    
    
# מחלקה

class Cube():
    height = 10   # attribute - תכונה
    width = 10    # attribute - תכונה
    depth = 10    # attribute - תכונה
    __smoothness = 10
    
    
        
        
    def base_S(self):
        return self.depth * self.width  
    def beauty(self):
        beauty = self.base_S() * self.height * self.__smoothness
        if beauty > 500 : 
            return 'very much'
        else:
            return 'it\'s okay you know'
        
if __name__ == '__main__':
    
    c1 = Cube()  # יצירת מופע של האובייקט 
    c2 = Cube()
    
    c1.depth = 100
    Cube.depth=2
   
    
    print('c1: '+ str(c1.depth))  
    print('c2: '+str(c2.depth))
    print('Cube : '+str(Cube.depth)) 
    
    # print(cube1.depth)
    # print(cube1.base_S())
    # print(cube1.beauty())
    # # print(cube2.depth)
        
    

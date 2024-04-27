# int,float,string,boolean
print(  type(21)      )
print(  type(21.234)  )
print(  type("21")    )
print(  type(True)    )

# אם אנחנו רוצים לעבור מסיבה כזו או אחרת למשפחה שונה ממה שאנחנו עכשיו 
# ניתן לעשות זאת ע"י המרה גלויה explicit casting
x=21
print( "x is of type:" , type(x)    )
x = str(x)
print( "x after casting is of type:" , type(x) )
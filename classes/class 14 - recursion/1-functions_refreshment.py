
# argumnets 
# return values
# after the return statment, you cannot write more code in the function, it 'returns'

def func():
    print('i start doing something')
    x = str(input())
    val = x.split(' ')
    return val[0]
    c = int(input())
    print(c*8) 




if __name__ == '__main__':
    x = func()
    print(x)
    



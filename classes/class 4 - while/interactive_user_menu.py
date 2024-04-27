import libs


def main():
    print('\n\nwelcom to Ilay and Amir\'s interactive menu' )
        
    while True:
        print('\n\nchoose an option that seems nice to you:')
        print('1. count the number of chars in the given string')
        print('2. coin toss (heads/tails)')
        print('3. random number generator')
        print('type \'quit\' to quit our menu :(')
        # print('')
        option = input('you\'re choice:\n')
        if option=='1':
            libs.chars_counter()
        if option=='quit':
            break
    print('bye bye!!!!!!')
        
        
        
if __name__ == '__main__':
    main()

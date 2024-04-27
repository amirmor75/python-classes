# write a function that sums up all recursive elements that show up inside the list, 
#no matter the depth
# example: 
# sum_list_r( [1,[[2]],3,[7],2] ) = 15
# sum_list_r( [[[2]],3,[7],2] ) = 14
# sum_list_r( 1 ) = 1





# sum_list_r ( [1,[[2]],3,[7],2] ) =>
# sum_list_r ( [[[2]],3,[7],2] ) + sum_list_r ( 1 ) =>
# sum_list_r ( [3,[7],2] ) + sum_list_r([[2]]) + sum_list_r ( 1 )


def sum_list_r(val):
    if type(val) == type(1):
        return val
    sum = 0
    for element in val:
        sum += sum_list_r(element)        
    return sum 
        
     
if __name__ == '__main__':
    print(type(int))
    lst = [10, [1,[[2,5],2,4,5],3,[7],2] ]
    print(sum_list_r(lst) )
    
##########################################
# hw : to try and solve the function with no recursion 


##########################################
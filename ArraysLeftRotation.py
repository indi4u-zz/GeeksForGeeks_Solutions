def array_left_rotation(a, n, k):
    output = [0] * n
    for idx, val in enumerate(a):            
        if(idx - k > -1 ):
            new_idx = idx - k             
        else: 
            new_idx = (idx - k + n )      
       
        output[new_idx] = val
    return(output)

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
#print(a)
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

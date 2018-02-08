#code
test_cases = int(input())
for i in range(test_cases):
    line2 = list(map( int ,  input().strip().split(' ')))
    no_leaves =  line2[0]
    jumping_factor = list(map( int ,  input().strip().split(' ')))
    leaves = list(range(1,no_leaves+1) )
    
    for f in sorted(set(jumping_factor)):            
            for l in sorted(leaves):
                if(l%f == 0 and l in leaves):
                    #print('removing l',l)
                    leaves.remove(l)
                    
    print(len(leaves))
    
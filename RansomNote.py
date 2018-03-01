import collections

def ransom_note(magazine, ransom):
    dict1 = collections.Counter(magazine)
    dict2 = collections.Counter(ransom)
    
    for key,value in dict2.items():
        if( key in dict1.keys()):            
            if(dict1[key] < value):
                return(False)
        else:            
            return(False)
        
    return(True)

m, n = map(int, input().strip().split(' '))
magazine = list (input().strip().split(' '))
ransom = list( input().strip().split(' '))
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

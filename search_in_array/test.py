import algorithms


arrays = [[1, 9, 8, 2, 3, 4, 5, 7, 6],[11,31,50,69,78,95,92,4,25,36,74],[1156, 9812, 8882, 228181, 311,14, 225, 1817, 886],[158, 889, 528, 852, 823, 854, 54, 47, 56]]
for i in arrays:
    i.sort()
targets = [4,92,9812,159]  
expected = [3,9,7,-1]


cnt=-1
for i in arrays:
    cnt += 1 
    result = algorithms.ternary_search(i,targets[cnt])
    print(result)
   
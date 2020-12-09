dict1 = {} 
dict1 = {(0, 0): 1, (0, 1): 'John', (0, 2): 18, (0,3): 98, 
         (1, 0): 2, (1, 1): 'David', (1, 2): 18, (1,3): 97, 
         (2, 0): 3, (2, 1): 'Malan', (2, 2): 19, (2,3): 78,
         (3, 0): 4, (3, 1): 'Ralph', (3,2): 20, (3,3): 87,
         (4, 0): 5, (4, 1): 'Lewis', (4,2): 20, (4,3): 84,
} 
print("Roll No."," Name "," Age"," Marks(out of 100) " ) 
  
for i in range(5): 
      
    for j in range(4): 
        print(dict1[(i, j)], end ='\t') 
          
    print()
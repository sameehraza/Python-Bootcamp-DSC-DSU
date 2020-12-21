# Week 1 Assignment

## 1. Diagonal
### Script
```bash
string=input('E-nter a string:')
for i in range(len(string)):
    print(' '*i,string[i])
```
##Output
```bash
Enter a string:python    
 p 
  y
   t
    h
     o
      n
```
## 2. Records
### Script
```bash
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
```
### Output
```bash
Roll No.  Name   Age  Marks(out of 100) 
1       John    18      98
2       David   18      97
3       Malan   19      78
4       Ralph   20      87
5       Lewis   20      84
```
## 3. Lyrics
### Script
```bash
import time
baari_2 = "Kadi tu es Gali de hi , Agle morr te milda si , Tainu khabar si saari ke , Haal jo mere dil da si , Tu bhul gaya saariyan oh gallan , Te mai na bhulli ve sajna , Ke aj mainu vekh k vi hath te , Teri chaah dulli na sajna , Vekhi teri wafa sajna , Bhul gayi si mai raah sajna , Jandi jandi kho gayi saah , Khwaabaan de vich tere , Main taan hi uchiyan deewaran rakhiyan , Iss dil de chaar chufere , Naale saambh k rakhiya si , Koi dil ch na laa de dere"
song = baari_2.split(",")
for i in range(0,len(song),1):
    print(song[i])
    time.sleep(1)
```
### Output

``` bash
Kadi tu es Gali de hi 
 Agle morr te milda si 
 Tainu khabar si saari ke 
 Haal jo mere dil da si 
 Tu bhul gaya saariyan oh gallan 
 Te mai na bhulli ve sajna 
 Ke aj mainu vekh k vi hath te 
 Teri chaah dulli na sajna 
 Vekhi teri wafa sajna 
 Bhul gayi si mai raah sajna 
 Jandi jandi kho gayi saah 
 Khwaabaan de vich tere 
 Main taan hi uchiyan deewaran rakhiyan 
 Iss dil de chaar chufere 
 Naale saambh k rakhiya si 
 Koi dil ch na laa de dere

```

## 
Coding:
 
n=int(input())
for i in range(0,n):
 str1 = input()
 vowels = 0
 consonants = 0
 for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 print(vowels,end=" ")
 print(consonants)

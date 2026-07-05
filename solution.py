#solution for celusis to fahernhiet:
for i in range(0,101,10):
    print(i ,"-",i*9/5+32)    

#solution for count:
s=input("Enter a sentence:")
vow="aeiouAEIOU"
constant="bcdfghijklmopqrstuvwxyzBCDFGHIJKLMOPQRSTUVWXYZ"
space=" "
v=0
c=0
sp=0
for i in s:
    if i in vow:
        v+=1
    elif i in constant:
        c+=1
    elif i in space:
        sp+=1
print("the vowels in the sentence are:",v)
print("the consonansts in the sentnce are:",c)
print("the spaces in the sentnce are:",sp)

str=input("Enter string: ")
word=str.split()
max=0
for i in word:
    a=(len(i))
    if(max<a):
        max=a
        longest=i
print("Longest word in string is ",longest," with length of ",max)

ser=input("Enter the word whose frequency you want to find out string: ")
counter=0
for i in word:
    if(ser==i):
        counter=counter+1
print("Word ",ser," occur ",counter," times in string")

pal=input("Enter the word which you want to know is palindrome or not: ")
if(pal[0::]==pal[::-1]):
    print("Yes it is palindrome!!")
else:
    print("It's not palindrome!!")
    
substring=input("Enter the substring whose occurenece you want to find: ")
index=str.find(substring)
print("Substring ",substring," ocuur at index ",index)

for i in word:
    print("Length of word ",i," is ",len(i))
    


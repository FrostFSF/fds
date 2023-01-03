a = []
n = int(input("Enter number of elements: "))

for i in range(n):
    a.append(int(input("Enter elements: ")))

#sentinal search
search_key = int(input("Enter searching element: "))

temp = a[n-1]
a[n-1] = search_key

i = 0
while(a[i] != search_key):
    i+=1

a[n-1] = temp
if(i < n-1 or a[n-1] == search_key):
    print("Found" , i)
else:
    print("Not found")
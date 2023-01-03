marks=[]
marks1=[]
n=int(input("Enter total number of students: "))
print("Enter prcentage of ",n," students: ")
for i in range(0,n):
    print("Enter percentage of ",i+1," student: ")
    x=float(input())
    marks.append(x)
    marks1.append(x)
print("List of percentage of students: ",marks)
for i in range(0,n):
    min=i
    for j in range((i+1),n):
        if(marks[j]<marks[min]):
            min=j
    if(min!=i):
        temp=marks[i]
        marks[i]=marks[min]
        marks[min]=temp
print("List of percentage sorted by selection sort is: ",marks)
for a in range(0,n):
    for b in range(0,n-1):
        if(marks1[b]>marks1[b+1]):
            temp1=marks1[b+1]
            marks1[b+1]=marks1[b]
            marks1[b]=temp1
print("List of percentage sorted by bubble sort: ",marks1)

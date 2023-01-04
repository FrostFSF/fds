'''
Group A - Assignment no.2
Write a python program to store marks scored in subject Fundamentals of Data Structure by n sudents in the class.
Write function to compute following:
1) The average score of class
2) Highest score and lowest score of class
3) Count of students who were absent for the test.
4) Display marks with highest frequency
'''

def avg_marks(marks,n):
    sum = 0
    for i in marks:
        if i != -1 :
            sum = sum + i
    x = ab_student(marks,n)
    avg = sum/(n-x)
    print ("The average is ", avg)

def high_frequency_marks(marks,n):
    count1 = 0
    mrks = 0
    mrks1 = 0 
    for i in range (n):
        count = 0
        mrks = 0
        j = i+1
        if (marks [i] != -1):
            while (j< n):
                if (marks[i]==marks[j]):
                    count = count+1
                    mrks = marks[i]
                j = j+1
        if (count1<count):
            count1 = count +1
            mrks1 = mrks
    print ("Highest Frequency is ",count1)
    print("Marks is ",mrks1)

def high_low(marks,n):
    high = -1
    low = 9999
    for i in marks:
        if i !=-1 :
            if high < i :
                high = i
            if low > i:
                low = i 
    print ("The highest marks ",high,"The lowest marks ",low)

def ab_student(marks,n):
    count = 0
    for i in marks:
        if i == -1:
            count = count+1
    return count

def main():
    marks=[]
    n = int (input ("ENtet the numer of elements :- "))
    for i in range(n):
        marks.append(int(input("ENter the marks :- ")))
    
    high_low(marks,n)
    z = ab_student(marks,n)
    print("The number of absent Students ",z)
    avg_marks(marks,n)
    high_frequency_marks(marks,n)

main()
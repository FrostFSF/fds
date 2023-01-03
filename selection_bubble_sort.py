def selection_sort(array):
    n = len(array)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(array[j] < array[i]):
                array[j],array[i] = array[i],array[j]


def bubble_sort(array):
    n = len(array)
    counter = 1
    while(counter < n):
        for i in range(n-counter):
            if(array[i] > array[i+1]):
                array[i],array[i+1] = array[i+1],array[i]
        counter+=1

def display_top_five(array):
    n = len(array)
    for i in range(n-5,n):
        print(array[i],end=" ")

def main():
    a = []
    done = 0
    while(1):
        print("\n1) accept data")
        print("2) selection sort")
        print("3) bubble sort")
        print("4) exit")
        user_choice = int(input("Enter choice: "))

        if(user_choice == 4):
            print("EXITED!")
            break
        elif(user_choice == 1):
            n = int(input("Enter number of elements: "))
            for i in range(n):
                a.append(int(input("Enter elements: ")))
            done = 1
        elif(user_choice == 2):
            if(done == 1):
                selection_sort(a)
                display_top_five(a)
            else:
                print("Please accept data first")
        elif(user_choice == 3):
            if(done == 1):
                bubble_sort(a)
                display_top_five(a)
            else:
                print("Please accept data first")
        else:
            print("Invalid choice")

main()

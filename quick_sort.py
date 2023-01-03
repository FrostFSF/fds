def swap(array,i,j):
    array[i],array[j] = array[j],array[i]


def partition(array,left_index,right_index):
    pivot = array[right_index]
    i = left_index - 1

    for j in range(left_index,right_index):
        if(array[j] < pivot):
            i+=1
            swap(array,i,j)
    swap(array,i+1,right_index)
    return i+1



def quicksort(array,left_index,right_index):
    
    if(left_index < right_index):
        pi = partition(array,left_index,right_index)

        quicksort(array,left_index,pi-1)
        quicksort(array,pi+1,right_index)


def display_top_five(array):
    n = len(array)
    for i in range(n-5,n):
        print(array[i],end=" ")


def main():
    a = []
    done = 0
    while(1):
        print("\n1) accept data")
        print("2) quick sort")
        print("3) exit")
        user_choice = int(input("Enter choice: "))

        if(user_choice == 3):
            print("EXITED!")
            break
        elif(user_choice == 1):
            n = int(input("Enter number of elements: "))
            for i in range(n):
                a.append(float(input("Enter elements: ")))
            done = 1
        elif(user_choice == 2):
            if(done == 1):
                quicksort(a,0,n-1)
                display_top_five(a)
            else:
                print("Please accept data first")
        else:
            print("Invalid choice")

main()
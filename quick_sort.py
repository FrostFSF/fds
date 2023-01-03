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



def main():
    a = []
    n = int(input("Enter number of elements: "))

    for i in range(n):
        a.append(int(input("Enter element: ")))
    
    quicksort(a,0,n-1)
    print(a)

main()
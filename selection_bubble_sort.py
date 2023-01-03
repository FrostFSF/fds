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


def main():
    a = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        a.append(int(input("Enter elements: ")))

    #selection_sort(a)
    #bubble_sort(a)
    print(a)

main()

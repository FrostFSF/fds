def Fibonacci_Search(A,n,X) :
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    offset = -1
    while (f3 < n) :
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    while (f3 > 1) :
        i = min(offset+f1, n-1)
        if(A[i] == X) :
            return i #Found
        else :
            if (X < A[i] ) : # left substudent (66 % or 2/3 student)
                f3 = f1
                f2 = f2 - f1
                f1 = f3 - f2
            else : # right substudent ( 33 % or 1/3 student)
                f3 = f2
                f2 = f1
                f1 = f3 - f2
                offset = i
    if(f2 == 1 and (offset+1) < n and A[offset + 1] == X) : 
        return offset+1 # Found
    return -1 #NOT FOUND

a = [1,2,3,4,5]
flag = Fibonacci_Search(a,5,6)
if(flag == -1):
    print("NOT FOUND")
else:
    print("FOUND AT: ", flag)
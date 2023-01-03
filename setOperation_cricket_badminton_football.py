def accept_data(cricket,badminton,football):
    c1=int(input("Enter the no. of students who play cricket: "))
    b1=int(input("Enter the no. of students who play badminton: "))
    f1=int(input("Enter the no. of students who play football: "))


    print("the number of students in cricket are:",c1)
    print("the number of students in badminton are:",b1)
    print("the number of students in football are:",f1)

    for i in range(c1):
        name=input("enter the name:")
        cricket.add(name)
    print("the names of students in cricket are:")
    print(cricket)

    for i in range(b1):
        name=input("enter the name:")
        badminton.add(name)
    print("the names of students in badminton are:")
    print(badminton)

    for i in range(f1):
        name=input("enter the name:")
        football.add(name)
    print("the names of students in football are:")
    print(football)

def play_cricket_and_badminton(cricket,badminton):
    play=set()

    for i in cricket:
        if i in badminton:
            play.add(i)

    print("the students who play cricket and badminton are:",play)

def play_either_cricket_or_badminton_but_not_both(cricket,badminton):
    abbb=set()

    for i in cricket:
        if i not in badminton:
            abbb.add(i)

    for i in badminton:
        if i not in cricket:
            abbb.add(i)

    print("the students who play either cricket or badminton but not both",abbb)

def play_neither_cricket_nor_badminton(cricket,badminton,football):
    play=set()

    for i in football:
        if i not in cricket and badminton:
            play.add(i)
    
    print("the no of students who play neither cricket nor badminton",len(play),play)

def play_cricket_and_football_not_badminton(cricket,badminton,football):
    play=set()
    
    
    for i in cricket:
        if i in football and i not in badminton:
            play.add(i)
        

    print ("the no. of students playing cricket and football but not  badminton",len(play))

        

    

   


def main():
    cricket=set()
    badminton=set()
    football=set()
    
    accept_data(cricket,badminton,football)
    play_cricket_and_badminton(cricket,badminton)
    play_either_cricket_or_badminton_but_not_both(cricket,badminton)
    play_neither_cricket_nor_badminton(cricket,badminton,football)
    play_cricket_and_football_not_badminton(cricket,football,badminton)

main()
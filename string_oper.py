def longest_word(string_any):
    word = string_any.split()
    max_word_len = 0
    longest = ""
    for i in word:
        if(max_word_len < len(i)):
            max_word_len = len(i)
            longest = i
    
    print("Longest word: ", longest, " of length: ", max_word_len)


def frequecy(string_any):
    x = input("Enter a character: ")
    counter = 0
    for i in string_any:
        if(i == x):
            counter+=1
    print("Frequency of ", x, " is: ",counter)


def is_palindrome(string_any):                             
    if(string_any[::] == string_any[::-1]):
        print("Palindrome")
    else:
        print("Not palindrome")


def is_substring(string_any):

    substr = input("Enter a sub string: ")
    i = string_any.find(substr)
    print(i)




def main():
    while(1):
        print("1) accept data")
        print("2) frequency of character")
        print("3) longest word")
        print("4) Is plaindrome")
        print("5) Is substring")
        print("6) exit")

        user_choice = int(input("Enter choice: "))
        if(user_choice == 6):
            print("EXITED!")
            break
        elif(user_choice == 1):
            string = input("Enter string: ")

        elif(user_choice == 2):
            frequecy(string)

        elif(user_choice == 3):
            longest_word(string)

        elif(user_choice == 4):
            is_palindrome(string)

        elif(user_choice == 5):
            is_substring(string)

        else:
            print("Invalid choice!")
    

main()
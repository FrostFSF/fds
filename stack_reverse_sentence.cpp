#include <iostream>
#include <string.h>
using namespace std;

#define size 100

char array[size];
int top = -1;

void push(char any)
{
    if(top == size-1)
    {
        cout << "FULL";
    }
    else
    {
        top++;
        array[top] = any;
    }
}

char pop()
{
    if(top == -1)
    {
        cout << "EMPTY";
    }
    else
    {
        char x = array[top];
        top--;
        return x;
    }
}


void display()
{
    for (int i = top; i >= 0; i--)
    {
        cout << array[top] << "";
    }
}





int main()
{
    string myStr;
    cout << "Enter a string: ";
    getline(cin,myStr);

    for (int i = 0; i < myStr.length(); i++)
    {
        push(myStr[i]);
    }

    char reverse[100];
    int a = 0;
    for(int i = top; i >= 0; i--)
    {
        reverse[a] = pop();
        a++;
    }
    cout << reverse << endl;
    if(reverse == myStr)
    {
        cout << "Plaindrome";
    }
    else
    {
        cout << "NO";
    }

    
}
#include <iostream>

using namespace std;

int main()
{
    int space=5, leftspace=5, rightspace=5, x=1, xcurrent=1, row=0, currentrow=0;
    while(row<6)
    {
        while(leftspace!=0)
        {
            cout << " ";
            leftspace--;
        }
        while(xcurrent!=0)
        {
            cout << "X";
            xcurrent--;
        }
        while(currentrow>0)
        {
            cout << "X";
            currentrow--;
        }
        while(rightspace!=0)
        {
            cout << " ";
            rightspace--;
        }
        cout << endl;
        space--;
        leftspace = space;
        rightspace = space;
        x++;
        xcurrent = x;
        row++;
        currentrow=row;
    }
    cout << endl << endl << "6 rows of X" << endl << "Needs nested loops" << endl << "Observe the pattern" << endl;
    return 0;
}

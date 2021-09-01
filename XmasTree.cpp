#include <iostream>
using namespace std;

int main()
{
    for(int n=0;n<6;n++)
    {
        if(n==0)
            cout<<"     x     ";
        if(n==1)
            cout<<"\n    xxx    ";
        if(n==2)
            cout<<"\n   xxxxx   ";
        if(n==3)
            cout<<"\n  xxxxxxx  ";
        if(n==4)
            cout<<"\n xxxxxxxxx ";
        if(n==5)
            cout<<"\nxxxxxxxxxxx";
    }
    return 0;
}

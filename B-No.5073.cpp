// src : https://www.acmicpc.net/problem/5073
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[3];
    while(true)
    {
        for(int i=0;i<3;i++)
            cin >> a[i];
        sort(a,a+3);

        if(a[2]==0)
            break;
        else if(a[0]+a[1]<=a[2])
            cout<<"Invalid"<<endl;
        else if(a[0]==a[2])   
            cout<<"Equilateral"<<endl;
        else if(a[1]==a[2] || a[0]==a[1])
            cout<<"Isosceles"<<endl;
        else
            cout<<"Scalene"<<endl; 
    }
    return 0;
}
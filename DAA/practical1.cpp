#include<iostream> 
using namespace std;

void Fibbonacci(int n){
    int a = 0;
    int b = 1;
    int sum = 0;
    cout<<a<<" "<<b<<" ";

    for(int i=2; i<n;i++){
        sum = a+b;
        cout<<sum<<" ";
        a = b;
        b = sum;
    }
    cout<<endl;
}

int FibbonacciR(int n){
    if(n==0 || n==1){
        return n;
    }
    return FibbonacciR(n-1) + FibbonacciR(n-2);
}

int main(){
    int n;
    cout<<"Enter the value upto which you want the fibbonacci series ";
    cin>>n;
    Fibbonacci(n);
    cout<<"Fibonacci series using the recurssion "<<endl;
    for(int i = 0; i<n; i++){
        cout<<FibbonacciR(i)<<" ";
    }
    return 0;
}
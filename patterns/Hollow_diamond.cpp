#include<iostream>
using namespace std;

main() {
    int n;
    cin >> n;

    for(int i=1;i <= n;i++) {
        for(int j=1;j <= n-i;j++) {
            cout << " ";
        }

        cout << "*";

        for(int j=1;j <= (i-2)*2+1;j++) {
            cout << " ";
        }

        if(i > 1) {
            cout << "*";
        }

        cout << endl;
    }

    for(int i=1;i <= n-1;i++) {

        for(int j=1;j <= i;j++) {
            cout << " ";
        }

        cout << "*";

        for(int j=1;j <= (n-i-2)*2+1;j++) {
            cout << " ";
        }

        if(i < n-1) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}
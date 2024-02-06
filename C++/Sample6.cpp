#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> vt;
    for(int i=0; i<10; i++){
        vt.push_back(i);
    }

    cout << "정렬하기 전의 상태는 ";
    vector<int>::iterator it = vt.begin();
    while(it != vt.end()){
        cout << *it; it++;
    }
    cout << " 입니다.\n";

    cout << "뒤집으면 ";
    reverse(vt.begin(), vt.end()); 
    it = vt.begin ();
    while(it != vt.end()){ 
        cout << *it;
        it++;
    }
    cout << " 입니다.\n";

    cout << "정렬 후의 상태는 ";
    sort(vt.begin(), vt.end()); 
    it = vt.begin ();
    while(it != vt.end()){
        cout << *it;
        it++;
    }
    cout << " 입니다.\n";
}
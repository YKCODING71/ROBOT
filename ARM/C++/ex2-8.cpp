#include <iostream>
#include <string>
using namespace std;

int main() {
    int totalSale = 0;  // 현재까지 판매 총 금액
    int order;          // 현재 주문한 금액
    string coffee;      // 주문한 커피 종류
    int num;            // 잔 수
    cout << "아메리카노 3000원, 카푸치노 4000원, 아이스아메리카노 3500원입니다." << endl;

    while (true) {
        cout << "주문>> ";
        cin >> coffee >> num;

        if (num <= 0) { 
            cout << "잔 수는 양수를 입력해주세요" << endl;
            continue;
        }

        if (coffee == "아메리카노") order = 3000 * num;
        else if (coffee == "아이스아메리카노") order = 3500 * num;
        else if (coffee == "카푸치노") order = 4000 * num;
        else order = 0;
        
        if (order > 0) cout << order << "원입니다. 맛있게 드세요" << endl;
        else cout << "없는 커피입니다. 다시 입력해주세요" << endl;

        totalSale += order;
        if (totalSale > 100000) {
            cout << "주문을 마감합니다. \n판매총액: " << totalSale << "원" << endl;
            break;
        }
    }       
}

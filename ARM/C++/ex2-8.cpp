#include <iostream>
#include <string>
using namespace std;

int main() {
    int totalSale = 0;  // ������� �Ǹ� �� �ݾ�
    int order;          // ���� �ֹ��� �ݾ�
    string coffee;      // �ֹ��� Ŀ�� ����
    int num;            // �� ��
    cout << "�Ƹ޸�ī�� 3000��, īǪġ�� 4000��, ���̽��Ƹ޸�ī�� 3500���Դϴ�." << endl;

    while (true) {
        cout << "�ֹ�>> ";
        cin >> coffee >> num;

        if (num <= 0) { 
            cout << "�� ���� ����� �Է����ּ���" << endl;
            continue;
        }

        if (coffee == "�Ƹ޸�ī��") order = 3000 * num;
        else if (coffee == "���̽��Ƹ޸�ī��") order = 3500 * num;
        else if (coffee == "īǪġ��") order = 4000 * num;
        else order = 0;
        
        if (order > 0) cout << order << "���Դϴ�. ���ְ� �弼��" << endl;
        else cout << "���� Ŀ���Դϴ�. �ٽ� �Է����ּ���" << endl;

        totalSale += order;
        if (totalSale > 100000) {
            cout << "�ֹ��� �����մϴ�. \n�Ǹ��Ѿ�: " << totalSale << "��" << endl;
            break;
        }
    }       
}

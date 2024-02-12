#include <iostream>
using namespace std;

int main() {
	int n[10];
	int i;
	int *p;
	
	for (i = 0; i < 10; i++) {
		*(n + i) = i * 3;
	}

	p = n; 
	for (i = 0; i < 10; i++) {
		cout << *(p + i) << ' ';
	}
	cout << "\n";
	
	for(i=0; i<10; i++) {
		*p = *p + 2; 
		p++; 
	}

	for(i=0; i<10; i++)	cout << n[i] << ' '; 
	cout << "\n";	
}
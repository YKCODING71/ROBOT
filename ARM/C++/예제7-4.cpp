#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void main()
{
    int value;
    printf("������ �Է��ϰ� Enter>");
    scanf("%d", &value);
    if (value > 0)
        printf("����Դϴ�.\n");
    else if (value < 0)
        printf("�����Դϴ�.\n");
    else
        printf("0�Դϴ�.\n");
}

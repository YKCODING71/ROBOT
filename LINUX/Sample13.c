#include <stdio.h>
#include <string.h>

int main(void)
{
   char str0[20];
   char str1[10];
   char str2[10];

   strcpy_s(str1, 10, "Hello");
   strcpy_s(str2, 10, "Goodbye");
   strcpy_s(str0, 20, str1);
   strcat_s(str0, 20, str2);

   printf("배열 str1는 %s입니다. \n", str1);
   printf("배열 str2는 %s입니다. \n", str2);
   printf("연결하면 %s입니다. \n", str0); 

   return 0;
}

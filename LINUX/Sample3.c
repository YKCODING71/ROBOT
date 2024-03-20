#include <stdio.h>

int main(void)
{
   int test[5] = {80,60,55,22,75};

   printf("test[0]의 값은 %d입니다. \n", test[0]);
   printf("test[0]의 어드레스는 %p입니다. \n", &test[0]);
   printf("test의 값은 %p입니다. \n", test);
   printf("즉 *test의 값은 %d입니다. \n", *test);

   return 0;
}

#include <stdio.h>

/* avg 함수의 선언 */
double avg(int *pT);

int main(void)
{
   int test[5];
   int i;
   double ans;

   printf("5명의 시험 점수를 입력하세요. \n"); 

   for(i=0; i<5; i++){
      scanf_s("%d", &test[i]);
   }

   ans = avg(test);

   printf("5명의 평균은 %lf점입니다. \n", ans);

   return 0;
}

/* avg 함수의 정의 */
double avg(int *pT)
{
   int i;
   double sum;

   sum = 0.0;
   
   for(i=0; i<5; i++){
      sum += pT[i];
   }
   return sum/5;
}

#include <stdio.h>

int main(void) {
	int i,a ,b;
	scanf("%d %d", &a,&b);
	for (i=a+1; i<b ;i++)
	    if( i%2==0)
	      printf("%d" "\t",i);
	return 0;
}

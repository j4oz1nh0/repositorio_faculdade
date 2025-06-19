#include <stdio.h>
#include <stdio.h>
void main() {
 int *p, *q, i=99, j=10;
 p = &i;
 p = &*&i;
 i = *&*&j;
 q = p;
 i=(*p)++ + *q;
 i=(*&j);
 printf( "a) p = &i: %d \n", &i);
 printf( "b) p = &*&i: %d \n", &*&i);
 printf( "c) i = (*&)j: %d \n", *&j);
 printf( "d) i = *&*&j: %d \n", *&*&j);
 printf( "e) q = &p: %d \n", &p);
 printf( "f) i = (*p)++ +*q: %d \n", (*p)++ +*q);
}

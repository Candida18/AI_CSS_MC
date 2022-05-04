#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
char c[1000];
char value[1000];
char operators[10][1] = {"+", "=", "-", "*", "/"};
char keywords[10][10] = {"int", "float", "char", "double", "long"};
FILE *fp1;
fp1 = fopen("input.txt", "r");
memset(value, 0, 1000);
fscanf(fp1, "%s", c);
while (strcmp(c, "END") != 0)
{
int i = 0;
int flag = 0;
int j = 0;
while (c[i] != ' ')
{
value[j++] = c[i++];
}
int k = 0;
while (k < 5)
{/* code */
// printf("%s\n",keywords[i++]);
if (strcmp(value, keywords[k++]) == 0)
{
printf("\n%s is keyword", value);
flag = 1;
}
}
if (value[0] >= 42 && value[0] <= 47 && value[0] != 44 || value[0] >=
60 && value[0] <= 62 || value[0] == 37 || value[0] == 38)
{
printf("\n%s is operator", value);
}
else if (value[0] >= 58 && value[0] <= 59 || value[0] == 44)
{
printf("\n%s is special symbol", value);
}
else if (value[0] >= 48 && value[0] <= 57)
{
printf("\n%s is constant", value);
}
else if (value[0] == 34 || value[0] == 39)
{
printf("\n%s is literal", value);
}
else if (flag == 0)
{
printf("\n%s is identifier", value);
}
memset(value, 0, 1000); // to clear the buffer
fscanf(fp1, "%s", c);
}
return 0;
}

/*
int a ;
float b = 10.2 ;
char ch = 'z' ;
char d = "strings" ;
int d = a * b ;
$name ;
END*/
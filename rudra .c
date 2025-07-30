#include<stdio.h>
int main(){
    int rows,col,i,j;
    printf("enter the rows");
    scanf("%d",&rows);
    printf("enter colounm");
    scanf("%d",&col);
    int arr1[rows][col],arr2[rows][col],addition[rows,coloumn];
    for(i=0;i<rows;i++){
        for(j=0;j<col;j++){
        printf("enter elements %d ,%d",i,j);
    scanf("%d",&arr1[i][j]);
    }
}
for(i=0;i<rows;i++){
    for(j=0;j<col;j++){
    printf("enter elements %d ,%d",i,j);
scanf("%d",&arr2[i][j]);
}
}
for(i=0;i<rows;i++){
    for(j=0;j<col;j++){
    addition[i][j]=arr1[i]+arr[j];
}
printf("\n");
}

}

int main()
{
    int r;
    scanf("%d",&r);
    for (int i=1;i<=r;i++) 
    {
        for (int j=1;j<=r-i;j++)
        {
                printf(" ");
        }
        for (int j=1;j<2*i;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

#include <unistd.h>

void ft_alphabetreversed(void)
{
    char zeta='z';
    while (zeta>='a')
    {
        write(1, &zeta, 1);
        zeta--;
    }
    
}

int main(char)
{
    ft_alphabetreversed();
    return 0;
}
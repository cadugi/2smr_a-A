#include <unistd.h>

void ft_numbers(void)
{
    char one;
    one='1';
    while (one <= '9')
    {
        write(1, &one , 1);
        one++;
    }
    
}

int main(void)
{
    ft_numbers();
    return 0;
}
#include <unistd.h>

void ft_alphabet(void)
{
    char alpha='a';
    while (alpha <= 'z')
    {
        write(1, &alpha, 1);
        alpha++;
    }
    

}

int main(char)
{
    ft_alphabet();
    return 0;
}

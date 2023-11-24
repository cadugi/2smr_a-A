#include <unistd.h>

void negative(int n)
{
    if (n > 0)
    {
        write(1, "P", 1);
    }
    else
    {
        write(1, "N", 1);
    }
}

int main(int argc, char const *argv[])
{
    int n = -5;
    negative(n);
    return 0;
}

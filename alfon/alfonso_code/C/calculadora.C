#include <stdio.h>

float potencia(float base, int exponente) 
{
    float resultado = 1;
    for (int i = 0; i < exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

int main()
{
    float x, y, resultado;
    char op;
    int valido = 1;

    printf("Ingrese operacion (+, -, *, /, ^): ");
    scanf(" %c", &op);  // Corrected the scanf format specifier

    printf("Ingrese el primer digito: ");
    scanf("%f", &x);  // Corrected the scanf format specifier and removed the extra comma

    printf("Ingrese el segundo digito: ");
    scanf("%f", &y);  // Corrected the scanf format specifier

    switch (op)
    {
        case '+':
            resultado = x + y;
            break;
        case '-':
            resultado = x - y;
            break;
        case '*':
        case 'x':  // Corrected the case for multiplication
            resultado = x * y;
            break;
        case '/':
            resultado = x / y;
            break;
        case '^':
            resultado = potencia(x, (int)y);  // Used the potencia function for exponentiation
            break;
        default:
            valido = 0;
    }

    if (valido)
        printf("El resultado es %f\n", resultado);
    else
        printf("Operacion invalida\n");

    return 0;
}

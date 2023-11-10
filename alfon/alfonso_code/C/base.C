#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef _WIN32
// No es Windows, no es necesario comprobar OpenSSL
#define CHECK_OPENSSL
#endif

#ifdef CHECK_OPENSSL
#include <openssl/aes.h>
#endif

// Función para verificar si OpenSSL está instalado
int opensslInstalado() {
#ifdef CHECK_OPENSSL
    // Intenta incluir los encabezados de OpenSSL
    #include <openssl/aes.h>
    return 1;
#else
    return 0;
#endif
}

// Función para redirigir al usuario a la página de descarga de OpenSSL
void redirigirDescargaOpenSSL() {
    printf("OpenSSL no está instalado. Por favor, descárguelo e instálelo desde:\n");
    printf("https://slproweb.com/download/Win64OpenSSL-3_1_4.exe\n");
}

#define MAX_USUARIO 100
#define MAX_CONTRASENA 100
#define MAX_CUENTAS 10
#define ARCHIVO_CUENTAS "cuentas.bin"

typedef struct {
    char usuario[MAX_USUARIO];
    char contrasena[MAX_CONTRASENA];
} Credenciales;

typedef struct {
    Credenciales *cuentas[MAX_CUENTAS];
    int numCuentas;
} AlmacenCuentas;

// Clave secreta para AES (128 bits = 16 bytes)
static const unsigned char aes_key[] = "tuclave123456789";

void encriptarDatos(Credenciales *datos) {
    AES_KEY aesKey;
    AES_set_encrypt_key(aes_key, 128, &aesKey);

    AES_encrypt((unsigned char *)datos->usuario, (unsigned char *)datos->usuario, &aesKey);
    AES_encrypt((unsigned char *)datos->contrasena, (unsigned char *)datos->contrasena, &aesKey);
}

void desencriptarDatos(Credenciales *datos) {
    AES_KEY aesKey;
    AES_set_decrypt_key(aes_key, 128, &aesKey);

    AES_decrypt((unsigned char *)datos->usuario, (unsigned char *)datos->usuario, &aesKey);
    AES_decrypt((unsigned char *)datos->contrasena, (unsigned char *)datos->contrasena, &aesKey);
}

Credenciales *crearCredenciales(const char *usuario, const char *contrasena) {
    Credenciales *credenciales = (Credenciales *)malloc(sizeof(Credenciales));
    strcpy(credenciales->usuario, usuario);
    strcpy(credenciales->contrasena, contrasena);
    return credenciales;
}

void guardarCuentas(AlmacenCuentas *almacen) {
    FILE *archivo = fopen(ARCHIVO_CUENTAS, "wb");
    if (archivo == NULL) {
        printf("Error al abrir el archivo para escritura.\n");
        return;
    }

    for (int i = 0; i < almacen->numCuentas; ++i) {
        encriptarDatos(almacen->cuentas[i]);
        fwrite(almacen->cuentas[i], sizeof(Credenciales), 1, archivo);
        encriptarDatos(almacen->cuentas[i]);  // Desencriptar para mantener desencriptados los datos en el programa
    }

    fclose(archivo);
}

void cargarCuentas(AlmacenCuentas *almacen) {
    FILE *archivo = fopen(ARCHIVO_CUENTAS, "rb");
    if (archivo == NULL) {
        printf("Archivo de cuentas no encontrado. Creando uno nuevo.\n");
        return;
    }

    while (almacen->numCuentas < MAX_CUENTAS &&
           fread(almacen->cuentas[almacen->numCuentas], sizeof(Credenciales), 1, archivo) == 1) {
        // Allocate memory for the loaded credential
        almacen->cuentas[almacen->numCuentas] = (Credenciales *)malloc(sizeof(Credenciales));
        // Desencriptar solo al cargar desde el archivo
        desencriptarDatos(almacen->cuentas[almacen->numCuentas]);
        almacen->numCuentas++;
    }

    fclose(archivo);
}

void agregarCuenta(AlmacenCuentas *almacen) {
    if (almacen->numCuentas < MAX_CUENTAS) {
        char usuario[MAX_USUARIO];
        char contrasena[MAX_CONTRASENA];

        printf("Ingrese el nombre de usuario: ");
        scanf("%s", usuario);

        printf("Ingrese la contrasena: ");
        scanf("%s", contrasena);

        almacen->cuentas[almacen->numCuentas++] = crearCredenciales(usuario, contrasena);
        printf("Cuenta guardada exitosamente.\n");
        guardarCuentas(almacen);
    } else {
        printf("El almacen de cuentas está lleno.\n");
    }
}

void verCuentas(AlmacenCuentas *almacen) {
    printf("Cuentas almacenadas:\n");
    for (int i = 0; i < almacen->numCuentas; ++i) {
        // Desencriptar antes de mostrar
        desencriptarDatos(almacen->cuentas[i]);
        printf("Usuario: %s\nContrasena: %s\n\n", almacen->cuentas[i]->usuario, almacen->cuentas[i]->contrasena);
        // Volver a encriptar para evitar cambios en la memoria
        encriptarDatos(almacen->cuentas[i]);
    }
}

int main() {
    AlmacenCuentas almacen;
    almacen.numCuentas = 0;

    // Allocate memory for each account
    for (int i = 0; i < MAX_CUENTAS; ++i) {
        almacen.cuentas[i] = (Credenciales *)malloc(sizeof(Credenciales));
    }
        if (!opensslInstalado()) {
        redirigirDescargaOpenSSL();
        return 1;  // Salir del programa
    }

    cargarCuentas(&almacen);

    int opcion;
    do {
        printf("\nSeleccione una opcion:\n");
        printf("1. Agregar Cuenta\n");
        printf("2. Ver Cuentas\n");
        printf("0. Salir\n");
        scanf("%d", &opcion);

        switch (opcion) {
        case 1:
            agregarCuenta(&almacen);
            break;
        case 2:
            verCuentas(&almacen);
            break;
        case 0:
            printf("Saliendo del programa.\n");
            break;
        default:
            printf("Opción no válida. Intente de nuevo.\n");
        }

    } while (opcion != 0);

    // Liberar memoria
    for (int i = 0; i < MAX_CUENTAS; ++i) {
        free(almacen.cuentas[i]);
    }

    return 0;
}

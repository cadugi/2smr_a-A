# Función para verificar si el script se está ejecutando como administrador
function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $adminRole = [Security.Principal.WindowsBuiltInRole]::Administrator
    return $currentUser.IsInRole($adminRole)
}

# Verifica si el script se está ejecutando como administrador y solicita elevación si es necesario
if (-not (Test-Admin)) {
    $arguments = "& '" + $MyInvocation.MyCommand.Definition + "'"
    Start-Process PowerShell -Verb RunAs -ArgumentList $arguments
    Write-Host "Solicitando permisos de administrador..."
    exit
}

# Define la ruta del archivo y el mensaje
$rutaDestino = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Mensaje.txt"
$mensaje = "Buenos dias, amor mio."

# Intenta crear el archivo en la carpeta de inicio común con privilegios elevados
try {
    # Crea el archivo de texto con el mensaje
    $mensaje | Out-File -FilePath $rutaDestino -Encoding UTF8


} catch {
    Write-Host "Error al crear el archivo: $_.Exception.Message"
}

# Pausa para que puedas ver los mensajes antes de que se cierre la ventana


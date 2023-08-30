#Investigar el módulo sys
#El modulo sys permite verificar e interactuar con el sistema operativo, directorios, etc
import sys
print("plataforma:", sys.platform)
print(sys.stdout.write("Estandar de salida: "))
print("Version de Python:",sys.version)
print("Sistema de codificacion:", sys.getfilesystemencoding())
print("Sistema de codificacion por defecto:", sys.getdefaultencoding())
print("El sistema de variable por la ruta:", sys.path)
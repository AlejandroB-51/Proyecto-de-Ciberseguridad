Fecha de Inicio: 9 de octubre 2026
Herramientas utilizadas: Navegador web, terminal Linux brindada por la web "TryHackMe", TryHackMe AttackBox

1.-  Resumen de la Actividad: El objetivo de este laboratorio es aprender a iniciar sesión y controlar terminales de máquinas remotas mediante SSH
  1.- SSH: Secure Shell (SSH) es un protocolo que le permite a dos dispositivos comunicarse de forma cifrada

2.- Conexión SSH
  1.- Usamos la terminal linux para conectarnos de forma remota a la maquina objetivo que es el cliente de este laboratorio, para hacerlo usaremos el comando: ssh nombredeusurio@dirección_IP. el nombre de usuario que nos dan es: tryhackme. por en la terminal colocamos: ssh tryhackme@10.10.119.205 (10.10.119.205 es la IP de la TryHackMe AttackBox que se me brindo en este laboratorio), después de hacerlo la terminal me pidió la contraseña del usuario, el laboratorio nos da esa contraseña y es: tryhackme

3.- Banderas e Interruptores  
  1.- Especificación de Argumentos: En la mayoría de los argumentos podemos especificar argumentos, esto se hace escribiendo un guion "-" seguido de una palabra clave que es conocida como parámetros. en los comandos estos realizan su comportamiento predeterminado a no ser que se especifique lo contrario, el laboratorio nos da un ejemplo con el comando "ls" que nos permite ver el contenido del directorio e el que nos encontramos excluyendo los archivos ocultos, pero podemos usar los parámetros para de esta forma se puedan ampliar los comportamientos de los comandos, al usar "ls -a" nos sirve para ver los archivos que empiezan con "." que son archivos ocultos, "-a" en ese parámetro "a" es la abreviatura de "all". Los comandos que aceptan parámetros tambien incluyen el parámetro "--help" que nos mostrara una lista de los parámetros que se pueden usar y su función
  
4.- Comandos de Linux
  touch: Permite crear archivos 
  mkdir: Crea directorios 
  cp: Copia archivos o carpetas 
  mv: Mueve un archivo o carpeta
  rm: Elimina un archivo o carpeta
  type: Nos ayuda a saber el origen de un comando y donde esta guardado
  file: Nos mostrara el formato real del archivo así como el contenido de este
  su: Ese comando nos permite cambiar entre usuarios

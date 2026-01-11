# DataBunker-AA5

<<<<<<< HEAD
Proyecto Data Bunker
1. Descripción del proyecto
Trabajo hecho por: Anna Gual Poblet, Lena Boajram Makarem, Andrea Olivas Vazquez, Lucas Delas De Esteban y Pol Latorre Cañisà. En este Sprint (Tareas 12-23) hemos hecho lo necesario para crear claves de seguridad y encriptar archivos. El problema que resolvemos es coger archivos y convertirlos a formato cifrado para que nadie los pueda leer sin permiso.
2. Requisitos de sistema y dependencias
Para que funcione nuestro código, aparte de tener Python, hay que instalar la librería de criptografía. Es lo único externo que hemos usado para que la seguridad con Fernet vaya bien. Si no tienes esto instalado, el programa no arrancará porque le faltarán herramientas.
3. Pasos de instalación (dev)
Simplemente descarga los archivos del proyecto. Luego, abre la consola y escribe el comando: pip install cryptography. No hay que hacer nada más complicado, solo asegúrate de tener todos los .py en la misma carpeta para que se encuentren entre ellos.
4. Instrucciones detalladas de uso
Para probarlo, ejecuta el menú (main.py o interfaz.py). Lo primero es la "Prueba de la clave": dale a generar y debería aparecer el archivo key.key en la carpeta; sin esto no se puede hacer nada. Luego haz la "Prueba de cifrado": intenta cifrar un archivo de prueba. Si al abrir el archivo resultante salen símbolos raros, es que ha funcionado bien.
=======

1. Descripción del proyecto
Trabajo hecho por: Anna Gual Poblet, Lena Boajram Makarem, Andrea Olivas Vazquez, Lucas Delas De Esteban y Pol Latorre Cañisà. 
En este Sprint (Tareas 12-23) hemos hecho lo necesario para crear claves de seguridad y encriptar archivos. El problema que resolvemos es coger archivos y convertirlos a formato cifrado para que nadie los pueda leer sin permiso.

2. Requisitos de sistema y dependencias
Para que funcione nuestro código, aparte de tener Python, hay que instalar la librería de criptografía. Es lo único externo que hemos usado para que la seguridad con Fernet vaya bien. Si no tienes esto instalado, el programa no arrancará porque le faltarán herramientas.

3. Pasos de instalación (dev)
Simplemente descarga los archivos del proyecto. Luego, abre la consola y escribe el comando: pip install cryptography. No hay que hacer nada más complicado, solo asegúrate de tener todos los .py en la misma carpeta para que se encuentren entre ellos.

4. Instrucciones detalladas de uso
Para probarlo, ejecuta el menú (main.py o interfaz.py). Lo primero es la "Prueba de la clave": dale a generar y debería aparecer el archivo key.key en la carpeta; sin esto no se puede hacer nada. Luego haz la "Prueba de cifrado": intenta cifrar un archivo de prueba. Si al abrir el archivo resultante salen símbolos raros, es que ha funcionado bien.

>>>>>>> lucasdelas610/Develop
5. Breve descripción de la estructura del código
Hemos separado el código en partes. En key_manager.py el programa aprende a generar y guardar la clave segura. En crypto_utils.py está la lógica para encriptar y desencriptar. En main.py y menu.py hemos puesto validaciones para que el programa no falle si falta la clave o el archivo.
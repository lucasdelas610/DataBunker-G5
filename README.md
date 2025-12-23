# DataBunker-AA5

Trabajo hecho por:

Anna Gual Poblet 
Lena Boajram Makarem 
Andrea Olivas Vazquez 
Lucas Delas De Esteban 
Pol Latorre Cañisà

Sprint: Claves y Cifrado (Tareas 12-23) En esta parte del trabajo hemos hecho lo necesario para crear la clave de seguridad y encriptar los archivos.

Qué hemos hecho Crear la clave: El programa ya sabe generar una clave segura usando Fernet.

Guardar la clave: La clave se guarda en un archivo llamado key.key. Sin esto no se puede hacer nada.

Encriptar: Ya podemos coger los archivos y convertirlos a formato cifrado para que no se puedan leer.

Validaciones: Hemos puesto comprobaciones para que no falle si falta la clave o el archivo.

Qué necesitas instalar Para que funcione nuestro código, hay que instalar la librería de criptografía:

pip install cryptography Cómo probarlo Hemos hecho unos scripts para ver si funciona todo bien:

Prueba de la clave: Ejecuta la función de generar clave. Debería aparecer el archivo key.key en la carpeta.

<<<<<<< HEAD
Prueba de cifrado: Intenta cifrar un archivo de prueba. Si al abrir el archivo resultante salen símbolos raros, es que ha funcionado bien.
=======
Prueba de cifrado: Intenta cifrar un archivo de prueba. Si al abrir el archivo resultante salen símbolos raros, es que ha funcionado bien.
>>>>>>> origin/main

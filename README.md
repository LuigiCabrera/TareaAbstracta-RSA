# TareaAbstracta-RSA

RSA Key Generator.py:

  Este archivo permite generar pares de claves (publica y privada) junto con un modulo aleatorio. 
  Para la generacion de primos aleatorios se usa el algoritmo Sieve of Eratosthenes. Rango = [7, 2^20]
  Este almacena aproximadamente 82 mil primos en tiempo de ejecucion, de ser necesario se puede bajar este limite en la linea 52

attack1_general.py:
  Este programa recie como input la clave publica e, el modulo n y el mensaje encriptado c. Intenta 3 tipos de ataques. El primero si m^e < n. El segundo si m^e mod n = m.
  El tercero (Solo si n es pequeño o facil de factorizar) encuentra los factores p y q que componene a n para hallar euler(n) y encontrar la llave privada
  Se hace uso de una base de datos de primos generada nuevamente por el algorithmo Sieve of Eratosthenes Rango = [2, 2^20]. 
  La idea es aprovechar dichos primos para factorizar de la manera mas eficiente m.
  find_factors es un algoritmo recursivo que encuentra todos los factores de un numero, siempre y cuando estos factores esten en el rango de la base de datos de primos (2^20).
  Nuevamente, en la linea 89 puede modificar el rango de la base de datos, si es muy pequeña quiza no pueda factorizar el n del ejercicio 2a. 
  Si es demasiado grande podria consumir una cantidad de memoria peligrosa.
  

attack2_SimilarMessages.py;

  Este archivo contiene el algoritmo para realizar "Similar Messages attack" Ingresando e1, e2, c1, c2 y n comprueba y decifra el mensaje m
  Solo capaz de decifrar si e1 y e2 son coprimos y c2 y n tambien.
  

  
    



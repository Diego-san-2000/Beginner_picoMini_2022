# fixme2.py
![Descripcion del CTF](img/description.png)

## Descripción
Fix the syntax error in the Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/4/fixme2.py)

## Resolucion
Descargamos el archivo y lo ejecutamos con el siguiente comando.

```
python3 fixme2.py
```

![Consola](img/console1.png)

Esta vez se trata de un error de asignación. Al estar en un if, el programa espera una comparación entre dos variables (==), pero tenemos una asignación (=). Abrimos codium para arreglar el error:

```
codium fixme2.py
```

Y modificamos la línea 22:

![VSCodium](img/codium.png)

Ahora al ejecutar el comando no dará ningún error:

![Consola](img/console2.png)

Y obtendremos la flag: 'picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}'
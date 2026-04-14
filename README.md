# Python Sandbox

Repositorio de práctica de buenas practicas de Python.

## Contenido

- `main.ipynb`: cuaderno con apuntes y ejercicios de buenas prácticas en Python.
- `test_asyncio.py`: ejemplo de ejecución concurrente con `asyncio.gather`.
- `multi 1.py`: ejemplo de paralelismo con `multiprocessing.Process`.
- `multi 2.py`: ejemplo de paralelismo con `multiprocessing.Pool` y `map`.

## Requisitos

- Python 3 instalado.
- Entorno virtual local.

Creación de entorno

``` bash
python -m venv mi_entorno
source mi_entorno/bin/activate
```

## Ejecución rápida

Usando el entorno virtual del repo:

```bash
python "test_asyncio.py"
python "multi 1.py"
python "multi 2.py"
```

Con el intérprete del sistema:

```bash
python3 "test_asyncio.py"
python3 "multi 1.py"
python3 "multi 2.py"
```

> Nota: los archivos `multi 1.py` y `multi 2.py` tienen espacios en el nombre; ejecuta siempre con comillas.

## Estado del proyecto

Este repositorio es un sandbox educativo.

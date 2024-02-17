# Plant Disease
Deteccion de enfermedades en hojas de la papa

## Tecnologias

- Python 3.11
- VirtualEnv
- Jupypter Notebook

## Instalacion

1. Clonar el repositorio

```bash
git clone https://github.com/JCarlosSL/plant_disease.git
```

2. Crear un entorno virtual
    
```bash
python -m venv venv
```
3. Activar el entorno virtual

```bash
source venv/bin/activate
```

4. Instalar las dependencias
    
```bash
pip install -r requirements.txt
```

## Uso

1. Necesitamos Descargar el dataset de [Kaggle](https://www.kaggle.com/abdallahalidev/plantvillage-dataset) y descomprimirlo en la carpeta data

2. Ejecutar el script remove_background.py para eliminar el fondo de las imagenes

```bash
python remove_background.py
```

3. Ejecutar el script augmentation.py para aumentar el dataset
    
```bash
python augmentation.py
```

4. Dividir el dataset en train, validation y test
    
```bash
python split_dataset.py
```

# Reportes Wandb

Los reportes generados se encuentran en la carpeta documents

- Accuracy y loss de los modelos [Reporte 1](documents/report1.pdf)
- Comparacion con los modelos de DL [Reporte 2](documents/report2.pdf)
# **Proyecto ETL Kaggle**

# Explicacion de los datos

# Explciacion de la estructura de carpetas

## App

## Datos

# Explicacion del codigo

# common.env o contrasennas
Las contrasennas se pasaran por keybase.

# Ejecucion
**Comando para ejecutar el proyecto**  
`docker-compose up --build `

# Ejecucion en vscode
**Instalar dev containers**  
Installar las extensiones de vscode: dev containers, ssh remote
  

**Abrir la terminal de vscode**  
`ctrl + shit + p`
  

## Existe devcontainer.json
**Ejecutar si ya existe .devcontainer/devcontainer.json**  
`Dev containers: Rebuild and open in container`
  

## No existe devcontainer.json
  
### Agregar files de configuracion de Docker Compose  
`Dev containers: Add dev container configuration files`  
**Seleccionar**: `From 'docker-compose.yml'` que es el que creamos.    
**Seleccionar**: `app` que es el contenedor que utilizaremos para development.     
El contenedor `db` es el que contiene la base de datos, pero como tal no usaremos codigo/envs de ahi.    
  
### Configurar github
**Modificar**:  
`.devcontainer/devcontainer.json` para agregar nuestras credenciales de github.  
Puedes hacer commits desde vscode y su terminal, pero el push debe hacerse desde una terminal local (no en el contenedor)    
    
  
### Instalar las extensiones que deseamos
Despues a cada extension podemos darle click derecho, agregar a `dev_environmnet.yml` para que cada vez que lo ejecutemos esten instaladas.  
  

## Dudas y tutorial
`Dev containers: get started with dev containers`
  

# Fuentes de datos/referencias
https://www.kaggle.com/datasets/yasirabdaali/kaggle-user-rankings-dataset?select=kaggle+discussions.csv 
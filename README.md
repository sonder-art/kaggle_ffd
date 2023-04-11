# **Proyecto ETL Kaggle**

# Explicacion de los datos

# Explciacion de la estructura de carpetas

## App

## Datos

# Explicacion del codigo

# common.env o contrasennas
Las contrasennas se pasaran por keybase.  
No olvides cambiar el sample_env.env a common.env

# Ejecucion
**Comando para ejecutar el proyecto**  
`docker-compose up --build `

# Ejecucion en vscode
Video: https://www.youtube.com/watch?v=SDa3v4Quj7Y 
En nuestro caso ya contamos con los devvontainer.json para el proyecto. Ese es el que vamos a utilizar.  
No tienen que crearlo desde cero, **pero si tienen que modificarlo**. En estricto sentido, no deberia de estar ese archivo,
pero para simplificar su uso lo hemos dejado.

## **Instalar dev containers**  
Instalar las extensiones de vscode: dev containers, ssh remote en caso de no tenerlas. (Ver video)

## **Modificar devcontainer.json**

### **Configurar github**
**Modificar**:  
`.devcontainer/devcontainer.json` para agregar nuestras credenciales de github.  
Puedes hacer commits desde vscode y su terminal, pero el push debe hacerse desde una terminal local (no en el contenedor)   
**Github Credentials:** Cambien la linea "postCreateCommand":" git config --global user.name uumami && git config --global user.email vazcorm@gmail.com" a su configuracion de github y listo.  
   
      
### **Instalar/Agregar las extensiones que deseamos**
Despues a cada extension podemos darle click derecho, agregar a `dev_environmnet.yml` para que cada vez que lo ejecutemos esten instaladas.  

## **Lanzar el environment**
**Abrir la terminal de vscode**  
`ctrl + shit + p`

**Ejecutar este comando si ya modificaste .devcontainer/devcontainer.json**   
`Dev containers: Rebuild and open in container`      

## **En caso de no existe devcontainer.json**
  
### Agregar files de configuracion de Docker Compose  
**Ejecutar**:`ctrl + shit + p`
**Seleccionar**:`Dev containers: Add dev container configuration files`  
**Seleccionar**: `From 'docker-compose.yml'` que es el que creamos.    
**Seleccionar**: `app` que es el contenedor que utilizaremos para development.     
El contenedor `db` es el que contiene la base de datos, pero como tal no usaremos codigo/envs de ahi.   
  

# Fuentes de datos/referencias
https://www.kaggle.com/datasets/yasirabdaali/kaggle-user-rankings-dataset?select=kaggle+discussions.csv 
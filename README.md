# Cloud_P0
Proyecto de nivelación 0

## Video
https://youtu.be/rmlwciDaIII

## Documentación del API :D
https://documenter.getpostman.com/view/12814750/2sA2r3Z6EB

## Docker Hub
### Front 
https://hub.docker.com/repository/docker/cat09/front/general
### Back 
https://hub.docker.com/repository/docker/cat09/back/general


## Instrucciones de uso :) 

1. Desde power shell ejecutar:
   ```shell
   docker run --name back -p 8000:8000 -e -d cat09/back:1.0
   ```
3. En otra pestaña de power Shell, ejecutar:
   ```shell
   docker run --name front -p 3000:3000 -e -d cat09/front:1.0
   ```
   (En esta parte aparecen warnings, la app se ejecuta correctamente 👍)
4. Abrir http://localhost:3000/
5. Enjoy 

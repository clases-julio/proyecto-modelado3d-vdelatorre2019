# proyecto-modelado3d-vdelatorre2019

## Día 1 


## Descripción

Este es un modelo de robot parecido al Scara solo que su end effector está compuesto por 4 pinzas capaces de coger objetos y está montado sobre ruedas.

En primer lugar, diseñamos las 4 ruedas con sus dos ejes que las conectan entre
sí, muy parecido a lo que ya hicimos en la práctica 2.


![ejes_ruedas](https://user-images.githubusercontent.com/90764556/158598384-8d95d7e5-850d-4d81-9368-339c2bd98cf5.png)



Después añadimos los 4 soportes que se encargarán de soportar el peso de la base de nuestro robot articulado. 


![ejes_base](https://user-images.githubusercontent.com/90764556/158598516-5aeb85d8-b44d-41b4-944b-3b8ffa57161e.png)


Una vez añadimos la primera base, añadimos otra secundaria sobre la cual estarán montado los 2 eslabones.


![base_robot](https://user-images.githubusercontent.com/90764556/158598679-e1e60d8a-90a6-4a25-9807-0dfc5b37cd40.png)

Una vez tenemos nuestra base del robot montada, sobre ella estarán los eslabones unidos por una articulación que será una esfera para simular su respectivo movimiento.

![links](https://user-images.githubusercontent.com/90764556/158599168-991feeb7-69e9-4432-a7cf-24e2e9f998cb.png)


Ahora simplemente añadimos nuestro end effector que estará formado por 4 pinzas articuladas.

![end_effector](https://user-images.githubusercontent.com/90764556/158599273-1b840c89-bb1e-42e2-9979-ac70fd028e79.png)

Finalmente, renderizamos nuestro modelo de robot Scara añadiendole diferentes colores simulando una textura sobre las distintas partes independientes que componen
el robot final.

![robot_final](https://user-images.githubusercontent.com/90764556/158599725-eae817ab-0611-43c1-8872-292b2dbbdf36.png)






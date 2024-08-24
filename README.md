Función:
La aplicación permite al usuario registrar tareas con su título, descripción y estado, revisar las tareas registradas y a su vez filtrar por el estado en que se encuentran.

Proceso de creación:
Inicialmente creamos el modelo tarea dentro de la aplicación, creamos su respectivo formulario, para luego definir 2 vistas básicas, estas contienen el crearTarea y listarTareas.
En las urls definimos los paths y asignamos su vista, junto con el nombre, para luego crear los templates trabajando con el formulario en la vista crearTarea,
y con la lista de tareas en listarTareas, finalmente, realizamos la configuración del proyecto,
incluyendo nuestra aplicación en INSTALLED_APPS e incluyendo las urls de la aplicación en las urls globales.

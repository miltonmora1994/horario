GESTION DE HORARIOS ITP

En esta aplicacion usted poda:
Gestionar Espacios Academicos medinate el CRUD (Crear, Leer, Actualizar y Borrar)
Gestionar Estudiantes medinate el CRUD (Crear, Leer, Actualizar y Borrar)
Gestionar Sesiones para cada dia con sus respectivos espacios acadmicos, mediante el CRUD
Gestionar la asistencias de sus Estudiantes en sus diferentes espacios academicos, la asistencia esta
relacionada con el semestre y a la vez con los estudiantes creados para el respectio semestre.
y en ultima intancia poder listar la asistencia de aquellos que SI asistieron a cada sesion.
tambien puedes eliminar cada lista de asistencia con el fin volver a gestionar nuevamente una sesion y tomar 
asistencia de la misma para luego listar.
Nuestra aplicacion corre localmente en el puerto 3000 (localhost:3000)

La base de datos es creada en msql y por defecto corre en el puerto 3306, se debe crear la bd manual con 
el nombre flask_horarios y correr sobre ella el sql que se encuentra en la aplicacion llamado flask_horarios.sql, ahi ara la creacion de las tablas y la configuracion para cada registo.

Tener en cuenta algunos requerimiento basicos para correr la aplicacon como son flask, flask_mysql, flask_mysqulbd, aunque si correros el archivo requirements, se instalan automaticamente.

Finalmente levantamos servicios con el codigo python app.py, apuntamos en el navegador a localhost:300 y tenemos funcionando nuestra aplicacion....
....... que la disfruten....... copyright ©.
# Proyecto-SC-115

## Universidad Fidélitas

### Curso

**Programación Básica**

### Profesora

**SABORIO OVIEDO MARIA LAURA**

### Estudiantes

- **Jafeth Garro Roldán**
- **Aldo Mora Aguilar**
- **Daniel Vindas Morraz**

## Estructura del Proyecto

Este proyecto tiene la siguiente estructura:

- `.gitignore`: Este archivo se utiliza para especificar archivos o directorios que Git debe ignorar.
- `README.md`: Este archivo proporciona información sobre el proyecto.
- `src`: Esta carpeta contiene los archivos de código fuente del proyecto. En este caso, incluye el script de Python que ejecuta la funcionalidad principal de la aplicación.
- `src/main.py`: Este es el script principal de Python de la aplicación.
- `Enunciado SC-115 Proyecto Final.pdf`: Este archivo contiene el enunciado o las instrucciones para el proyecto final del curso SC-115. Incluye los requisitos, objetivos y criterios de evaluación del proyecto.
- `Portada.pdf`: Este archivo es la portada del proyecto. Incluye detalles como el título del proyecto, los nombres de los miembros del equipo, la fecha, etc.

## Acerca de la Aplicación

La aplicación es un script de Python que realiza varias operaciones relacionadas con las citas médicas. Permite a los usuarios ver médicos y pacientes, programar citas y realizar otras tareas relacionadas.

## Estructura de datos

### Medicos

Se almacenan en la variable `medicos`, la cual es una lista bidimencional, la cual almacena a todos los medicos.

Cada medico se almacena en una lista siguiendo la estructura:

| Nombre | Especialidad | Correo Electrónico | Número de Teléfono | Días de Trabajo | Horario |
| :----: | :----------: | :----------------: | :----------------: | :-------------: | :-----: |
| String |    String    |       String       |       String       |      List       | String  |
|   0    |      1       |         2          |         3          |        4        |    5    |

> ### Ejemplo de Médico
>
> - **Nombre**: Dr. John Doe
> - **Especialidad**: Odontologo
> - **Correo Electrónico**: johndoe@example.com
> - **Número de Teléfono**: 1234567890
> - **Días de Trabajo**:
>   - Lunes: Trabaja
>   - Martes: Trabaja
>   - Miércoles: Trabaja
>   - Jueves: Trabaja
>   - Viernes: Trabaja
>   - Sábado: No Trabaja
>   - Domingo: No Trabaja
> - **Horario**: Mañana
>
> ```python
> ["Dr. John Doe", "Odontologo","johndoe@example.com", "1234567890", ["Trabaja","Trabaja", "Trabaja", "Trabaja", "Trabaja", "No Trabaja", "No Trabaja"], 'm']
> ```

### Pacientes

Se almacenan en la variable `pacientes`, la cual es una lista bidimensional que almacena a todos los pacientes.

Cada paciente se almacena en una lista siguiendo la estructura:

| Nombre | Correo Electrónico | Dirección | Número de Teléfono | Médico Asignado |
| :----: | :----------------: | :-------: | :----------------: | :-------------: |
| String |       String       |  String   |       String       |     String      |
|   0    |         1          |     2     |         3          |        4        |

> ### Ejemplo de Paciente
>
> - **Nombre**: Alice Johnson
> - **Correo Electrónico**: alicejohnson@example.com
> - **Dirección**: 123 Main St
> - **Número de Teléfono**: 1234567890
> - **Médico Asignado**: Dr. John Doe
>
> ```python
> ["Alice Johnson", "alicejohnson@example.com", "123 Main St", "1234567890", "Dr. John Doe"]
> ```

### Citas Agendadas

Se almacenan en la variable `citasAgendadas`, la cual es una lista bidimensional que almacena todas las citas agendadas.

Cada cita se almacena en una lista siguiendo la estructura:

| Activo | Fechas | Paciente | Doctor | Procedimiento | Pagado | Método de Pago (opcional) |
| :----: | :----: | :------: | :----: | :-----------: | :----: | :-----------------------: |
|  Bool  | String |  String  | String |    String     |  Bool  |          String           |
|   0    |   1    |    2     |   3    |       4       |   5    |             6             |

> ### Ejemplo de Cita Sin Pagar
>
> - **Activo**: True \*Nota: Valor por defecto es siempre `True`
> - **Fechas**: 1/1 , 1/2
> - **Paciente**: Alice Johnson
> - **Doctor**: Dr. John Doe
> - **Procedimiento**: Cirugía reconstructiva de mandíbula y maxilar
> - **Pagado**: False \*Nota: Valor por defecto es siempre `False`
>
> ```python
> [True, ["1/1"], "Alice Johnson", "Dr. John Doe", "Cirugía reconstructiva de mandíbula y maxilar", False]
> ```

> ### Ejemplo de Cita Pagada
>
> - **Fecha**: 2/1
> - **Paciente**: Bob Smith
> - **Doctor**: Dr. Jane Doe
> - **Procedimiento**: Limpieza dental
> - **Pagado**: True
> - **Método de Pago**: Tarjeta débito/crédito
>
> ```python
> ["2/1", "Bob Smith", "Dr. Jane Doe", "Limpieza dental", True, "Tarjeta débito/crédito"]
> ```

### Nota

Somos conscientes de que existen formas más eficientes de almacenar y manejar la información. Sin embargo, en este proyecto solo se nos permite utilizar los conocimientos que hemos adquirido en clase.

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
| String |    String    |       String       |       String       |   List [str]    | String  |
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

| Activo |   Fechas   | Paciente | Doctor | Procedimiento | Pagado | Método de Pago (opcional) |
| :----: | :--------: | :------: | :----: | :-----------: | :----: | :-----------------------: |
|  Bool  | List [Str] |  String  | String |    String     |  Bool  |          String           |
|   0    |     1      |    2     |   3    |       4       |   5    |             6             |

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
> - **Activo**: True
> - **Fecha**: 2/1
> - **Paciente**: Bob Smith
> - **Doctor**: Dr. Jane Doe
> - **Procedimiento**: Limpieza dental
> - **Pagado**: True
> - **Método de Pago**: Tarjeta débito/crédito
>
> ```python
> [True, ["2/1"], "Bob Smith", "Dr. Jane Doe", "Limpieza dental", True, "Tarjeta débito/crédito"]
> ```

## Funciones de Pagos

#### marcarCitaPagada(index: int, metodoPago: str)

Esta función marca una cita como pagada y registra el método de pago utilizado.

- **Parámetros**:

  - `index` (int): El índice de la cita en la lista de citas agendadas.
  - `metodoPago` (str): El método de pago utilizado para pagar la cita.

- **Retorna**:
  - None

#### procesarPagos()

Esta función procesa el pago de una cita seleccionada, mostrando las opciones de pago disponibles, calculando descuentos según el método de pago, y actualizando la información de la cita en la base de datos.

- **Parámetros**:

  - Ninguno

- **Retorna**:
  - None

#### preciosTratamientos(tratamiento: str)

Esta función devuelve el precio de un tratamiento específico.

- **Parámetros**:

  - `tratamiento` (str): El nombre del tratamiento.

- **Retorna**:
  - int: El precio del tratamiento.

#### descuento_segun_MetodoPago(metodo: str)

Esta función calcula el descuento aplicable según el método de pago.

- **Parámetros**:

  - `metodo` (str): El método de pago utilizado.

- **Retorna**:
  - float: El porcentaje de descuento.

#### getNombreMetodoPago(metodo: int)

Esta función devuelve el nombre del método de pago basado en un número de identificación del método.

- **Parámetros**:

  - `metodo` (int): El número que identifica el método de pago.

- **Retorna**:
  - str: El nombre del método de pago.

#### calcularPrecioFinal(precioNeto: float, descuento: float)

Esta función calcula el precio final de un tratamiento después de aplicar el descuento.

- **Parámetros**:

  - `precioNeto` (float): El precio base del tratamiento.
  - `descuento` (float): El descuento a aplicar.

- **Retorna**:
  - float: El precio final después del descuento.

#### generarFactura()

Esta función genera una factura detallada para una cita pagada, incluyendo todos los detalles relevantes como el nombre del paciente, el tratamiento, el precio, los descuentos aplicados, y el total general.

- **Parámetros**:

  - Ninguno

- **Retorna**:
  - None

## Sección de Reportes

### Reportes Generales

#### `mostrarReportes()`

Esta función muestra un menú con opciones de reportes disponibles como citas, pacientes, médicos, y tratamientos. La función permite la selección de un reporte específico para visualización y sigue en ejecución hasta que el usuario elija regresar al menú principal.

**Parámetros:**

- Ninguno

**Retorna:**

- `None`

#### `mostrarCambiosDeHorarioCita(cita: list)`

Esta función muestra los cambios de horario de una cita específica. Devuelve un string que contiene todos los cambios de horario si existen, o un mensaje indicando que no hay cambios.

**Parámetros:**

- `cita` (list): Información de la cita, incluyendo cambios de horario.

**Retorna:**

- `String`: Informe de los cambios de horario o un mensaje indicativo de la ausencia de cambios.

### Reportes Específicos

#### `generarReporteCitas()`

Genera un reporte de todas las citas agendadas, incluyendo estado de la cita, detalles relevantes y cambios de horario. Este reporte se muestra en consola y se guarda en el archivo `reporteCitas.txt`.

**Parámetros:**

- Ninguno

**Retorna:**

- `None`

#### `generarReportePacientes()`

Genera un reporte de los pacientes registrados, mostrando información detallada como nombre, correo, dirección, y teléfono. El reporte se muestra en pantalla y se guarda en el archivo `reportePacientes.txt`. La función espera que el usuario presione enter para continuar antes de cerrar.

**Parámetros:**

- Ninguno

**Retorna:**

- `None`

#### `generarReporteMedicos()`

Genera un reporte de todos los médicos registrados, mostrando información como nombre, especialidad, correo, teléfono, días y horarios de trabajo. Este reporte se visualiza en consola y se guarda en `reporteMedicos.txt`. La función también pausa para que el usuario pueda presionar enter para continuar.

**Parámetros:**

- Ninguno

**Retorna:**

- `None`

#### `generarReporteTratamientos()`

Genera un reporte de todos los tratamientos disponibles con sus respectivos precios, y lo guarda en el archivo `reporteTratamientos.txt`. Además, imprime el reporte en consola para su visualización inmediata.

**Parámetros:**

- Ninguno

**Retorna:**

- `String`: Contenido del reporte de tratamientos.

## Funciones para gestionar la información

### Funciones de Médicos

#### [guardarMedico(medico: list)](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L168)

Esta función guarda un médico en el archivo `medicos.txt`.

- **Parámetros**:

  - `medico` (list): Lista que contiene la información del médico a guardar.

- **Retorna**:
  - None

#### [leerMedicos()](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L188)

Esta función lee los médicos registrados en el archivo `medicos.txt` y los almacena en la lista `medicos`.

- **Parámetros**:

  - Ninguno

- **Retorna**:
  - None

### Funciones de Pacientes

#### [guardarPaciente(paciente: list)](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L319)

Esta función guarda un paciente en el archivo `pacientes.txt`.

- **Parámetros**:

  - `paciente` (list): Lista que contiene la información del paciente a guardar.

- **Retorna**:
  - None

#### [leerPacientes()](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L335)

Esta función lee los pacientes registrados en el archivo `pacientes.txt` y los almacena en la lista `pacientes`.

- **Parámetros**:

  - Ninguno

- **Retorna**:
  - None

### Funciones de Citas

#### [guardarCita(cita: list)](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L574)

Esta función guarda una cita en el archivo `citas.txt`.

- **Parámetros**:

  - `cita` (list): Lista que contiene la información de la cita a guardar.

- **Retorna**:
  - None

#### [leerCitas()](https://github.com/IAmJafeth/Proyecto-SC-115/blob/main/src/main.py?plain=1#L597)

Esta función lee las citas registradas en el archivo `citas.txt` y las almacena en la lista `citasAgendadas`.

- **Parámetros**:

  - Ninguno

- **Retorna**:
  - None

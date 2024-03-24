presetación = """
    PROYECTO FINAL - Grupo #5

Curso:          Programación Básica

Profesora:      SABORIO OVIEDO MARIA LAURA

Estudiantes:    Jafeth Garro Roldán
                Daniela Elena Gómez Mora
                Aldo Mora Aguilar
                Daniel Vindas Morraz

"""

# * FUNCIONES MEDICOS---------------------------------------------------------------------------------------------------------------------------


def getNombreDiaTrabajo(index):
    """
    Retorna el nombre del día de la semana correspondiente al índice dado.

    Parámetros:
    - index (int): El índice del día de la semana (0 para Lunes, 1 para Martes, etc.)

    Retorna:
    - str: El nombre del día de la semana correspondiente al índice dado.
    """
    if index == 0:
        return "Lunes"
    if index == 1:
        return "Martes"
    if index == 2:
        return "Miércoles"
    if index == 3:
        return "Jueves"
    if index == 4:
        return "Viernes"
    if index == 5:
        return "Sábado"
    if index == 6:
        return "Domingo"


def crearSemanaDeTrabajo():
    """
    Crea una lista que representa los días de trabajo de un médico.

    Returns:
    - dias (list): Lista que representa los días de trabajo del médico. Cada elemento de la lista indica si el médico trabaja o no en ese día.
    """
    dias = ["No Trabaja"] * 7

    while True:
        print("\n\t\tSeleccione los días de trabajo del médico")
        print(f"\t1- Lunes ({dias[0]})")
        print(f"\t2- Martes ({dias[1]})")
        print(f"\t3- Miércoles ({dias[2]})")
        print(f"\t4- Jueves ({dias[3]})")
        print(f"\t5- Viernes ({dias[4]})")
        print(f"\t6- Sábado ({dias[5]})")
        print(f"\t7- Domingo ({dias[6]})")
        print("\n\t8- Finalizar selección")

        dia = int(input("\nSeleccione un día: "))

        if dia == 8:
            break

        if dia < 1 or dia > 7:
            print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")
            continue

        dias[dia - 1] = "Trabaja"

    return dias


def formatSemanaDeTrabajo(dias):
    """
    Formatea los días de trabajo de la semana.

    Args:
        dias (list): Una lista de strings que representa los días de la semana.

    Returns:
        str: Una cadena formateada con los días de trabajo separados por coma.
    """
    semana = ""
    for i in range(len(dias)):
        if dias[i] == "Trabaja":
            semana += getNombreDiaTrabajo(i) + ", "
    return semana


def mostrarMedico(medico):
    """
    Muestra la información de un médico en la consola.

    Parámetros:
    - medico: una lista que contiene la información del médico en el siguiente orden:
        - Nombre del médico (str)
        - Especialidad del médico (str)
        - Correo del médico (str)
        - Teléfono del médico (str)
        - Días de trabajo del médico (list)
        - Horario del médico ('m' para mañana, 't' para tarde)

    Retorna:
    None
    """
    print(f"Nombre: {medico[0]}")
    print(f"Especialidad: {medico[1]}")
    print(f"Correo: {medico[2]}")
    print(f"Teléfono: {medico[3]}")
    print(f"Días de trabajo: {formatSemanaDeTrabajo(medico[4])}")
    print(f"Horario: {'Mañana' if medico[5] == 'm' else 'Tarde'}\n")


def crearMedico():
    """
    Función que permite al usuario ingresar la información de un médico y agregarlo a la lista de médicos.

    Parámetros:
    - No recibe ningún parámetro.

    Retorna:
    - No retorna ningún valor.
    """
    medico = []
    print("\n\tEstimado(a) usuario ingrese la siguiente información\n")
    medico.append(input("Nombre completo del médico: "))
    medico.append(input("Especialidad del médico: "))
    medico.append(input("Correo electrónico del médico: "))
    medico.append(input("Número telefónico del médico: "))
    medico.append(crearSemanaDeTrabajo())

    while True:
        horario = input(
            "\tIngrese \"m\" si el médico trabaja en la mañana o \"t\" si el médico trabaja en la tarde: ").strip().lower()
        if horario == "m" or horario == "t":
            break
        print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")
    medico.append(horario)
    medicos.append(medico)

    print("\n\tMédico agregado exitosamente\n")
    mostrarMedico(medico)
    input("\nPresione enter para continuar...")


def mostrarTodosMedicos():
    """
    Muestra la información de los médicos registrados.

    Si no hay médicos registrados, se muestra un mensaje indicando que no hay médicos.
    Si hay médicos registrados, se muestra la información de cada médico, incluyendo su nombre, especialidad, correo, teléfono, días de trabajo y horario.
    """
    if len(medicos) == 0:
        print("\n\tNo hay médicos registrados\n")
        input("\nPresione enter para continuar...")
        return

    print("\n\tMédicos registrados\n")
    for medico in medicos:
        mostrarMedico(medico)

    input("\nPresione enter para continuar...")

# * FUNCIONES PACIENTES---------------------------------------------------------------------------------------------------------------------------


def asignarMedico():
    """
    Función que permite al usuario seleccionar un médico de una lista de médicos registrados.

    Parámetros:
    - Ninguno

    Retorna:
    - medico (list): Una lista que contiene la información del médico seleccionado en el siguiente orden:
        - Nombre del médico (str)
        - Especialidad del médico (str)
        - Correo del médico (str)
        - Teléfono del médico (str)
        - Días de trabajo del médico (list)
        - Horario del médico ('m' para mañana, 't' para tarde)
    """
    print("\n\tSeleccione un médico de la lista\n")
    for i in range(len(medicos)):
        print(f"\t{i+1}- {medicos[i][0]} ({medicos[i][1]})")

    while True:
        index = int(input("\nSeleccione un médico: ")) - 1

        if index < 0 or index >= len(medicos):
            print("Opción incorrecta, intente de nuevo")
            continue

        break

    return medicos[index]


def crearPaciente():
    """ 
    Función que crea un nuevo paciente y lo agrega a la lista de pacientes.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    if len(medicos) == 0:
        print("\n\tNo hay médicos registrados\n")
        print("\tPor favor registre un médico antes de agregar un paciente\n")
        input("\nPresione enter para continuar...")
        return

    paciente = []
    print("\n\tEstimado(a) usuario ingrese la siguiente información\n")
    paciente.append(input("Nombre del paciente: "))
    paciente.append(input("Correo electrónico del paciente: "))
    paciente.append(input("Dirección del paciente: "))
    paciente.append(input("Número telefónico del paciente: "))
    paciente.append(asignarMedico()[0])
    pacientes.append(paciente)
    mostrarPaciente(paciente)
    input("\nPresione enter para continuar...")


def mostrarPaciente(paciente):
    """
    Muestra la información de un paciente.

    Args:
        paciente (list): Una lista que contiene la información del paciente en el siguiente orden:
            - Nombre del paciente (str)
            - Correo electrónico del paciente (str)
            - Dirección del paciente (str)
            - Teléfono del paciente (str)
            - Médico tratante del paciente (str)
    """
    print(f"Nombre: {paciente[0]}")
    print(f"Correo: {paciente[1]}")
    print(f"Dirección: {paciente[2]}")
    print(f"Teléfono: {paciente[3]}")
    print(f"Médico tratante: {paciente[4]}\n")


def mostrarTodosPacientes():
    """
    Muestra la información de los pacientes registrados.

    Si no hay pacientes registrados, se muestra un mensaje indicando que no hay pacientes.
    Si hay pacientes registrados, se muestra la información de cada paciente, incluyendo su nombre, correo, dirección, teléfono y médico tratante.
    """
    if len(pacientes) == 0:
        print("\n\tNo hay pacientes registrados\n")
        input("\nPresione enter para continuar...")
        return

    print("\n\t\tPacientes registrados\n")

    for i in range(len(pacientes)):
        print(f"\n\tPaciente {i+1}")
        mostrarPaciente(pacientes[i])

    input("\nPresione enter para continuar...")


def registrarCita():
    # TODO: Avance 2 Módulo de Citas y Cancelación de Citas - Registro de cita:
    # ! Owner: Jafeth Garro
    """
    solicitar el día de la cita en cual se debe validar la disponibilidad de los horarios, médicos 
    según la especialidad y tratamiento del paciente para agendar dicha cita. 
    """


def cancelarCita():
    # TODO: Módulo de Citas y Cancelación de Citas - Cancelación y/o reprogramación de cita
    # ! Owner: Aldo Mora
    """
    en caso de aplicar para una cancelación de cita programada 
    debe solicitar el día que tenía la cita agendada, y debe dar opción a que le permita reprogramar dicha cita 
    a nuevo horario disponible según el tratamiento y medico a aplicar.
    """


def procesarPagos():
    # TODO: Avance 2 Módulo de Pagos - Formas  de  Pago
    # ! Owner: Daniel Vindas
    """
    Se  debe  registrar  la  forma  de  pago  según  los  tratamientos  solicitados,  aquí  se 
    manejarían las formas de pago en efectivo, transferencia sinpe, tarjeta de crédito o débito; adicional de un 
    grupo de descuentos según el tratamiento que usted con su equipo defina como parte de su programa.
    """


def generarFactura():
    # TODO: Avance 2 Módulo de Pagos - Facturación
    # ! Owner: Elena Gomez
    """
    Se realiza la gestión de la factura, donde debe tomar en consideración la generación de un 
    documento que simule una factura al paciente. Tome en consideración que debe llevar el siguiente detalle: 
    Clínica  de  atención,  Especialidad,  Moneda,  Nombre  del  Paciente,  Servicio,  Cantidad,  Precio,  Detalle, 
    Subtotal, Descuento, IVA, Total General.
    """


# * VARIABLES --------------------------------------------------------------------------------------------------------------------------------
# 'medicos' es una lista que almacena la información de todos los médicos. Cada médico se representa como una lista de sus detalles.
medicos = []

# 'pacientes' es una lista que almacena la información de todos los pacientes. Cada paciente se representa como una lista de sus detalles.
pacientes = []

# 'citas' es una lista que almacena la información de todas las citas. Cada cita se representa como una lista de sus detalles.
citas = []

# * PROGRAMA PRINCIPAL ------------------------------------------------------------------------------------------------------------------------


print(presetación)

while True:

    # Mostraremos el menú principal:
    print("\n\t\tMENÚ PRINCIPAL")
    print("\t1- Módulo de expedientes")
    print("\t2- Módulo de citas y cancelación de citas")
    print("\t3- Módulo de pagos")
    print("\t4- Módulo de reportes")
    print("\t5- Salir")

    # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
    menu_option = input("\nSeleccione una opcion: ")

    if menu_option == "1":  # ! Módulo de Expedientes -----------------------------------------------------------------------------

        while True:
            # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
            # Mostraremos el menú del Módulo de Expedientes:
            print("\n\t\t\tMODULO DE EXPEDIENTES ")
            print("\t\t1- Agregar médico")
            print("\t\t2- Agregar pacientes")
            print("\t\t3- Ver médicos")
            print("\t\t4- Ver pacientes")
            print("\t\t5- Regresar al MENÚ PRINCIPAL")

            menu_option = input("\n\tSeleccione una opcion: ")

            if menu_option == "1":
                # Si el usuario elige agregar un médico
                crearMedico()

            elif menu_option == "2":

                # Si el usuario elige agregar un paciente nuevo
                crearPaciente()

            elif menu_option == "3":
                # Lista de médicos
                print(
                    "A continuación se muestran los médicos del consultorio dental:\n")
                mostrarTodosMedicos()

            elif menu_option == "4":
                # Lista de pacientes ya registrados
                print(
                    "A continuación se muestran los pacientes del consultorio dental:\n")
                mostrarTodosPacientes()

            elif menu_option == "5":
                # Si el usuario elige regresar al menú principal
                break

            else:
                # Si el usuario elige una opción incorrecta
                print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

    elif menu_option == "2":  # ! Módulo de Citas y Cancelación de Citas ----------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")
        # TODO: Agregar funcionalidad de Módulo de Citas y Cancelación de Citas
        # !: Owners: Jafeth Garro y Aldo Mora

    elif menu_option == "3":  # ! Módulo de Pagos ----------------------------------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")
        # TODO: Agregar funcionalidad de Módulo de Citas y Cancelación de Citas
        # !: Owners: Daniel Vindas y Elena Gomez

    elif menu_option == "4":  # ! Módulo de Reportes -------------------------------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "5":  # ! Salir del programa -------------------------------------------------------------------------------
        print("\n -- CERRANDO PROGRAMA -- \n")
        break

    else:  # ! Opción incorrecta
        print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

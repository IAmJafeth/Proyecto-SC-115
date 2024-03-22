presetación = """
    PROYECTO FINAL - Grupo #5

Curso:          Programación Básica

Profesora:      SABORIO OVIEDO MARIA LAURA

Estudiantes:    Jafeth Garro Roldán
                Daniela Elena Gómez Mora
                Aldo Mora Aguilar
                Daniel Vindas Morraz

"""
# * FUNCIONES----------------------------------------------------------------------------------------------------------------------------


def crearMedico():
    """
    Función que permite al usuario ingresar la información de un médico y agregarlo a la lista de médicos.

    Parámetros:
    - No recibe ningún parámetro.

    Retorna:
    - No retorna ningún valor.
    """
    medico = []
    print("\n\t\tEstimado(a) usuario ingrese la siguiente información\n")
    medico.append(input("\tNombre completo del médico: "))
    medico.append(input("\tEspecialidad del médico: "))
    medico.append(input("\tCorreo electrónico del médico: "))
    medico.append(input("\tNúmero telefónico del médico: "))
    medico.append(
        input("\tDías de trabajo del médico en el siguiente formato día/día/+...: "))
    while True:
        horario = input(
            "\tIngrese \"m\" si el médico trabaja en la mañana o \"t\" si el médico trabaja en la tarde: ").strip().lower()
        if horario == "m" or horario == "t":
            break
        print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")
    medico.append(horario)
    medicos.append(medico)


def crearPaciente():
    """
    Función que crea un nuevo paciente y lo agrega a la lista de pacientes.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    paciente = []
    print("\n\t\tEstimado(a) usuario ingrese la siguiente información\n")
    paciente.append(input("\tNombre del paciente: "))
    paciente.append(input("\tCorreo electrónico del paciente: "))
    paciente.append(input("\tDirección del paciente: "))
    paciente.append(input("\tNúmero telefónico del paciente: "))
    paciente.append(input("\tNombre del médico asignado: "))
    pacientes.append(paciente)


def mostrarMedicos():
    """
    Muestra la información de los médicos registrados.

    Si no hay médicos registrados, se muestra un mensaje indicando que no hay médicos.
    Si hay médicos registrados, se muestra la información de cada médico, incluyendo su nombre, especialidad, correo, teléfono, días de trabajo y horario.
    """
    if len(medicos) == 0:
        print("\n\tNo hay médicos registrados\n")
        return

    print("\n\t\tMédicos registrados\n")
    for medico in medicos:
        print(f"\tNombre: {medico[0]}")
        print(f"\tEspecialidad: {medico[1]}")
        print(f"\tCorreo: {medico[2]}")
        print(f"\tTeléfono: {medico[3]}")
        print(f"\tDías de trabajo: {medico[4]}")
        print(f"\tHorario: {'Mañana' if medico[5] == 'm' else 'Tarde'}")
        print("\n")


def mostrarPacientes():
    """
    Muestra la información de los pacientes registrados.

    Si no hay pacientes registrados, se muestra un mensaje indicando que no hay pacientes.
    Si hay pacientes registrados, se muestra la información de cada paciente, incluyendo su nombre, correo, dirección, teléfono y médico tratante.
    """
    if len(pacientes) == 0:
        print("\n\tNo hay pacientes registrados\n")
        return

    print("\n\t\tPacientes registrados\n")
    for paciente in pacientes:
        print(f"\tNombre: {paciente[0]}")
        print(f"\tCorreo: {paciente[1]}")
        print(f"\tDirección: {paciente[2]}")
        print(f"\tTeléfono: {paciente[3]}")
        print(f"\tMédico tratante: {paciente[4]}")
        print("\n")


# * VARIABLES --------------------------------------------------------------------------------------------------------------------------------
# 'medicos' es una lista que almacena la información de todos los médicos. Cada médico se representa como una lista de sus detalles.
medicos = []

# 'pacientes' es una lista que almacena la información de todos los pacientes. Cada paciente se representa como una lista de sus detalles.
pacientes = []


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
                mostrarMedicos()

            elif menu_option == "4":
                # Lista de pacientes ya registrados
                print(
                    "A continuación se muestran los pacientes del consultorio dental:\n")
                mostrarPacientes()

            elif menu_option == "5":
                # Si el usuario elige regresar al menú principal
                break

            else:
                # Si el usuario elige una opción incorrecta
                print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

    elif menu_option == "2":  # ! Módulo de Citas y Cancelación de Citas ----------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "3":  # ! Módulo de Pagos ----------------------------------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "4":  # ! Módulo de Reportes -------------------------------------------------------------------------------
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "5":  # ! Salir del programa -------------------------------------------------------------------------------
        print("\n -- CERRANDO PROGRAMA -- \n")
        break

    else:  # ! Opción incorrecta
        print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

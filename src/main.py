presentacion = """
    PROYECTO FINAL - Grupo #5

Curso:          Programación Básica

Profesora:      SABORIO OVIEDO MARIA LAURA

Estudiantes:    Jafeth Garro Roldán
                Aldo Mora Aguilar
                Daniel Vindas Morraz

"""
#region Medicos
# * FUNCIONES MEDICOS---------------------------------------------------------------------------------------------------------------------------


def getNombreDia(index):
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


def getNombreHorario(horario):
    """
    Retorna el nombre del horario según el código proporcionado.

    Parámetros:
    - horario (str): El código del horario. Puede ser "m" para mañana o "t" para tarde.

    Retorna:
    - str: El nombre del horario correspondiente al código proporcionado. Puede ser "Mañana" o "Tarde".
    """
    return "Mañana" if horario == "m" else "Tarde"


def crearSemanaDeTrabajo():
    """
    Crea una lista que representa los días de trabajo de un médico.

    Returns:
    - dias (list): Lista que representa los días de trabajo del médico. Cada elemento de la lista indica si el médico trabaja o no en ese día.
    """
    dias = ["No Trabaja"] * 7

    while True:
        print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
        print("│      **Seleccione los días de trabajo del médico**  │")
        print("├─────────────────────────────────────────────────────┤")
        print(f"│ /// 1- Lunes ({dias[0]})                           ")
        print(f"│ /// 2- Martes ({dias[1]})                          ")
        print(f"│ /// 3- Miércoles ({dias[2]})                       ")
        print(f"│ /// 4- Jueves ({dias[3]})                          ")
        print(f"│ /// 5- Viernes ({dias[4]})                         ")
        print(f"│ /// 6- Sábado ({dias[5]})                          ")
        print(f"│ /// 7- Domingo ({dias[6]})                         ")
        print("├─────────────────────────────────────────────────────┤")
        print("│ /// 8- Finalizar selección                          │")
        print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

        dia = int(input("\nSeleccione un día: "))

        if dia == 8:
            break

        if dia < 1 or dia > 7:
            print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
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
            semana += getNombreDia(i) + ", "
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
    print(f"Horario: {getNombreHorario(medico[5])}\n")


def seleccionarEspecialidadMedico():
    """
    Permite al usuario seleccionar una especialidad de médico de una lista de especialidades.

    Returns:
        str: La especialidad de médico seleccionada.
    """
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│      **Seleccione la especialidad del médico**      │")
    print("├─────────────────────────────────────────────────────┤")
    print(f"│ /// 1- Odontología General                         ")
    print(f"│ /// 2- Ortodoncia                                  ")
    print(f"│ /// 3- Odontopediatría                             ")
    print(f"│ /// 4- Implantología Dental                        ")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

    while True:
        option = input("\nSeleccione una especialidad: ")

        if option == "1":
            return "Odontología General"
        if option == "2":
            return "Ortodoncia"
        if option == "3":
            return "Odontopediatría"
        if option == "4":
            return "Implantología Dental"
        else:
            input(
                "\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- \nPresione enter para continuar..."
            )


def guardarMedico(medico: list):
    """
    Función que guarda un médico en el archivo medicos.txt

    Parámetros:
    - medico (list): Lista que contiene la información del médico a guardar en el archivo medicos.txt

    Retorna:
    - None"""
    file = open("medicos.txt", "a", encoding="utf-8")
    for x in medico:
        if not isinstance(x, list):
            file.write(f"{x}~")
        else:
            for y in x:
                file.write(f"{y}~")
    file.write("\n")
    file.close()


def leerMedicos():
    """ "
    Función que lee los médicos registrados en el archivo medicos.txt y los almacena en la lista medicos.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    file = open("medicos.txt", "r")
    medicos_file = file.read().split("\n")
    file.close()
    medicos_file.pop()
    for x in medicos_file:
        medico = []
        horario = []
        medico_preliminar = x.split("~")
        for i in range(len(medico_preliminar)):
            if (
                medico_preliminar[i] == "Trabaja"
                or medico_preliminar[i] == "No Trabaja"
            ):
                horario.append(medico_preliminar[i])

                if len(horario) == 7:
                    medico.append(horario)
            else:
                medico.append(medico_preliminar[i])
        medicos.append(medico)


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
    especialidad = seleccionarEspecialidadMedico()
    medico.append(especialidad)
    print(f"Especilidad: {especialidad}")
    medico.append(input("\nCorreo electrónico del médico: "))
    medico.append(input("Número telefónico del médico: "))
    medico.append(crearSemanaDeTrabajo())

    while True:
        horario = (
            input(
                '\nIngrese "m" si el médico trabaja en la mañana o "t" si el médico trabaja en la tarde: '
            )
            .strip()
            .lower()
        )
        if horario == "m" or horario == "t":
            break
        print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
    medico.append(horario)
    medicos.append(medico)
    guardarMedico(medico)
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

    for i in range(len(medicos)):
        print(f"\n\tMédico {i+1}")
        mostrarMedico(medicos[i])

    input("\nPresione enter para continuar...")

#region Pacientes
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
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│           **Seleccione un médico de la lista**      │")
    print("├─────────────────────────────────────────────────────┤")
    for i in range(len(medicos)):
        print(f"│ /// {i+1}- {medicos[i][0]} ({medicos[i][1]})   ")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

    while True:
        index = int(input("\nSeleccione un médico: ")) - 1

        if index < 0 or index >= len(medicos):
            print("Opción incorrecta, intente de nuevo")
            continue

        break

    return medicos[index]


def guardarPaciente(paciente):
    """ "
    Función que guarda un paciente en el archivo pacientes.txt

    Parámetros:
    - paciente (list): Lista que contiene la información del paciente a guardar en el archivo pacientes.txt

    Retorna:
    - None"""
    file = open("pacientes.txt", "a", encoding="utf-8")
    for x in paciente:
        file.write(f"{x}~")
    file.write("\n")
    file.close()


def leerPacientes():
    """ "
    Función que lee los pacientes registrados en el archivo pacientes.txt y los almacena en la lista pacientes.

    Parámetros:
    - Ninguno

    Retorna:
    - None"""
    file = open("pacientes.txt", "r")
    pacientes_file = file.read().split("\n")
    file.close()
    for x in pacientes_file:
        paciente = x.split("~")
        paciente.pop()
        pacientes.append(paciente)


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
    guardarPaciente(paciente)
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

#region Citas
# * FUNCIONES CITAS---------------------------------------------------------------------------------------------------------------------------


def getDiasDelMes(mes):
    """
    Retorna la cantidad de días que tiene un mes.

    Parámetros:
    - mes (int): El número del mes.

    Retorna:
    - int: La cantidad de días que tiene el mes.
    """
    if mes == 2:
        return 28
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    return 31


def mostrarCita(cita):
    """
    Muestra la información de una cita.

    Args:
        cita (list): Una lista que contiene la información de la cita en el siguiente orden:
            - Fecha de la cita (str)
            - Nombre del paciente (str)
            - Nombre del médico (str)
            - Tratamiento (str)
    """
    print(f"Fecha: {getFechaCita(cita)}")
    print(f"Paciente: {cita[2]}")
    print(f"Médico: {cita[3]}")
    print(f"Tratamiento: {cita[4]}")
    print(f"Estado de Pago: {'Pagada' if cita[5] else 'No Pagada'}")
    if cita[5]:
        print(f"Método de pago: {cita[6]}")
    print("\n")


def menuTratamientos():
    """
    Muestra un menú de opciones de tratamientos y solicita al usuario que seleccione un tratamiento.

    Returns:
        int: La opción de tratamiento seleccionada.
    """
    print(
        "╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮"
    )
    print(
        "│                                             Opciones de tratamientos                                                        │"
    )
    print(
        "├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤"
    )
    print(
        "│ /// 1.  Limpieza dental                                 Odontologia general           - Odontólogo                          │"
    )
    print(
        "│ /// 2.  Puentes dentales                                Prótesis dental               - Prostodoncista                      │"
    )
    print(
        "│ /// 3.  Extracción dental                               Odontologia general           - Odontólogo                          │"
    )
    print(
        "│ /// 4.  Restauración dental                             Estética dental               - Dentista estético                   │"
    )
    print(
        "│ /// 5.  Blanqueamiento dental                           Estética dental               - Dentista estético                   │"
    )
    print(
        "│ /// 6.  Carillas de porcelada                           Estética dental               - Dentista estético                   │"
    )
    print(
        "│ /// 10. Tratamiento de caries                           Odontologia general           - Odontólogo                          │"
    )
    print(
        "│ /// 7.  Colocación de brackets                          Ortodoncia                    - Ortodoncista                        │"
    )
    print(
        "│ /// 8.  Tratamiento de gingivitis                       Odontologia general           - Odontólogo                          │"
    )
    print(
        "│ /// 9.  Colocación de retenedores                       Ortodoncia                    - Ortodoncista                        │"
    )
    print(
        "│ /// 12. Tratamiento de lesiones faciales                Cirugía oral y maxilofacial   - Cirujano oral y maxilofacial        │"
    )
    print(
        "│ /// 11. Cirugía reconstructiva de mandíbula y maxilar   Cirugía oral y maxilofacial   - Cirujano oral y maxilofacial        │"
    )
    print(
        "╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯"
    )

    while True:
        opcion = int(input("\nSeleccione un tratamiento: "))
        if opcion < 1 or opcion > 12:
            print("Opción incorrecta, intente de nuevo")
            continue
        break
    return opcion


def getNombreTratamiento(index):
    """
    Retorna el nombre del tratamiento correspondiente al índice dado.

    Parámetros:
    - index (int): El índice del tratamiento.

    Retorna:
    - str: El nombre del tratamiento correspondiente al índice dado.
    """
    if index == 1:
        return "Limpieza dental"
    if index == 2:
        return "Puentes dentales"
    if index == 3:
        return "Extracción dental"
    if index == 4:
        return "Restauración dental"
    if index == 5:
        return "Blanqueamiento dental"
    if index == 6:
        return "Carillas de porcelana"
    if index == 7:
        return "Tratamiento de caries"
    if index == 8:
        return "Colocación de brackets"
    if index == 9:
        return "Tratamiento de gingivitis"
    if index == 10:
        return "Colocación de retenedores"
    if index == 11:
        return "Tratamiento de lesiones faciales"
    if index == 12:
        return "Cirugía reconstructiva de mandíbula y maxilar"


def getFechaCita(cita):
    return cita[1][len(cita[1]) - 1]


def setFechaCita(cita, fecha):
    cita[1].append(fecha)


def guardarCita(cita):
    """ "
    Función que guarda una cita en el archivo citas.txt

    Parámetros:
    - cita (list): Lista que contiene la información de la cita a guardar en el archivo citas.txt

    Retorna:
    - None
    """
    file = open("citas.txt", "a", encoding="utf-8")
    for x in cita:
        if isinstance(x, list):
            file.write(f"{x[0]}~")
        else:
            if x == False:
                file.write("~")
            else:
                file.write(f"{x}~")
    file.write("\n")
    file.close()


def leerCitas():
    """ "
    Función que lee las citas registradas en el archivo citas.txt y las almacena en la lista citasAgendadas.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    file = open("citas.txt", "r")
    citas = file.read().split("\n")
    file.close()
    citas.pop()
    for x in citas:
        cita = x.split("~")
        cita.pop()
        for i in range(len(cita)):
            if cita[i] == "True" or cita[i] == "":
                cita[i] = bool(cita[i])
        cita[1] = [cita[1]]
        citasAgendadas.append(cita)


def crearCita():
    """
    Función que permite al usuario registrar una cita.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    print("\n\tREGISTRO DE CITAS")

    if len(pacientes) == 0 or len(medicos) == 0:
        print("\n\tNo hay pacientes o médicos registrados\n")
        print(
            "\tPor favor registre un paciente y un médico antes de agendar una cita\n"
        )
        input("\nPresione enter para continuar...")
        return

    while True:
        cita = []

        cita.append(True)

        while True:
            print("Seleccione el mes de la cita")
            mes = int(input("Mes (1-12): "))
            if mes < 1 or mes > 12:
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
                continue
            break
        dias = getDiasDelMes(mes)

        while True:
            print("Seleccione el día de la cita")
            dia = int(input(f"Día (1-{dias}): "))
            if dia < 1 or dia > dias:
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
                continue
            break
        fecha = f"{dia}/{mes}"
        cita.append([fecha])

        while True:
            print("\nSeleccione al paciente")
            for i in range(len(pacientes)):
                print(f"{i+1}- {pacientes[i][0]}")
            index = int(input("\nSeleccione un paciente: ")) - 1
            if index < 0 or index >= len(pacientes):
                print("Opción incorrecta, intente de nuevo")
                continue
            break
        cita.append(pacientes[index][0])

        while True:
            count = 0
            print(f"\nMedicos Disponibles para el {fecha}\n")
            medicosDisponibles = []
            for medico in medicos:
                for citaAgendada in citasAgendadas:
                    if (
                        getFechaCita(citaAgendada) == fecha
                        and citaAgendada[2] == medico[0]
                    ):
                        count += 1
                        break
                else:
                    medicosDisponibles.append(medico)

            if count == len(medicos):
                print("No hay médicos disponibles para esta fecha")
                break

            for i in range(len(medicosDisponibles)):
                print(f"{i+1}- {medicosDisponibles[i][0]} ({medicosDisponibles[i][1]})")

            index = int(input("\nSeleccione un médico: ")) - 1
            if index < 0 or index >= len(medicos):
                print("Opción incorrecta, intente de nuevo")
                continue

            cita.append(medicos[index][0])
            break

        tratamiento = getNombreTratamiento(menuTratamientos())
        cita.append(tratamiento)
        cita.append(False)

        citasAgendadas.append(cita)
        guardarCita(cita)
        print("\n\tCita registrada exitosamente\n")
        mostrarCita(cita)
        input("\nPresione enter para continuar...")
        break


def reprogramarCancelarCita():
    """
    Reprograma o cancela una cita existente.

    Esta función permite al usuario reprogramar o cancelar una cita existente.
    Se solicita al usuario seleccionar el mes y día de la cita que desea reprogramar o cancelar.
    Si la cita existe, se muestra la información actual de la cita y se le da la opción al usuario de reagendar o cancelar la cita.
    Si la cita no existe, se muestra un mensaje indicando que no se encontró una cita en esa fecha.

    Args:
        None

    Returns:
        None
    """
    encontrado = False
    citas = getCitasActivas()

    print("\nREPROGRAMACIÓN/CANCELACIÓN DE CITAS")
    if len(pacientes) == 0 or len(medicos) == 0:
        print("\n\tNo hay pacientes o médicos registrados\n")
        print(
            "\tPor favor registre un paciente y un médico antes de agendar una cita\n"
        )
        input("\nPresione enter para continuar...")
        return

    while True:
        while True:
            print("Seleccione el mes de la cita")
            mes = int(input("Mes (1-12): "))
            if mes < 1 or mes > 12:
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
                continue
            break
        dias = getDiasDelMes(mes)

        while True:
            print("Seleccione el día de la cita")
            dia = int(input(f"Día (1-{dias}): "))
            if dia < 1 or dia > dias:
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
                continue
            break
        fecha = f"{dia}/{mes}"
        for c in citas:

            if getFechaCita(c) == fecha:
                print("\nSe ha encontrado la cita, los datos actuales son:\n")
                mostrarCita(c)
                encontrado = True
                indice = buscarIndiceCita(fecha, c[2], c[4])
                break

        if encontrado == False:
            print("\nNo se ha encontrado una cita en esa fecha")
            input("\nPresione enter para continuar...")
            return

        while True:
            print("¿Desea reagendar o cancelar la cita?\n")
            print("1. Reagendar cita")
            print("2. Cancelar cita")
            print("3. Salir")

            opcion = input("\nSelecione una opcion ")

            if opcion == "1":
                reprogramarCita(indice)
                break
            elif opcion == "2":
                citasAgendadas[indice][0] = False
                print("\nLa cita ha sido cancelada")
                break
            elif opcion == "3":
                print("\nRegresando al menu principal")
                return
            else:
                print("Ingrese una opcion valida")

        input("\nPresione enter para continuar...")
        break


def reprogramarCita(indice):
    """
    Reprograma una cita existente en base a un índice dado.

    Parámetros:
    - indice (int): El índice de la cita a reprogramar en la lista de citas agendadas.

    Retorna:
    None
    """
    citas = getCitasActivas()
    encontrado = False
    print("\nReprogramar cita")
    while True:
        print("Seleccione el nuevo mes de la cita")
        mes = int(input("Mes (1-12): "))
        if mes < 1 or mes > 12:
            print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
            continue
        break
    dias = getDiasDelMes(mes)
    while True:
        print("Seleccione el día de la cita")
        dia = int(input(f"Día (1-{dias}): "))
        if dia < 1 or dia > dias:
            print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")
            continue
        break
    fecha = f"{dia}/{mes}"
    for cita in citas:
        if getFechaCita(cita) == fecha and (
            cita[3] == citasAgendadas[indice][3] or cita[4] == citasAgendadas[indice][4]
        ):
            encontrado = True
            break
    if encontrado == True:
        print(
            "Lo sentimos, en base al medico y tratamiento, no hay disponibilidad para reagendar la cita"
        )
    else:
        while True:
            print(
                "\nSi hay disponibilidad de horario, presione 1 para confirma la reprogramacion de su cita"
            )
            print("1. Confirmar reprogramacion")
            print("2. Cancelar reprogramacion")
            opc = input("\nSeleccione una opcion ")
            if opc == "1":
                setFechaCita(citasAgendadas[indice], fecha)
                print(
                    "\nLa cita ha sido reprogramada exitosamente, a continuacion mostramos sus datos: "
                )
                mostrarCita(citasAgendadas[indice])
                break
            elif opc == "2":
                print("\nLa reprogramacion ha sido cancelada")
                break
            else:
                print("Ingrese una opcion valida")
                continue


def printCitasSinPagar():
    """
    Imprime las citas sin pagar en el siguiente formato:
    {número de cita}- Fecha: {fecha} | Paciente: {nombre del paciente} | Tratamiento: {nombre del tratamiento}
    """

    citasSinPagar = getCitasSinPagar()

    for i in range(len(citasSinPagar)):
        print(
            f"{i+1}- Fecha: {getFechaCita(citasSinPagar[i])} | Paciente: {citasSinPagar[i][2]} | Tratamiento: {citasSinPagar[i][4]}"
        )


def getCitasSinPagar():
    """
    Obtiene una lista de citas agendadas que no han sido pagadas.

    Returns:
        list: Una lista de citas agendadas que no han sido pagadas.
    """
    citas = getCitasActivas()
    citasSinPagar = []
    for cita in citas:
        if cita[5] == False:
            citasSinPagar.append(cita)
    return citasSinPagar


def getCitasPagadas():
    """
    Obtiene una lista de citas agendadas que no han sido pagadas.

    Returns:
        list: Una lista de citas agendadas que no han sido pagadas.
    """
    citas = getCitasActivas()

    citasPagadas = []
    for cita in citas:
        if cita[5] == True:
            citasPagadas.append(cita)
    return citasPagadas


def getCitasActivas():
    """
    Obtiene una lista de citas agendadas que no han sido pagadas.

    Returns:
        list: Una lista de citas agendadas que no han sido pagadas.
    """
    citasActivas = []
    for cita in citasAgendadas:
        if cita[0] == True:
            citasActivas.append(cita)
    return citasActivas


def seleccionarCitaAPagar():
    """
    Esta función permite al usuario seleccionar una cita para pagar.

    La función obtiene la lista de citas sin pagar y verifica si hay citas disponibles.
    Si no hay citas por pagar, se muestra un mensaje y se retorna None.
    Si hay citas por pagar, se muestra la lista de citas y se solicita al usuario que seleccione una cita.
    Se verifica que la opción seleccionada sea válida y se retorna la cita seleccionada.

    Returns:
        list: La cita seleccionada para pagar.

    """
    citasSinPagar = getCitasSinPagar()

    if len(citasSinPagar) == 0:
        print("\n\tNO HAY CITAS POR PAGAR")
        input("Presione enter para continuar...")
        return

    print("\n\tSELECCIONE LA CITA QUE DESEA PAGAR\n")
    printCitasSinPagar()

    while True:
        index = int(input("\nSeleccione una cita: ")) - 1

        if index < 0 or index >= len(citasSinPagar):
            print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo --")
            continue
        break

    return citasSinPagar[index]


def buscarIndiceCita(fecha, paciente, tratamiento):
    """
    Busca el índice de una cita en la lista de citas agendadas.

    Parámetros:
    - fecha (str): La fecha de la cita a buscar.
    - paciente (str): El nombre del paciente de la cita a buscar.
    - tratamiento (str): El nombre del tratamiento de la cita a buscar.

    Retorna:
    - int: El índice de la cita en la lista de citas agendadas, si se encuentra.
    - None: Si la cita no se encuentra en la lista de citas agendadas.
    """
    for i in range(len(citasAgendadas)):
        cita = citasAgendadas[i]
        if (
            getFechaCita(cita) == fecha
            and cita[2] == paciente
            and cita[4] == tratamiento
        ):
            return i

    return None


def imprimirCitas():
    """
    Imprime las citas agendadas en el siguiente formato:
    - Cita [número de cita]
    - Fecha: [fecha de la cita]
    - Paciente: [nombre del paciente]
    - Médico: [nombre del médico]
    - Tratamiento: [nombre del tratamiento]
    - Pagada: [estado de pago de la cita]
    - Método de pago: [método de pago utilizado] (solo si la cita está pagada)

    Si no hay citas agendadas, muestra un mensaje indicando que no hay citas y espera a que el usuario presione enter para continuar.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """
    citas = getCitasActivas()
    if len(citas) == 0:
        print("\n\tNo hay citas agendadas\n")
        input("\nPresione enter para continuar...")
        return

    for i in range(len(citas)):
        print(f"\tCita {i+1}")
        mostrarCita(citas[i])

    input("Presione enter para continuar...")

#region Pagos
#  * FUNCIONES PAGOS---------------------------------------------------------------------------------------------------------------------------


def marcarCitaPagada(index, metodoPago):
    """
    Marca una cita como pagada y registra el método de pago utilizado.

    Parámetros:
    - index (int): El índice de la cita en la lista de citas agendadas.
    - metodoPago (str): El método de pago utilizado para pagar la cita.

    """
    citasAgendadas[index][5] = True
    citasAgendadas[index].append(metodoPago)


def procesarPagos():

    cita = seleccionarCitaAPagar()

    if not cita:
        return

    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│               **Formas De Pago**                    │")
    print("├─────────────────────────────────────────────────────┤")
    print("│Métodos de pago:                                     │")
    print("├─────────────────────────────────────────────────────┤")
    print("│ /// 1. Pago en efectivo                             │")
    print("│ /// 2. Pago Por Transferencia Sinpe                 │")
    print("│ /// 3. Pago por tarjeta de crédito/débito           │")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

    while True:
        metodoDePago = int(
            input("Por favor ingrese el método de pago con el que desea cancelar: ")
        )

        if metodoDePago < 1 or metodoDePago > 3:
            print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo --")
            continue

        break

    nombreMetodoPago = getNombreMetodoPago(metodoDePago)
    descuento = descuento_segun_MetodoPago(nombreMetodoPago)
    tratamiento = cita[4]
    precioNeto = preciosTratamientos(tratamiento)
    precioFinal = calcularPrecioFinal(precioNeto, descuento)

    marcarCitaPagada(
        buscarIndiceCita(getFechaCita(cita), cita[2], tratamiento), nombreMetodoPago
    )
    print("\nTransaccion completada con exito: \n")
    print(f"Tratamiento:\t{tratamiento}")
    print(f"Metodo de Pago:\t{nombreMetodoPago}")
    print(f"Precio Orignial:\t{precioNeto}")
    print(f"Descuento:\t{descuento*100}%")
    print(f"Precio Final:\t{precioFinal}")
    input("\nPresione enter para continuar...")


def preciosTratamientos(tratamiento):
    """
    Devuelve el precio de un tratamiento dental dado su nombre.

    Parámetros:
    - tratamiento (str): El nombre del tratamiento dental.

    Retorna:
    - int: El precio del tratamiento.
    """
    if tratamiento == "Limpieza dental":
        return 30_000
    elif tratamiento == "Puentes dentales":
        return 150_000
    elif tratamiento == "Extracción dental":
        return 40_000
    elif tratamiento == "Restauración dental":
        return 60_000
    elif tratamiento == "Blanqueamiento dental":
        return 50_000
    elif tratamiento == "Carillas de porcelana":
        return 80_000
    elif tratamiento == "Tratamiento de caries":
        return 25_000
    elif tratamiento == "Colocación de brackets":
        return 200_000
    elif tratamiento == "Tratamiento de gingivitis":
        return 35_000
    elif tratamiento == "Colocación de retenedores":
        return 60_000
    elif tratamiento == "Tratamiento de lesiones faciales":
        return 300_000
    elif tratamiento == "Cirugía reconstructiva de mandíbula y maxilar":
        return 500_000


def descuento_segun_MetodoPago(metodo):
    """
    Calcula el descuento según el método de pago seleccionado.

    Parámetros:
    - metodo: str, el método de pago seleccionado.

    Retorna:
    - float, el porcentaje de descuento correspondiente al método de pago.
    """
    if metodo == "Efectivo":
        return 0.10
    elif metodo == "Transferencia Sinpe":
        return 0.30
    elif metodo == "Tarjeta débito/crédito":
        return 0.05


def getNombreMetodoPago(metodo):
    """
    Devuelve el nombre del método de pago correspondiente al número proporcionado.

    Parámetros:
    - metodo: int. El número del método de pago.

    Retorna:
    - str. El nombre del método de pago correspondiente al número proporcionado.
    """
    if metodo == 1:
        return "Efectivo"
    if metodo == 2:
        return "Transferencia Sinpe"
    if metodo == 3:
        return "Tarjeta débito/crédito"


def calcularPrecioFinal(precioNeto, descuento):
    """
    Calcula el precio final de un producto aplicando un descuento al precio neto.

    Parámetros:
    precioNeto (float): El precio neto del producto.
    descuento (float): El porcentaje de descuento a aplicar.

    Retorna:
    float: El precio final del producto después de aplicar el descuento.
    """
    return precioNeto - precioNeto * descuento


def generarFactura():
    citasPagadas = getCitasPagadas()
    print("\nSeleccione una cita para generar la factura:\n")
    i = 1
    while i <= len(citasPagadas):
        cita = citasPagadas[i - 1]
        print(f"{i}. Fecha: {getFechaCita(cita)}, Paciente: {cita[2]}")
        i += 1

    while True:

        opcion = int(
            input("\nSeleccione una cita (por número). Ejemplo, 1, 2 ó 3: ")
        )  # devuelve un string

        if opcion < 1 or opcion > len(citasPagadas):
            print(
                "Por favor, ingrese un número válido, considere que debe ser conforme a la cantidad de citas agendadas."
            )
        else:
            break

    # Obtener los detalles de la cita seleccionada
    cita_seleccionada = citasPagadas[opcion - 1]

    # Detalles de la factura
    clinica = "Clínica de Dientes"  # creo jeje
    especialidad = "Odontología"
    moneda = "CRC"
    paciente = cita_seleccionada[2]
    servicio = cita_seleccionada[4]  # Tratamiento
    precio = preciosTratamientos(servicio)
    cantidad = 1
    subtotal = precio * cantidad
    descuento = descuento_segun_MetodoPago(cita_seleccionada[6])
    iva = 0.13  # Impuesto de venta del 13%
    total_general = subtotal - (subtotal * descuento) + (subtotal * iva)

    # Imprimir la factura
    print("\n" + "=" * 40)
    print("FACTURA".center(40))
    print("=" * 40)
    print(f"Clínica: {clinica}")
    print(f"Especialidad: {especialidad}")
    print(f"Moneda: {moneda}")
    print(f"Nombre del Paciente: {paciente}")
    print("-" * 40)
    print("Servicios:")
    print(f" - Servicio: {servicio}")
    print(f" - Cantidad: {cantidad}")
    print(f" - Precio: {moneda} {precio}")
    print("-" * 40)
    print(f"Detalle: {servicio}")
    print("-" * 40)
    print("Resumen:")
    print(f" - Subtotal: {moneda} {subtotal}")
    print(f" - Descuento: {descuento*100}%")
    print(f" - IVA: {iva*100}%")
    print("-" * 40)
    print(f"Total General: {moneda} {total_general}")
    print("=" * 40)

    # Marcar la cita como pagada
    cita_seleccionada[4] = True

    print("\n¡Factura generada exitosamente!")
    input("\nPresione enter para continuar...")

#region Reportes
# * FUNCIONES REPORTES------------------------------------------------------------------------------------------------------------------------


def mostrarReportes():
    """
    Muestra un menú con las opciones de reportes disponibles.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """
    while True:
        print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
        print("│               **REPORTES**                          │")
        print("├─────────────────────────────────────────────────────┤")
        print("│Opciones:                                            │")
        print("├─────────────────────────────────────────────────────┤")
        print("│ /// 1- Reporte de citas                             │")
        print("│ /// 2- Reporte de pacientes                         │")
        print("│ /// 3- Reporte de médicos                           │")
        print("│ /// 4- Reporte de Tratamiento                       │")
        print("├─────────────────────────────────────────────────────┤")
        print("│ /// 5- Regresar al menú principal                   │")
        print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            generarReporteCitas()
            input("\nPresione enter para continuar...")
        elif opcion == "2":
            generarReportePacientes()
        elif opcion == "3":
            generarReporteMedicos()
        elif opcion == "4":
            print(f"\n{generarReporteTratamientos()}\n")
            input("\nPresione enter para continuar...")
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta, intente de nuevo")
            continue


def mostrarCambiosDeHorarioCita(cita):
    """
    Muestra los cambios de horario de una cita.

    Parámetros:
    - cita (list): Una lista que contiene la información de la cita.

    Retorna:
    Ninguno
    """
    reporte = ""
    if len(cita[1]) == 1:
        reporte = "No hay cambios de horario de la cita"
        return reporte

    print(f"\tCambios de horario de la cita")
    for i in range(1, len(cita[1])):
        reporte += f"\t{i}. {cita[1][i]}"
    return reporte


def generarReporteCitas():
    """
    Genera un reporte de citas agendadas.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """
    print("\n\tREPORTE DE CITAS AGENDADAS\n")
    reporte = ""
    if len(citasAgendadas) == 0:
        print("No hay citas agendadas")
        input("\nPresione enter para continuar...")
        return
    file = open("reporteCitas.txt", "w", encoding="utf-8")
    for i in range(len(citasAgendadas)):
        print(f"\n\tCita {i+1}")
        estado = "Activada" if citasAgendadas[i][0] else "Cancelada"
        print(f"Estado: {estado}")
        mostrarCita(citasAgendadas[i])
        file.write("------------------------------\n")
        file.write(f"Fecha: {getFechaCita(citasAgendadas[i])}\n")
        file.write(f"Paciente: {citasAgendadas[i][2]}\n")
        file.write(f"Médico: {citasAgendadas[i][3]}\n")
        file.write(f"Tratamiento: {citasAgendadas[i][4]}\n")
        file.write(
            f"Estado de Pago: {'Pagada' if citasAgendadas[i][5] else 'No Pagada'}\n"
        )
        if citasAgendadas[i][5]:
            file.write(f"Método de pago: {citasAgendadas[i][6]}\n")
        reporte = mostrarCambiosDeHorarioCita(citasAgendadas[i])
        print(reporte)
        file.write(f"Cambio de horarios:{reporte}\n")
        file.write("------------------------------\n")
    file.close()


def generarReportePacientes():
    """
    Genera un reporte de pacientes registrados.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """

    print("\n\tREPORTE DE PACIENTES REGISTRADOS\n")

    if len(pacientes) == 0:
        print("No hay pacientes registrados")
        input("\nPresione enter para continuar...")
        return
    file = open("reportePacientes.txt", "w", encoding="utf-8")
    for i in range(len(pacientes)):
        mostrarPaciente(pacientes[i])
        file.write("------------------------------\n")
        file.write(f"Nombre: {pacientes[i][0]}\n")
        file.write(f"Correo: {pacientes[i][1]}\n")
        file.write(f"Dirección: {pacientes[i][2]}\n")
        file.write(f"Teléfono: {pacientes[i][3]}\n")
        file.write(f"Médico tratante: {pacientes[i][4]}\n")
    file.write("------------------------------\n")
    file.close()

    input("\nPresione enter para continuar...")


def generarReporteMedicos():
    """
    Genera un reporte de médicos registrados.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """

    print("\n\tREPORTE DE MÉDICOS REGISTRADOS\n")

    if len(medicos) == 0:
        print("No hay médicos registrados")
        input("\nPresione enter para continuar...")
        return
    file = open("reporteMedicos.txt", "w", encoding="utf-8")
    for i in range(len(medicos)):
        file.write("------------------------------\n")
        mostrarMedico(medicos[i])
        file.write(f"Nombre: {medicos[i][0]}\n")
        file.write(f"Especialidad: {medicos[i][1]}\n")
        file.write(f"Correo: {medicos[i][2]}\n")
        file.write(f"Teléfono: {medicos[i][3]}\n")
        file.write(f"Días de trabajo: {formatSemanaDeTrabajo(medicos[i][4])}\n")
        file.write(f"Horario: {getNombreHorario(medicos[i][5])}\n")
    file.write("------------------------------\n")
    file.close()
    input("\nPresione enter para continuar...")


def generarReporteTratamientos():
    reporte = "Reporte de Tratamientos Dentales:\n"
    for tratamiento, precio in tratamientos_y_precios:
        reporte += f"- {tratamiento}: {precio:,} colones\n"
    file = open("reporteTratamientos.txt", "w", encoding="utf-8")
    file.write(reporte)
    file.close()
    return reporte


def crearArchivos():
    """
    Función que crea los archivos necesarios para almacenar la información de los pacientes, médicos y citas.

    Parámetros:
    - Ninguno

    Retorna:
    - None
    """
    open("medicos.txt", "a").close()
    open("citas.txt", "a").close()
    open("pacientes.txt", "a").close()
    open("reporteMedicos.txt", "a").close()
    open("reporteCitas.txt", "a").close()
    open("reportePacientes.txt", "a").close()
    open("reporteTratamientos.txt", "a").close()

#region Variables
# * VARIABLES --------------------------------------------------------------------------------------------------------------------------------
# 'medicos' es una lista que almacena la información de todos los médicos. Cada médico se representa como una lista de sus detalles.
medicos = []

# 'pacientes' es una lista que almacena la información de todos los pacientes. Cada paciente se representa como una lista de sus detalles.
pacientes = []

# 'citas' es una lista que almacena la información de todas las citas. Cada cita se representa como una lista de sus detalles.
citasAgendadas = []

# Lista de tratamientos y precios
tratamientos_y_precios = [
    ["Limpieza dental", 30_000],
    ["Puentes dentales", 150_000],
    ["Extracción dental", 40_000],
    ["Restauración dental", 60_000],
    ["Blanqueamiento dental", 50_000],
    ["Carillas de porcelana", 80_000],
    ["Tratamiento de caries", 25_000],
    ["Colocación de brackets", 200_000],
    ["Tratamiento de gingivitis", 35_000],
    ["Colocación de retenedores", 60_000],
    ["Tratamiento de lesiones faciales", 300_000],
    ["Cirugía reconstructiva de mandíbula y maxilar", 500_000],
]
#region Main
# * PROGRAMA PRINCIPAL ------------------------------------------------------------------------------------------------------------------------
crearArchivos()
print(presentacion)
leerCitas()
leerPacientes()
leerMedicos()

while True:

    # Mostraremos el menú principal:
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│               **MENÚ PRINCIPAL**                    │")
    print("├─────────────────────────────────────────────────────┤")
    print("│Opciones:                                            │")
    print("├─────────────────────────────────────────────────────┤")
    print("│ /// 1- Módulo de expedientes                        │")
    print("│ /// 2- Módulo de citas y cancelación de citas       │")
    print("│ /// 3- Módulo de pagos                              │")
    print("│ /// 4- Módulo de reportes                           │")
    print("├─────────────────────────────────────────────────────┤")
    print("│ /// 5- Salir                                        │")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

    # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
    menu_option = input("\nSeleccione una opcion: ")

    if (
        menu_option == "1"
    ):  # ! Módulo de Expedientes -----------------------------------------------------------------------------

        while True:
            # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
            # Mostraremos el menú del Módulo de Expedientes:
            print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
            print("│              **MODULO DE EXPEDIENTES**              │")
            print("├─────────────────────────────────────────────────────┤")
            print("│Opciones:                                            │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 1- Agregar médico                               │")
            print("│ /// 2- Agregar pacientes                            │")
            print("│ /// 3- Ver médicos                                  │")
            print("│ /// 4- Ver pacientes                                │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 5- Regresar al MENÚ PRINCIPAL                   │")
            print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

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
                    "A continuación se muestran los médicos del consultorio dental:\n"
                )
                mostrarTodosMedicos()

            elif menu_option == "4":
                # Lista de pacientes ya registrados
                print(
                    "A continuación se muestran los pacientes del consultorio dental:\n"
                )
                mostrarTodosPacientes()

            elif menu_option == "5":
                # Si el usuario elige regresar al menú principal
                break

            else:
                # Si el usuario elige una opción incorrecta
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")

    elif (
        menu_option == "2"
    ):  # ! Módulo de Citas y Cancelación de Citas ----------------------------------------------------------
        while True:
            # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
            print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
            print("│     **MODULO DE CITAS Y CANCELACIÓN DE CITAS**      │")
            print("├─────────────────────────────────────────────────────┤")
            print("│Opciones:                                            │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 1- Registrar cita                               │")
            print("│ /// 2- Cancelar cita                                │")
            print("│ /// 3- Ver citas agendadas                          │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 4- Regresar al MENÚ PRINCIPAL                   │")
            print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

            menu_option = input("\n\tSeleccione una opcion: ")

            if menu_option == "1":
                # Si el usuario elige registrar una cita
                crearCita()

            elif menu_option == "2":
                # Si el usuario elige cancelar una cita
                reprogramarCancelarCita()

            elif menu_option == "3":
                # Si el usuario elige ver las citas agendadas
                print("\n\tCITAS AGENDADAS\n")
                imprimirCitas()

            elif menu_option == "4":
                # Si el usuario elige regresar al menú principal
                break

            else:
                # Si el usuario elige una opción incorrecta
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")

    elif (
        menu_option == "3"
    ):  # ! Módulo de Pagos ----------------------------------------------------------------------------------
        while True:
            # Solicito al usuario que elija una opción del menú, si se cumple (elige la opción) el programa continua.
            print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
            print("│                **MODULO DE PAGOS**                  │")
            print("├─────────────────────────────────────────────────────┤")
            print("│Opciones:                                            │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 1- Formas de pago                               │")
            print("│ /// 2- Facturación                                  │")
            print("├─────────────────────────────────────────────────────┤")
            print("│ /// 3- Regresar al MENÚ PRINCIPAL                   │")
            print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

            menu_option = input("\n\tSeleccione una opcion: ")

            if menu_option == "1":
                # Si el usuario elige Formas de pago
                procesarPagos()

            elif menu_option == "2":
                # Si el usuario elige Facturación
                generarFactura()

            elif menu_option == "3":
                # Si el usuario elige regresar al menú principal
                break

            else:
                # Si el usuario elige una opción incorrecta
                print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")

    elif (
        menu_option == "4"
    ):  # ! Módulo de Reportes -------------------------------------------------------------------------------
        mostrarReportes()

    elif (
        menu_option == "5"
    ):  # ! Salir del programa -------------------------------------------------------------------------------
        print("\n -- CERRANDO PROGRAMA -- \n")
        break

    else:  # ! Opción incorrecta
        print("\n-- OPCIÓN INCORRECTA: Inténtelo de nuevo -- ")

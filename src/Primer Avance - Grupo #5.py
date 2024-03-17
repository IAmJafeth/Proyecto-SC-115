presetación = """
    PROYECTO FINAL - Grupo #5

Curso:          Programación Básica

Profesora:      SABORIO OVIEDO MARIA LAURA

Estudiantes:    Jafeth Garro Roldán
                Daniela Elena Gómez Mora
                Aldo Mora Aguilar
                Daniel Vindas Morraz

"""
# Variables

# Variables para médico:
# nomMed
# especialidad
# corrmed
# telefMed
# diasSemana
# mañTard

# Variables para paciente:
# nomPac
# corrPac
# direccion
# telefPac
# medPac

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

    if menu_option == "1":  # ! Módulo de Expedientes

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
                print("\n\t\t-- Ingresando Médico --\n")
                nomMed = input(
                    "\tEstimado(a) usuario, por favor ingrese el nombre completo del médico: ")
                especialidad = input(
                    "\tEstimado(a) usuario, por favor ingrese la especialidad del médico: ")
                corrMed = input(
                    "\tEstimado(a) usuario, por favor ingrese el correo electrónico del médico: ")
                telefMed = input(
                    "\tEstimado(a) usuario, por favor ingrese el número telefónico del médico: ")
                diasSemana = input(
                    "\tEstimado(a) usuario, por favor ingrese los días de trabajo del médico en el siguiente formato día/día/+...: ")
                mañTard = input(
                    "\tEstimado(a) usuario, por favor ingrese \"m\" si el médico trabaja en la mañana o \"t\" si el médico trabaja en la tarde: ")

            elif menu_option == "2":

                # Si el usuario elige agregar un paciente nuevo
                print("\n\t\t-- Ingresando Paciente --\n")
                nomPac = input(
                    "\tEstimado(a) usuario, por favor ingrese el nombre del paciente: ")
                corrPac = input(
                    "\tEstimado(a) usuario, por favor ingrese el correo electrónico del paciente: ")
                direccion = input(
                    "\tEstimado(a) usuario, por favor ingrese la dirección del paciente: ")
                telefPac = input(
                    "\tEstimado(a) usuario,por favor digite el número telefónico del paciente: ")
                medPac = input(
                    "\tEstimado(a) usuario, por favor ingrese el nombre del médico encargado: ")

            elif menu_option == "3":
                # Lista de médicos
                print("A continuación se muestran los médicos del consultorio dental:\n")
                print(
                    "-------------------------------------------------------------------------------------")
                print("Nombre", nomMed)
                print("Especialidad", especialidad)
                print("Correo", corrMed)
                print("Teléfono", telefMed)
                print("Dias disponibles", diasSemana)
                print("Horario disponible", mañTard)
                print(
                    "-------------------------------------------------------------------------------------")

            elif menu_option == "4":
                # Lista de pacientes ya registrados
                print(
                    "A continuación se muestran los pacientes del consultorio dental:\n")
                print(
                    "-------------------------------------------------------------------------------------")
                print("Nombre", nomPac)
                print("Correo", corrPac)
                print("Dirección", direccion)
                print("Teléfono", telefPac)
                print("Médico tratante", medPac)
                print(
                    "-------------------------------------------------------------------------------------")

            elif menu_option == "5":
                break

            else:
                print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

    elif menu_option == "2":
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "3":
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "4":
        print("\n -- OPCIÓN AÚN EN DESARROLLO --")

    elif menu_option == "5":
        print("\n -- CERRANDO PROGRAMA -- \n")
        break

    else:
        print("\n-- OPCIÓN INCORECTA: Inténtelo denuevo -- ")

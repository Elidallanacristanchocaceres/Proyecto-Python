import modules.Inici as cf
import funciones.globales as gf
import funciones.control as st
import main

def ConsultarPaciente():
    NroIdentificacion = input("Ingrese su número de cédula : ")
    paciente = gf.centroMedico['data'].get(NroIdentificacion)
    if paciente:
        print("Información del Paciente : ")
        print(f"Número de Identificación: {paciente.get('NroIdentificacion')}")
        print(f"Nombre y Apellido: {paciente.get('NombreApellido')}")
        print(f"Número de Consultorio: {paciente.get('NroConsultorio')}")
        print("Historial Médico:")
        print(f"Diagnóstico: {paciente.get('Historial', {}).get('Diagnostico', 'No disponible')}")
        print(f"Tratamiento: {paciente.get('Historial', {}).get('Tratamiento', 'No disponible')}")
        gf.pausar_pantalla()
        return MenuPacientes('op')
    else:
        print("No se encontró información para ese número de cédula", NroIdentificacion)
        
        gf.pausar_pantalla()
        return ConsultarPaciente()
 
def MenuPacientes(op : int):
    title = """
    **************************************
    * ADMINISTRAR PACIENTES CENTRO MEDICO*
    **************************************
    
    1.Crear 
    2. Editar 
    3. Leer 
    4. Eliminar 
    5. Consultar Paciente 
    6. Salir"
    """
    
    gf.borrar_pantalla()
    print(title)
    if (op != 6):
        
        try:
            op = int(input(":) "))
        except ValueError:
            print("La opcion que ingresaste es erronea :")
            gf.pausar_pantalla()
            MenuPacientes(0)
        else:
            match(op):
                case 1:
                    st.NewPacientes()
                case 2:
                    st.ModificarDatosPaciente()
                case 3:
                    especializacion = input("Ingrese la especialización (dejar en blanco para mostrar todos) : ")
                    st.LeerPacientes(especializacion)
                case 4:
                    st.EliminarPaciente()
                case 5:
                    ConsultarPaciente()
                case 6:
                    main.mainMenu(0)
                case _:
                    print("La opcion ingresada no esta disponible en las opciones :")
                    gf.pausar_pantalla()


def MenuMedicos(op : int):
    title ="""
    *******************
    *GESTIONAR MEDICOS*
    *******************
"""

    MenuMedicosOp = "1.Crear \n2. Editar \n3. Leer \n4. Eliminar \n5. Salir"
    gf.borrar_pantalla()
    if (op !=4):
        print(title)
        print(MenuMedicosOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("La opcion no tiene formato adecuado : ")
            gf.pausar_pantalla()
            MenuMedicos(0)
        else:
            match(op):
                case 1:
                    st.NewMedicos()
                case 2:
                    st.ModificarDatosMedico()
                case 3:
                    especializacion = input("Ingrese la especialización (dejar en blanco para mostrar todos) : ")
                    st.LeerMedicos(especializacion)
                case 4:
                    st.EliminarMedicos()
                case 5:
                    main.mainMenu(0)
                case _:
                    print("La opcion ingresada no esta disponible en las opciones : ")
                    gf.pausar_pantalla()

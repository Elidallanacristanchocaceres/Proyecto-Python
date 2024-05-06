import os
import json
from datetime import datetime, timedelta
import funciones.globales as gf
import modules.Inici as cf
import ui.uipacientes as uisSt

def NewMedicos():
    
    title = """
    ****************************
    * INFORMACION DEL MEDICO *
    ****************************
    """
    gf.borrar_pantalla()
    print(title)
    
    NroIdentificacion = int(input("Ingrese el numero de identificacion del medico :"))
    NombreApellido = input("Ingrese el nombre y apellido del medico:")
    Email = input("Ingrese el correo electronico :")
    NroConsultorio = int(input("Cual es el numero del consultorio del medico :"))
    especializacion = input("Cual es la especializacion del medico? (Pediatria, Ginecologia, Dermatologia, Endocrinologia, Optometria):")
    especialidades_validas = ['Pediatria', 'Ginecologia', 'Dermatologia', 'Endocrinologia', 'Optometria']
    if especializacion not in especialidades_validas:
        print("La especializacion es invalida debes escoger entre:", ", ".join(especialidades_validas))
    else:
        medicos = {
            'NroIdentificacion' : NroIdentificacion,
            'NombreApellido' : NombreApellido,
            'Email' : Email,
            'NroConsultorio' : NroConsultorio
        }
        
        if especializacion not in gf.centroMedico['data']:
            gf.centroMedico['data'][especializacion] = {}
            
        gf.centroMedico['data'][especializacion][NroIdentificacion] = medicos
        print("El medico se añadio correctamente a la especializacoion de:", especializacion)
        
        cf.UpdateFile(gf.centroMedico)
        
        cf.UpdateFile(gf.centroMedico)
    if(bool(input('Desea registrar otro medico? S(Si) o Enter(No) :'))):
        NewMedicos()
    else:
       uisSt.MenuMedicos(0)

def BuscarDatos():
    NroIdentificacion = input('Ingrese el Nro Identificación del médico: ')
    centroMedico = gf.centroMedico.get('data')

    if centroMedico:
        for especializacion, medicos in centroMedico.items():
            if NroIdentificacion in medicos:
                return medicos[NroIdentificacion]

    return None

def ModificarDatosMedico():
    datosMedico = BuscarDatos()
    if datosMedico:
        NroIdentificacion = datosMedico['NroIdentificacion']
        NombreApellido = datosMedico.get('NombreApellido', '')
        Email = datosMedico.get('Email', '')
        NroConsultorio = datosMedico.get('NroConsultorio', '')
        especializacion = datosMedico.get('Especializacion', '')

        print(f"Datos actuales del médico con Nro de Identificación {NroIdentificacion}:")
        print(f"1. Nombre y Apellido: {NombreApellido}")
        print(f"2. Correo Electrónico: {Email}")
        print(f"3. Número de Consultorio: {NroConsultorio}")
        print(f"4. Especialización: {especializacion}")

        for clave in datosMedico.keys():
            if clave not in ['NroIdentificacion']:
                if bool(input(f'Desea modificar {clave}? S(Si) o Enter No : ')):
                    datosMedico[clave] = input(f'Ingrese el nuevo {clave} :')
        
        gf.centroMedico['data'].update({NroIdentificacion: datosMedico})
        cf.ActualizarArchivo(gf.centroMedico)
        print("Datos del médico actualizados exitosamente.")
    else:
        print("No se encontraron datos para modificar.")
    
    gf.pausar_pantalla()
    uisSt.MenuMedicos(0)

    
def LeerMedicos(especializacion=None):
    titulo = """
    *********************
    * LISTA DEL MÉDICO  *
    *********************
    """
    gf.borrar_pantalla()
    print(titulo)
    
    centroMedico = gf.centroMedico.get('data')
    
    if not centroMedico:
        print("No hay médicos registrados.")
    else:
        if especializacion:
            medicos = centroMedico.get(especializacion, {})
            for medico_id, medico_info in medicos.items():
                if isinstance(medico_info, dict):  # Verifica si medico_info es un diccionario
                    print(f"Número de Identificación: {medico_id}")
                    print(f"Nombre y Apellido: {medico_info.get('NombreApellido', 'N/A')}")
                    print(f"Correo Electrónico: {medico_info.get('Email', 'N/A')}")
                    print(f"Número de Consultorio: {medico_info.get('NroConsultorio', 'N/A')}")
                    print(f"Especialización: {especializacion}")
                    print("\n")
                else:
                    print(f"Número de Identificación: {medico_id}")
                    print(f"Información del médico: {medico_info}")
                    print("\n")
        else:
            for especialidad, medicos in centroMedico.items():
                for medico_id, medico_info in medicos.items():
                    if isinstance(medico_info, dict):  # Verifica si medico_info es un diccionario
                        print(f"Número de Identificación: {medico_id}")
                        print(f"Nombre y Apellido: {medico_info.get('NombreApellido', 'N/A')}")
                        print(f"Correo Electrónico: {medico_info.get('Email', 'N/A')}")
                        print(f"Número de Consultorio: {medico_info.get('NroConsultorio', 'N/A')}")
                        print(f"Especialización: {especialidad}")
                        print("\n")
                    else:
                        print(f"Número de Identificación: {medico_id}")
                        print(f"Información del médico: {medico_info}")
                        print("\n")
            
    gf.pausar_pantalla()
    uisSt.MenuMedicos(especializacion)
    
def EliminarMedicos():
    NroIdentificacion = input("Ingrese el número de identificación del médico que desea eliminar: ")
    centroMedico = gf.centroMedico.get('data', {})
    
    for especialidad, medicos in centroMedico.items():
        
        if NroIdentificacion in medicos:
            del medicos[NroIdentificacion]  
            cf.UpdateFile(gf.centroMedico)  
            print("Médico eliminado exitosamente.")
            gf.pausar_pantalla()
            return uisSt.MenuMedicos('op')

    
    print("El número de identificación no existe en la base de datos.")


def NewPacientes():
    
    title = """
    ****************************
    * INFORMACION DEL PACIENTE *
    ****************************
    """
    gf.borrar_pantalla()
    print(title)
    NroIdentificacion = int(input("Ingrese el numero de identificacion : "))
    NombreApellido = input("Ingrese el nombre y apellido : ")
    NumeroTelefonico = int(input("Ingrese su numero de telefono : "))
    NumeroCelular = int(input("Ingrese su numero de celular : "))
    FechaNacimiento = int(input("Ingrese la fecha de nacimiento DD/MM/AA : "))
    Edad = int(input("Ingrese su edad : "))
    Genero = input("Ingrese el genero : ")
    NroConsultorio = int(input("Cual es el numero del consultorio : "))
    especializacion = input("De que especializacion la quiere? (Pediatria, Ginecologia, Dermatologia, Endocrinologia, Optometria):")
    especialidades_validas = ['Pediatria', 'Ginecologia', 'Dermatologia', 'Endocrinologia', 'Optometria']
    if especializacion not in especialidades_validas:
        print("La especializacion es invalida debes escoger entre:", ", ".join(especialidades_validas))
    else:
        hora_cita = int(input("Ingrese la hora de la cita (formato HH:MM): "))
        
        try:
            hora_cita_dt = datetime.strptime(hora_cita, '%H:%M')
        except ValueError:
            print("Formato de hora incorrecto. Debe ser HH:MM.")
            return
        
        citas = gf.centroMedico.get('data')
        if isinstance(citas, dict):
            for paciente_id, paciente_info in citas.items():
                if isinstance(paciente_info, dict) and 'HoraCita' in paciente_info:
                    cita_dt = datetime.strptime(paciente_info['HoraCita'], '%H:%M')
                    if cita_dt == hora_cita_dt:
                        print("La hora seleccionada para la cita está ocupada. Por favor, elige otra hora.")
                        return
        else:
            print("No se pudo verificar la disponibilidad de la cita.")
            
        hora_fin_cita = hora_cita_dt + timedelta(minutes=20)
        hora_fin_cita_str = hora_fin_cita.strftime('%H:%M')

        pacientes = {
            'NroIdentificacion' : NroIdentificacion,
            'NombreApellido' : NombreApellido,
            'NumeroTelefonico' : NumeroTelefonico,
            'NumeroCelular' : NumeroCelular,
            'FechaNacimiento' : FechaNacimiento,
            'Edad' : Edad,
            'Genero' : Genero,
            'NroConsultorio' : NroConsultorio,
            'Especializacion' : especializacion,
            'HoraCita' : hora_cita,  
            'HoraFinCita': hora_fin_cita_str
        }
        
        Diagnostico = input("Ingrese el diagnóstico del paciente: ")
        Tratamiento = input("Ingrese el tratamiento recomendado: ")

        # Actualizar el historial médico del paciente
        pacientes['Historial'] = {
        'Diagnostico': Diagnostico,
        'Tratamiento': Tratamiento
    }

        cf.AddData('data', NroIdentificacion, pacientes)
        gf.centroMedico.get('data').update({NroIdentificacion: pacientes})
        print("El paciente se añadió a la cita de:", especializacion)
        print("La cita durara 20 minutos.")
        
        

        paciente_id = input("Ingrese el número de identificación del medico:")
        paciente_info = gf.centroMedico.get('data').get(especializacion, {}).get(paciente_id)
        if paciente_info:
            if 'Citas' not in paciente_info:
                paciente_info['Citas'] = []
            paciente_info['Citas'].append({'Paciente': NombreApellido, 'HoraCita': hora_cita})
            cf.UpdateFile(gf.centroMedico)
            print("Cita registrada en el médico:", paciente_info['NombreApellido'])
        else:
            print("No se pudo registrar la cita. El paciente no existe o no tiene la especialización requerida.")
        cf.UpdateFile(gf.centroMedico)

        if(bool(input('¿Desea registrar otro paciente? S(Si) o Enter(No): '))):
            NewPacientes()
        else:
            uisSt.MenuPacientes(0)

def BuscarDatosPaciente():
    criterio = input('Ingrese el Nro Identificación del paciente : ')
    datos = gf.centroMedico.get('data').get(criterio)
    return datos

def ModificarDatosPaciente():
    datosPaciente = BuscarDatosPaciente()
    if datosPaciente:
        NroIdentificacion = datosPaciente['NroIdentificacion']
        NombreApellido = datosPaciente.get('NombreApellido', '')
        NumeroTelefonico = datosPaciente.get('NumeroTelefonico', '')
        NumeroCelular = datosPaciente.get('NumeroCelular', '')
        FechaNacimiento = datosPaciente.get('FechaNacimiento', '')
        Edad = datosPaciente.get('Edad', '')
        Genero = datosPaciente.get('Genero', '')
        NroConsultorio = datosPaciente.get('NroConsultorio', '')
        especializacion = datosPaciente.get('Especializacion', '')
        Sintomas = datosPaciente.get('Sintomas', '')

        print(f"Datos actuales del paciente con Nro de Identificación {NroIdentificacion}:")
        print(f"1. Nombre y Apellido: {NombreApellido}")
        print(f"2. Número de Teléfono: {NumeroTelefonico}")
        print(f"3. Número de Celular: {NumeroCelular}")
        print(f"4. Fecha de Nacimiento: {FechaNacimiento}")
        print(f"5. Edad: {Edad}")
        print(f"6. Género: {Genero}")
        print(f"7. Número de Consultorio: {NroConsultorio}")
        print(f"8. Especialización: {especializacion}")
        print(f"9. Síntomas: {', '.join(Sintomas)}")

        for clave in datosPaciente.keys():
            if clave not in ['NroIdentificacion', 'Sintomas']:
                if bool(input(f'Desea modificar {clave}? (S para sí, Enter para No): ')):
                    datosPaciente[clave] = input(f'Ingrese el nuevo {clave}: ')

        gf.centroMedico['data'][NroIdentificacion] = datosPaciente
        cf.ActualizarArchivo(gf.centroMedico)
        print("Datos del paciente actualizados exitosamente.")
    else:
        print("No se encontraron datos para modificar.")
    
    gf.pausar_pantalla()
    uisSt.MenuPacientes(0)
    
def LeerPacientes(especializacion=None):
    titulo = """
    **************************
    * LISTA DE PACIENTES     *
    **************************
    """
    gf.borrar_pantalla()
    print(titulo)
    
    centroMedico = gf.centroMedico.get('data')
    
    if not centroMedico:
        print("No hay pacientes registrados.")
    else:
        for paciente_id, paciente_info in centroMedico.items():
            if especializacion:
                if 'Especializacion' in paciente_info and paciente_info['Especializacion'] == especializacion:
                    print(f"Número de Identificación: {paciente_id}")
                    print(f"Nombre y Apellido: {paciente_info.get('NombreApellido', 'N/A')}")
                    print(f"Número de Consultorio: {paciente_info.get('NroConsultorio', 'N/A')}")
                    print(f"Historial Médico: ")
                    print(f"Diagnóstico: {paciente_info.get('Historial', {}).get('Diagnostico', 'No disponible')}")
                    print(f"Tratamiento: {paciente_info.get('Historial', {}).get('Tratamiento', 'No disponible')}")
                    print("\n")
            else:
                print(f"Número de Identificación: {paciente_id}")
                print(f"Nombre y Apellido: {paciente_info.get('NombreApellido', 'N/A')}")
                print(f"Número de Consultorio: {paciente_info.get('NroConsultorio', 'N/A')}")
                print(f"Especialización: {paciente_info.get('Especializacion', 'N/A')}")
                print(f"Historial Médico: ")
                print(f"Diagnóstico: {paciente_info.get('Historial', {}).get('Diagnostico', 'No disponible')}")
                print(f"Tratamiento: {paciente_info.get('Historial', {}).get('Tratamiento', 'No disponible')}")
                print("\n")
            
    gf.pausar_pantalla()
    uisSt.MenuPacientes(especializacion)


    
def EliminarPaciente():
    NroIdentificacion = input("Ingrese el número de identificación del paciente que desea eliminar: ")
    centroMedico = gf.centroMedico.get('data')
    if NroIdentificacion in centroMedico:
        del centroMedico[NroIdentificacion]
        cf.UpdateFile(gf.centroMedico)
        print("Paciente eliminado exitosamente.")
        gf.pausar_pantalla()
        return uisSt.MenuPacientes('op')
        
    else:
        print("El número de identificación no existe en la base de datos.")
    
    

        
        
     
        
    







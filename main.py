import modules.Inici as cf
import funciones.globales as fg
import ui.uipacientes as uiSt

def mainMenu(op):
    fg.borrar_pantalla()
    Title = """
    ***************************************
    * ESPECIALIZACIONES DEL CENTRO MEDICO *
    ***************************************
"""
    mainMenuOp = "1. Gestionar citas \n2 Gestionar medico \n3. Salir "

    if (op != 4):
        print(Title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('La opcion que ingreso es erronea :')
            fg.borrar_pantalla()
            mainMenu(0)
        else:
            match (opcion):
                case 1:
                    uiSt.MenuPacientes(0)
                case 2:
                    uiSt.MenuMedicos(0)
                case 3:
                    print('Hasta Luego')
                    fg.pausar_pantalla()
                case _:
                    print('La opcion ingreseda no se encuentra. Ingresa otra : ')
                    fg.pausar_pantalla()
                    mainMenu(0)

if __name__ == '__main__': 
    cf.MY_DATABASE = 'data/pacientes.json'
    cf.checkFile(fg.centroMedico)
    mainMenu(0)
    
    fg.centroMedico['data'] = {
        'Pediatria': {},
        'Ginecologia': {},
        'Dermatologia': {},
        'Endocrinologia': {},
        'Optometria': {}
    }
    
    fg.centroMedico['data'] = {
        'Pediatria': {
            'medico': {
                'NroIdentificacion': '001',
                'NombreApellido': 'Dr. Jorge Perez',
                'Email': 'jorge@gmail.com',
                'NroConsultorio': '101'
            }
        },
        'Ginecologia': {
            'medico': {
                'NroIdentificacion': '002',
                'NombreApellido': 'Dra. Diana Garcia',
                'Email': 'diana@gmail.com',
                'NroConsultorio': '102'
            }
        },
        'Dermatologia': {
            'medico': {
                'NroIdentificacion': '003',
                'NombreApellido': 'Dr. Jesus Lopez',
                'Email': 'jesus@gmail.com',
                'NroConsultorio': '103'
            }
        },
        'Endocrinologia': {
            'medico': {
                'NroIdentificacion': '004',
                'NombreApellido': 'Dra. Rosa Rodriguez',
                'Email': 'rosa@gmail.com',
                'NroConsultorio': '104'
            }
        },
        'Optometria': {
            'medico': {
                'NroIdentificacion': '005',
                'NombreApellido': 'Dr. Luis Martinez',
                'Email': 'luis@gmail.com',
                'NroConsultorio': '105'
            }
        }
    }
                    

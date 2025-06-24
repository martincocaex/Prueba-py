diccionario:{
                "usuario"[
                    {
                        "nombre":"",
                        "sexo":"",
                        "contraseña":""
                    }                
                ] 


            }





def largo_contraseña (contraseña:str):
    for i in range(8):
     print("La contraseña debe tener un maximo de largo de 8 caracteres.")
        
          


def eliminar_estudiante(estudiante:dict) -> None:
    datos_alumnos.remove(estudiante)
    print("Estudiante eliminado.")

def validar_datos_estudiante() -> dict:
    try:
        nombre_estudiante = input('Nombre: ').lower()
        
       
        exite_estudiante = buscar_estudiante(nombre_estudiante, 'nombre')
        if exite_estudiante != {}:
            print('Error: el nombre de estudiante ya existe.')
            return {}
        
        
        genero_estudiante = input('Genero (solo "F" o "M"): ').upper()
        
        
        if genero_estudiante != 'F' and genero_estudiante != 'M':
            print('Error: solo se permiten "F" de femenino o "M" de masculino.') 
            return {}
        
        
       
        
        
        return {"nombre":nombre_estudiante, "genero":genero_estudiante, "contraseña":contraseña_estudiante}
    
    except ValueError:
        print('Error: algun valor ingresado invalido.')
        return {}

def crear_estudiante() -> None:
    estudiante = validar_datos_estudiante()
   
    
    
    if estudiante != {}:
        
        datos_alumnos.append(estudiante)
        print("Estudiante agregado con exito")

def modificar_datos_estudiante(estudiante:dict):
    
    try:

        genero_estudiante = input("Genero (solo "F" o "M"): ").upper()
            

        if genero_estudiante != 'F' and genero_estudiante != 'M':
            print("Error: solo se permiten "F" de femenino o "M" de masculino.")
            return {}

            
       
        
        for i in datos_alumnos:
            if i['usuario'] == estudiante['usuario']:
                i['sexo'] == sexo
                i['contraseña'] == contraseña
        
        return True 
        
    except ValueError:
        print('Error: solo se permiten numeros enteros.')
        return {}
    


while True:
    try:
        print("*** MENU INGRESO DE USUARIOS ***")
        print("[1] - Ingresa usuario.")
        print("[2] - Buscar usuario.")
        print("[3] - Eliminar usuario.")
        print("[4] - Salir.")




        opcion = str(input("Ingrese una opcion :"))


        if opcion == 1:
            print("*** Añadir usuario ***")
            
            diccionario:{
                "usuario"[
                    {
                        "nombre":"nombre",
                        "sexo":"sexo",
                        "contraseña":"contraseña"
                    }                
                ] 


            }

            while True:
                if diccionario["usuario"]:
                    
                    nombre = input("Ingrese el nombre del usuario: ")
                    sexo = modificar_datos_estudiante("Ingrese el sexo del usuario F/M : ")
                    contraseña = largo_contraseña("Ingrese una contraseña: ")
                 

           
        elif opcion == 2:
            while True:
                try:
                    input("Ingrese el nombre del Usuario: ")
                    if diccionario["usuario"] == diccionario["usuario"]:

                        print(diccionario["usuario"])
                        
                    else:
                        print("El usuario no se encuentra.")
                        continue
                except ValueError:
                    print("Ingrese caracter")
        elif opcion == 3:
            diccionario["usuario"],eliminar_estudiante("")


        
        
        
        elif opcion == 4:
            print("Saliendo .....")
            break
        
        
        
        
        
        else:
            print("Opcion invalida.")
            continue
    
    except ValueError:
        print("Opcion invalida")
        continue
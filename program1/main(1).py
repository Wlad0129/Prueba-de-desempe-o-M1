from crud import *

def menu():
    """Imprime las opciones del sistema en consola."""
    print("\n" + "="*45)
    print(" student GESTIÓN SYSTEM")
    print("="*45)
    print("1. register student")
    print("2. list student")
    print("3. search student")
    print("4. update student")
    print("5. delete student")
    print("6. exit")
    print("-" * 45)

def ask_integer(Mesagge):
    while True:
        valeu = input(Mesagge)
        try:
            
            integer = int(valeu)
            if integer < 0:
                print("=> Error: The number cannot be negative..")
                continue
            return integer
        except ValueError:
            
            print("=> Error: Invalid data. You must enter a valid integer..")

def ask_datos(id_proporcionado=None):
    if id_proporcionado is None:
        while True:
            id_student = ask_integer("Enter your unique ID/ID number: ")
            
            if search_student_id(id_student) is not None:
                print("=> Error: There is already a student with that ID. Please try entering it again..")
            else:
                break
    else:
        id_student = id_proporcionado

    
    while True:
        name = input("Enter name: ").strip()
        if name:
            break
        print("=> Error: The name cannot be empty.")

    age = ask_integer("Enter the age: ")
    
    while True:
        op_plan = input("Enter (1. course, 2. program): ")
        if op_plan == '1':
            tipo_plan = "course"
            input(" ")
            break
        elif op_plan == '2':
            tipo_plan = "program"
            input(" ")
            break
        else:
            print("=> Error: Invalid option. Try again.")

    
    while True:
        op_status = input("Enter status(1. active, 2. inactive): ")
        if op_status == '1':
            status = "active"
            break
        elif op_status == '2':
            status = "inactive"
            break
        else:
            print("=> Error: Invalid option. Try again.")

    return {
        "id": id_student,
        "name": name,
        "age": age,
        "tipo_plan": tipo_plan,
        "status": status
    }

def read_student(student):
    """Manejo de visualización atractiva de un diccionario student (Criterio 6: Código Limpio)."""
    
    print(student)

def iniciar_sistema():
    while True:
        menu()
        op = input("choose a option (1-6): ")
        
        
        if op == '1':
            print("\n--- New student ---")
            datos_nuevo = ask_datos() 
            register_student_json(datos_nuevo)
            print("\n=> ¡student saved successfully!")
            
        elif op == '2':
            print("\n--- student list ---")
            regist = read_student_json()
            if not regist:
                print("=> There are no student registered in the system yet..")
            else:
                for r in regist:
                    read_student(r)
                    
        
        elif op == '3':
            print("\n--- Search student ---")
            
            while True:
                tipo = input("¿Search (1) ID or (2) name?: ")
                if tipo in ['1', '2']:
                    break
                print("=> Error: Invalid search option.")
                
            if tipo == '1':
                id_search = ask_integer("Enter ID to search: ")
                results = search_student_id(id_search)
                if results:
                    print("\nRecord found:")
                    read_student(results)
                else:
                    print("=> student not found with this ID.")
                    
            elif tipo == '2':
                name_id_search = input("Enter full or parcial name tosearch: ").strip()
                results = search_student_name(name_id_search)
                if results:
                    print(f"\nSe found {len(results)} regist(s):")
                    for r in results:
                        read_student(r)
                else:
                    print("=> No student with that name were found.")
                
        elif op == '4':
            print("\n--- update student ---")
            id_valor = ask_integer("Enter the student ID for an update: ")
            
            if search_student_id(id_valor) is not None:
                print(f"Entering new data for the ID: {id_valor}")
                nuevos_datos = ask_datos(id_proporcionado=id_valor)
                actualizado = update_student_json(id_valor, 'id', nuevos_datos)
                if actualizado:
                    print("\n=> The student data was successfully updated")
                else:
                    print("\n=> Internal update error.")
            else:
                print("=> Error: No student with this ID was found for update.")
                
        elif op == '5':
            print("\n--- delete student ---")
            id_valor = ask_integer("Enter the student ID to delete: ")
            if search_student_id(id_valor) is not None:
                while True:
                    seguro = input(f"¿Are you sure you want to delete the ID? {id_valor}? (yes/no): ").lower()
                    if seguro in ['yes', 'no']:
                        break
                    
                if seguro == 'yes':
                    delete = delete_student_json(id_valor, 'id')
                    if delete:
                        print("\n=> ¡student delete from system!")
                    else:
                        print("\n=> There was an error while deleting..")
                else:
                    print("\n=> Canceled operation.")
            else:
                print("=> Error:No student with this ID was found to delete.")
        elif op == '6':
            print("\n¡Thank you for using the student management system!")
            break
            
        else:
            print("\n=> Error: Por favor, ingrese un número de opción válido (1-6).")

if __name__ == "__main__":
    iniciar_sistema()
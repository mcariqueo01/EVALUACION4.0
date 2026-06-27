listatareas=[]
def mostrar_menu():
  print("=====================MENU PRINCIPAL===============")
  print()
  print("1. Agregar tarea")
  print("2. Buscar tarea")
  print("3. Eliminar tarea")
  print("4. Actualizar estado")
  print("5. Mostrar tareas")
  print("6. Salir")
  print()
  print("==================================================")

def leer_opcion():
  while True:
    opcion=int(input("seleccione opcion del 1 al 6:  "))
    try:
      if opcion>=1 and opcion <=6:
       return opcion
      else:
       print("opcion invalida, intente nuevamente") 

    except ValueError:
      print("opcion invalida, intente nuevamente")

def validar_nombre_tarea(descripcion):
  if descripcion.strip()!="":
    return True   
  else:
    return True

def validar(descripcion):
  if descripcion.strip()!="":
    print("error, descripcion no puede estar vacia ")
    return False
  else:
    return True

def validar_prioridad (prioridad):
  if prioridad>=1 and prioridad <=10:
    return True
  else:
    print("error, prioridad debe estar entre el 1 y el 10")
    return False

def validar_tiempo (tiempo):
  if tiempo>0:
    return True
  else:
    print("tiempo debe ser mayor a cero")
    return False

def agregar_tarea(lista):
  descripcion=str(input(" agregue descripcion de la tarea "))
  prioridad=int(input("indique prioridad del 1 al 10 "))
  tiempo=float(input("ingrese tiempo estimado de tarea a realizar "))

  if validar_nombre_tarea(descripcion) and validar_prioridad (prioridad) and validar_tiempo (tiempo):
    nueva_tarea={
        "descripcion": descripcion,
        "prioridad": prioridad,
        "tiempo_estimado": tiempo,
        "estado_tarea": False
    }
    lista.append(nueva_tarea)
    print("la tarea se agregó correctamente ")

  else:
    print("no se pudo agregar la tarea ")

def buscar_tarea(lista,tarea):
  posicion=0
  for i in lista:
    if i["descripcion"]==tarea:
      return posicion
    posicion+=1
  return -1

def actualizar_estado_tareas(lista):
  for tarea in lista:
    if tarea["prioridad"] >= 5:
      tarea["estado_tarea"] = True
    else:
      tarea["estado_tarea"] = False

def mostrar_tareas(lista):
    actualizar_estado_tareas(lista)
    if len (lista) == 0:
        print("No hay tareas en la lista.")
        return
    print("===================Lista de tareas==============")
    for tarea in lista:
         print()
         print(f"Descripcion: {tarea['descripcion']}")
         print(f"Prioridad: {tarea['prioridad']}")
         print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
         print(f"Estado: {'Completada' if tarea['estado_tarea'] else 'Pendiente'}")
         print()

while True:
  mostrar_menu()
  opcion=leer_opcion()
  if opcion==1:
    agregar_tarea(listatareas)
  elif opcion==2:
    tarea=str(input("ingrese descripcion de la tarea a buscar "))
    posicion=buscar_tarea(listatareas,tarea)
    if posicion!=-1:
      print("la tarea se encuentra en la posicion ",posicion)
    else:
      print("la tarea no se encuentra en la lista ")
  elif opcion==3:
    tarea=str(input("ingrese descripcion de la tarea a eliminar:  "))
    posicion=buscar_tarea(listatareas,tarea)
    if posicion!=-1:
      listatareas.pop(posicion)
      print("la tarea se elimino correctamente ")
    else:
      print("la tarea no se encuentra en la lista ")
  elif opcion==4:
    actualizar_estado_tareas(listatareas)
    print("El estado de las tareas se actualizo correctamente ")
  elif opcion==5:
    mostrar_tareas(listatareas)
  elif opcion==6:
    print()
    print("“Gracias por usar el sistema. Vuelva Pronto”")
    print()
    break
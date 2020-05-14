import sys
import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error

def menu():
    print("1 para ver a los usuarios")
    print("2 para subir calificaciones")
    print("3 para ver la estadistica descriptiva de las materias")
    print("4 para ver la estadistica descriptiva por alumno")
    print("5 para salir")
    
def Dar_Calificaciones(Matricula, NombreMateria, Calificacion):
    try:
        with sqlite3.connect("Evidencia5.db") as conn:
            mi_cursor=conn.cursor()
            valores={"Matricula":Matricula,"NombreMateria":NombreMateria, "Calificacion":Calificacion}
            mi_cursor.execute("INSERT INTO Calificacion VALUES(:Matricula,:NombreMateria,:Calificacion)", valores)
            print("Registro agregado exitosamente")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
  

def EstadisticasdeMaterias(NombreMateria):
    try:
         with sqlite3.connect("Evidencia5.db") as conn:
            mi_cursor=conn.cursor()
            materia={"NombreMateria":NombreMateria}
            mi_cursor.execute("SELECT AVG(Calificacion), MAX(Calificacion), MIN(Calificacion), NombreMateria  FROM Calificacion WHERE NombreMateria = :NombreMateria;", materia)
            registros=mi_cursor.fetchall()
            print("(Promedio de la Calificacion, Maxima Calificacion, Minima Calificacion, Nombre de la Materia)")
            print("*" * 100)
            for AVG, MAX, MIN, NombreMateria in registros:
                print(f"{AVG}\t\t\t\t{MAX}\t\t    {MIN}\t\t\t{NombreMateria}")
                     
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")


def EstadisticasdeAlumno(Matricula):
    try:
        with sqlite3.connect("Evidencia5.db") as conn:
            mi_cursor=conn.cursor()
            Matricula={"Matricula":Matricula}
            mi_cursor.execute("SELECT AVG(Calificacion), MAX(Calificacion), MIN(Calificacion), COUNT(Calificacion), SUM(Calificacion), Matricula FROM Calificacion WHERE Matricula = :Matricula;", Matricula)
            registros=mi_cursor.fetchall()
            print("(Promedio de la Calificacion, Maxima Calificacion, Minima Calificacion, Total de Calificaciones, Suma de Calificaciones, Matricula del Alumno)")
            print("*" * 150)
            for AVG, MAX, MIN, COUNT, SUM, Matricula in registros:
                print(f"{AVG}\t\t\t\t{MAX}\t\t   {MIN}\t\t \t{COUNT}\t\t\t{SUM}\t\t\t{Matricula}")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

 
Proceso=True
while Proceso == True:
    menu()
    Proceso2 = int(input("¿Que quieres realizar?:"))
   
    if Proceso2 == 1:
        try:
            with sqlite3.connect("Evidencia5.db") as conn:
                mi_cursor=conn.cursor()
                mi_cursor.execute("SELECT Nombre FROM Alumnos")
                registros=mi_cursor.fetchall()
        
                for registro in registros:
                    print(registro)
            
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        
    
    
    elif Proceso2 == 2:
        Matricula= int(input("Matricula a agregar: "))
        NombreMateria= input("Materia a calificar: ")
        Calificacion = int(input("Calificacion en la materia: "))
        Dar_Calificaciones(Matricula, NombreMateria, Calificacion)
        print("Se concluyó la carga de registros")



    elif Proceso2 == 3:
        NombreMateria= input("De que materia gustas ver las estadisticas: ")
        EstadisticasdeMaterias(NombreMateria)
       
        
    elif Proceso2 == 4:
        Matricula= input("De que alumno quieres ver las estadisticas: ")
        EstadisticasdeAlumno(Matricula)
        print("Fin de las estadisticas por alumnos")
        
    elif Proceso2 == 5:
        print("FIN DEL PROGRAMA")

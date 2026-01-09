from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

#--------Empezamos con la configuración de la app-----------

# Ponemos el titulo, la descripcion y version (lo que vemos en docs)
app=FastAPI(
    title="API de una librería",
    description="Proyecto portfolio API REST para gestionar los libros en una librería",
    version="1.0"
)


#-----------Modelo de datos (Pydantic)----------------
class Libro(BaseModel):
    id:int
    titulo:str
    autor:str
    paginas:int
    precio:int


#------------Creamos una base de datos simulada (en RAM) --------------
libros_db=[
    {"id":1 , "titulo":"la prueba 1" ,"autor":"anonimo" ,"paginas":10 ,"precio":1, "coste_real":0},  #hemos añadido "coste real para probar el filtrado"
    {"id":2 , "titulo":"libro de muestra 2" ,"autor":"sin autor" ,"paginas":20 ,"precio":2},
    {"id":3 , "titulo":"pendiente de nombre 3" ,"autor": "carente" ,"paginas":30 ,"precio":3}
]



#---------------------Rutas (ENDPOINTS)-----------------
@app.get("/", tags=["inicio"])
def home():
    return{"mensaje":"Bienvenido al portfolio de API librería"}


@app.get("/libros",response_model=List[Libro], tags=["libros"])
def obtener_listado_libros():
    """Devuelve la lista de todos los libros almacenados en la db.
    
    Nota: gracias al response_model=List[Libro], fastAPI filtra los datos aunque exista el campo 'coste_real',
    la API lo elimina de la respuesta porque no esta definido en el esquema 'Libro' creado previamente    
    
    """    
    return libros_db


@app.get("/libros/{id_libro}", response_model=Libro, tags=["libros"])
def obtener_libro_concreto(id_libro:int):
    # Buscamos un libro por su id unico
    for libro in libros_db:
        if id_libro==libro["id"]:
            return libro
    # En caso de buscar un libro no contenido en la db lanzamos un error
    raise HTTPException(status_code=404, detail="libro no encontrado")


@app.post("/libros", response_model=Libro, tags=["Libros"])
def crear_libro(nuevo_libro: Libro):
    # Añade un nuevo libro a la db
    for libro in libros_db:
        if nuevo_libro.id==libro["id"]:
            raise HTTPException(status_code=400, detail="el ID del libro ya existe")
        # Asegura que no se introduzca un ID ya recogido en la db
    
    libros_db.append(nuevo_libro.dict())
    return nuevo_libro


@app.put("/libros/{id_libro}", response_model=Libro, tags=["Libros"])
def actualizar_libro(id_libro:int, libro_actualizado:Libro):
    #Actualiza la informacion completa de un libro existente
    for index, libro in enumerate(libros_db):
        if libro["id"]==id_libro:
            libros_db[index]=libro_actualizado.dict()
            # Se asegura que el ID se mantenga aunque el usuario intente cambiarlo
            libros_db[index]["id"]=id_libro
            return libros_db[index]
    raise HTTPException(status_code=404, detail="libro no encontrado")


@app.delete("/libros/{id_libro}", tags=["Libros"])
def eleminar_libro(id_libro:int):
    # Elimina un libro de la db
    for libro in libros_db:
        if id_libro==libro["id"]:
            libros_db.remove(libro)
            return {"mensaje": "libro eliminado con exito"}
    raise HTTPException(status_code=404, detail="libro no encontrado")
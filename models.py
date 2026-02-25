# models.py

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def to_tuple(self):
        return (self.__id, self.__nombre, self.__cantidad, self.__precio)


class Inventario:
    def __init__(self):
        # Diccionario → clave: ID, valor: objeto Producto
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad, precio):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
            self.productos[id].set_precio(precio)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        return list(self.productos.values())
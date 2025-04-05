class Producto:
    def __init__(self, nombre, precio, vendedor, calificacion, fecha):
        self.nombre = nombre
        self.precio = precio
        self.vendedor = vendedor
        self.calificacion = calificacion
        self.fecha  = fecha

    def __repr__(self):
        return f"Producto(nombre='{self.nombre}', precio='{self.precio}', vendedor='{self.vendedor}', calificacion='{self.calificacion}')"


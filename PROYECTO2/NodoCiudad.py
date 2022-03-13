class NodoCiudad():
    def __init__(self,nombreciudad, unidadesciviles, row, column):
        self.nombreciudad=nombreciudad
        self.unidadesciviles=unidadesciviles
        self.row=row
        self.column=column
        self.siguiente=None
        self.anterior=None
        self.size=0

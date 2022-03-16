from MatrizDispersa import MatrizDispersa

class NodoCiudad():
    def __init__(self,nombreciudad, row, column):
        self.nombreciudad=nombreciudad
        self.row=row
        self.column=column
        self.siguiente=None
        self.anterior=None
        self.id=0
        self.MatrizDispersa=MatrizDispersa()

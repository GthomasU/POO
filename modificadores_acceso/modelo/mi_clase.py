class MiClase:
    def __init__(self):
        self.atributo_publico : int = 0
        self._atributo_protegido: str = 'atributo_protegido' 
        self.__atributo_privado: float = 0.0

    def __metodo_privado(self):
        pass

    def _metodo_protegido(self):
        pass

    @classmethod
    def metodo_de_clase(cls):
        pass
    @staticmethod
    def metodo_estatico():
        pass
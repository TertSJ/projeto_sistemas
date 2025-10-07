from model.Calcular import Calcular

class Controlador:
    def redirecionar(self,nome:str, num_1:int, num_2:int):
        controle = Calcular()
        return controle.calc(nome,num_1,num_2)
        
class Calcular:
    
    def calc(self, name:str, a:int , b:int):
        metodo = getattr(self, name)
        return metodo(a,b)


    def soma(self, a:int, b:int ):
        return a+b


    def subtracao(self, a:int, b:int ):
        return a-b
    

    def multiplicacao(self, a:int, b:int ):
        return a*b


    def divisao(self, a:int, b:int ):
        if (b==0):
            return 0
        return a/b

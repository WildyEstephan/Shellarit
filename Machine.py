__author__ = 'wildy'


class Machine():
    salida = []

    pila = []
    OPERADORES = {

        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        ':': 0,

    }

    def __init__(self, sal):
        self.salida = sal

    def suma(self, izq, der):

        return der + izq

    def resta(self, izq, der):

        return der - izq

    def multi(self, izq, der):

        return der * izq

    def divi(self, izq, der):

        return der / izq


    def ejecutar(self):

        for tk in self.salida:
            if ( not( self.OPERADORES.has_key(tk) ) ):
                self.pila.append(int(tk))
            elif( tk == "+" ):
                self.pila.append(self.suma(self.pila.pop(),self.pila.pop()))
            elif( tk == "-"):
                self.pila.append(self.resta(self.pila.pop(),self.pila.pop()))
            elif( tk == "*"):
                self.pila.append(self.multi(self.pila.pop(),self.pila.pop()))
            elif( tk == "/"):
                self.pila.append(self.divi(self.pila.pop(),self.pila.pop()))

        print 'El resultado es: %s' % self.pila[0]

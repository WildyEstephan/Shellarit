__author__ = 'wildy'

import Machine

class ShuntingYard():

    salida = [] ## para guardar la salida, es una cola
    pila = [':'] ## para guardar los operadores en el algoritmo


    ## Define el valor de precedencia de los operadores
    OPERADORES = {

        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        ':': 0,

    }

    ##iniciamos
    def __init__(self, expresion):
        self.parser(expresion)


    # agrega los elementos obtenidos en de la pila a la cola de salida
    def mandarCola(self):
        self.pila.reverse()
        for token in self.pila:
            if ( not token == ':' ):
                self.salida.append(token)

    ## obtiene el valor de la ultimo valor en la pila
    ## si este es igual o menor presedencia con el dado en la llamada
    ## se saca de la pila y se manda a la salida
    ## si es mayor que el que esta se agrega al tope sin sacar ninguno
    def insertar_pila(self, operador):

        ## si la pila no tiene items entonces se guarda el operador, luego retorna
        # if ( self.OPERADORES[self.pila] == None ):
        #     self.pila.append(operador)
        #     return

        ## mientras la jerarquia del operador dado sea menor o igual al del tope de la pila
        ## se saca y envia a la salida el tope de la pila
        ## sino se guarda al tope de la pila el operador
        while ( self.OPERADORES[operador] <= self.OPERADORES[ self.pila[len(self.pila) - 1] ] ):
            self.salida.append(self.pila.pop())
        else:
            self.pila.append(operador)


    ## Esto escanea los tokens dados y ejecuta el algoritmo de Shunting Yard
    def scan(self, tokens):
        print 'Escaneando'

        for token in tokens:
            if ( self.OPERADORES.has_key(token) ):
                self.insertar_pila(token)
            else:
                self.salida.append(token)

    ## convierte a tokens la entrada del usuario
    def parser(self, entrada):

        print 'Parseando'

        ## convierte a una lista dividida por espacios
        tokens = entrada.split(' ')
        print 'Estos son sus tokens'
        print 'Tiene %s tokens' % (len(tokens))

        for token in tokens:
            print token

        self.scan(tokens)

st = ShuntingYard(raw_input( 'Escriba una expresion aritmetica separada por espacios '))
st.mandarCola()
print 'el postfijo es %s' % ( st.salida )
man = Machine.Machine(st.salida)
man.ejecutar()
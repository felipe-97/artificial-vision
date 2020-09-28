importar sistema  operativo
de  randint de importación aleatoria  , uniforme  
  
acumulado  =  0
acumulado2  =  0
i  =  0
opcion  =  0
valor  =  0     

def  proceso ():
    casillas  = []
    print ( "Por Favor, Ingrese el numero de jugadores minimo 2 maximo 5:" )
    j =  int ( entrada ())
    si  j  <  2  o  j  >  5 :
        print ( "Digite un numero de jugadores (2-5)" )
        imprimir ( " PRESIONE ENTER PARA CONTINUAR " )
        entrada ()
        regreso
    para  i  en el  rango ( 1 , j + 1 ):
        Datos  =  0
        casillas . añadir ( Datos )
    i = 0

    mientras que  casillas [ i ] <=  valor :
        os . sistema ( "cls" )
        dado1  =  randint ( 1 , 6 )
        dado2  =  randint ( 1 , 6 )
        print ( "Jugador" , i + 1 , "Sacao:" , dado1 , "y" , dado2 )
        casillas [ i ] =  casillas [ i ] +  dado1  +  dado2
        print ( "Jugador" , i + 1 , "Acomulado de:" , casillas [ i ])
        print ( "Resultados Totales:" , casillas )
        input ( "Presiona enter para el turno del siguiente jugador" )
        si  casillas [ i ] > =  valor :
            print ( "El Jugador" , i + 1 , "Gano" )
            entrada ()
            rotura
        y  =  y + 1
        si  i ==  j :
            i = 0

mientras que  opcion  ! = 4 :
    os . sistema ( "cls" )
    imprimir ( "CARRERA DE DADOS " )
    print ( "Por Favor, Ingrese un numero del 1 al 3 para comenzar el juego:" )
    print ( "[1] Nivel Básico De 50 Puntos" )
    print ( "[2] Nivel Medio De 70 Puntos" )
    print ( "[3] Nivel Medio De 100 Puntos" )
    imprimir ( "[4] Salir" )
    opcion =  int ( entrada ())

    si  opcion ==  1 :
        print ( "Nivel Básico De 50 Puntos" )
        imprimir ( "--------------------------" )
        valor  =  50
        proceso ()
    elif  opcion ==  2 :
        print ( "Nivel Medio De 70 Puntos" )
        imprimir ( "--------------------------" )
        valor  =  70 
        proceso ()
    elif  opcion ==  3 :
        print ( "Nivel Avanzado De 100 Puntos" )
        imprimir ( "--------------------------" )
        valor  =  100 
        proceso ()
    elif  opcion  ==  4 :
        print ( "-------------------------- Gracias por jugar--------------------------" )
        print ( "-------------------------- Realizado por: Felipe Lopez -------------------------- " )
        salida  
    otra cosa :
        imprimir ( "EL NUMERO QUE INGRESO ES INVALIDO " )
        imprimir ( "PRESIONE ENTER PARA CONTINUAR " )
        entrada ()
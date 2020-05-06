def main(  ):
	
	seed = int( input( 'Inserte valor de semilla: ' ) )
	
	pseudorandomNumber( seed, generateTer ( seed ) )

def generateTer( seed ):
	
	#Datos base
	modulo = 9
	multiplicador = 7
	incremento = 4	
	
	# Impresión de historial
	print( "( ( {} * {} ) + {} ) % {} ".format( multiplicador, seed, incremento, modulo ) )
	
	#Retorno de valor n + 1
	return ( ( multiplicador * seed ) + incremento ) % modulo 

def pseudorandomNumber( seed, n ):

	# Declaración de lista de números
	nums = [  ]
	
	# Anexo del valor de inicio
	nums.append( n )

	# Generador de números
	while ( seed != n ):
		
		n = generateTer( n )
		
		nums.append( n )
	
	#Impresión de lista
	print( nums )
	
if __name__ == '__main__':

    main()

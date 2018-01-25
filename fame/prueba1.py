import commands

comando = 'node malware-jail/jailme.js malware-jail/facturas/c410086a1075dc1210aa7e2ff8f3040d860ca7c98e8805ff5e29b4c1617cbce4.js'

respuesta = commands.getoutput(comando)

#Recogemos los Run() de la salida
arrayLines = respuesta.splitlines()
for line in arrayLines:
	if line.find('Run') > 0:
		print line

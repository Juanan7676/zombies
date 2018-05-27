import sys, pygame, time, math, random, rungekutta
from pygame.locals import * 
from pygame import time as pytime


ANCHO = 640
ALTO = 480

alpha = 0.005 # Natalidad humanos
beta = 0.0006 # Infección
delta = 0.0001 # Muerte natural humanos
xi = 0.009 # Resurrección
alpha2 = 0.0005 # Muerte por humanos de los zombies
sigma = 0.004 # Muerte natural zombies
capacidad = 10000

tmax = 100



def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except (pygame.error, message):
		raise (SystemExit, message)
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image

def main():
	screen = pygame.display.set_mode((ANCHO, ALTO))
	pygame.display.set_caption("Zombies")
	
	fuente = pygame.font.SysFont("Calibri",25)

	palabra1 = fuente.render("Humanos: ", 0, (255,255,255))
	palabra2 = fuente.render("Zombies: ", 0, (255,255,255))
	palabra3 = fuente.render("Muertos: ", 0, (255,255,255))
	
	s0,r0,z0,dia = 750,0,5,0
	espera = 1

	sa,za,ra = s0,r0,z0

	soluciones = rungekutta.runge_kutta(s0,z0,r0,tmax,[alpha,beta,delta,xi,alpha2,sigma,capacidad])
	humano = load_image("images/s.gif",True)
	zombie = load_image("images/z.gif",True)
	muerto = load_image("images/r.gif",True)
	isla = load_image("images/isla.jpeg",False)
	# Bucle principal
	while dia < tmax:
		screen.blit(isla,(0,0))
		diastr = fuente.render("Día " + str(dia),1,(255,255,255))
		sstr = fuente.render(str(math.floor(soluciones[0][dia*10])),1,(80,80,255))
		zstr = fuente.render(str(math.floor(soluciones[1][dia*10])),1,(255,20,20))
		rstr = fuente.render(str(math.floor(soluciones[2][dia*10])),1,(128,128,128))	
		vstr = fuente.render("Velocidad x" + str(1/espera),1,(255,255,255))
		var_s = math.floor(soluciones[0][dia*10]) - sa
		var_z = math.floor(soluciones[1][dia*10]) - za
		var_r = math.floor(soluciones[2][dia*10]) - ra

		screen.blit(diastr, (20,20))
		screen.blit(palabra1, (20,60))
		screen.blit(sstr, (120,60))
		screen.blit(palabra2, (20,100))
		screen.blit(zstr, (120,100))
		screen.blit(palabra3, (20,140))
		screen.blit(rstr, (120,140))
		screen.blit(vstr, (ANCHO - 150, 20))
		if (var_s >= 0) :screen.blit(fuente.render("(+"+str(var_s)+")",1,(255,164,32)),(160,60))
		else: screen.blit(fuente.render("("+str(var_s)+")",1,(255,0,0)),(160,60))
		if (var_z >= 0) :screen.blit(fuente.render("(+"+str(var_z)+")",1,(255,164,32)),(160,100))
		else: screen.blit(fuente.render("("+str(var_z)+")",1,(255,0,0)),(160,100))
		if (var_r >= 0) :screen.blit(fuente.render("(+"+str(var_r)+")",1,(255,164,32)),(160,140))
		else: screen.blit(fuente.render("("+str(var_r)+")",1,(255,0,0)),(160,140))

		sa,za,ra = math.floor(soluciones[0][dia*10]),math.floor(soluciones[1][dia*10]),math.floor(soluciones[2][dia*10])
		
		humanos = math.floor(soluciones[0][dia*10])//10
		if (humanos > 50): humanos = 50
		k = 0
		while k < humanos:
			screen.blit(humano, (ANCHO / 2 - 80+16*(k%10),130+k//10*12))
			k += 1

		humanos = math.floor(soluciones[1][dia*10])//10+1
		if (humanos > 100): humanos = 100
		
		k = 0
		while k < humanos:
			screen.blit(zombie, (ANCHO / 2 - 150+16*(k%20),220+k//20*12))
			k += 1
		
		humanos = math.floor(soluciones[2][dia*10])//10
		k = 0
		while k < humanos:
			screen.blit(muerto, (ANCHO / 2 - 120+12*(k%10),300+k//10*10))
			k += 1
		
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
			if eventos.type == KEYDOWN:
				if eventos.key == K_UP and espera > 1.0/8:
					espera /= 2
				elif eventos.key == K_DOWN and espera < 1:
					espera *= 2

		pygame.display.flip()
		time.sleep(espera)
		dia += 1
	
	return 0

if __name__ == '__main__':
	pygame.init()
	main()

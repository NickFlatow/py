import pygame

print(pygame.version.ver);

def main():
	running = True
	while running:
		# event listeners
		for event in pygame.event.get():
			# if event is of type QUIT or Esc is pressed
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
				load_img('123')
			elif event.type == pygame.KEYUP and event.key == pygame.K_1:
				load_img('1')
			elif event.type == pygame.KEYUP and event.key == pygame.K_2:
				load_img('2')
				
		#destroy()
				
def load_img(n):
	img = pygame.image.load('{0}.png'.format(n))
	screen.blit(img,(0,0))
	pygame.display.update()
	
def destroy():
	print("cleanup")
	pygame.quit()
					

if __name__ == '__main__': #program start
	pygame.init()
	pygame.display.set_caption("1-2-3")
	screen = pygame.display.set_mode((400,400))
	try:
		main()
	except KeyboardInterrupt: # When Ctlr-C is pressed
		destroy()
	
	
	

import pygame

wn = pygame.display.set_mode((500,500))
arrow = ("   ..   ",
         "   ..   ",
         "        ",
         "..    ..",
         "..    ..",
         "        ",
         "   ..   ",
         "   ..   ")
x,a = pygame.cursors.compile(arrow)
print(a,x)
the_cursor = ((8,8),(0,0),x,a)

while True:
    pygame.mouse.set_cursor(*the_cursor)
    pygame.display.update()

import pygame


def cursor2ascii(cursor):
    """
    Returns a cursor represented in ascii format where the 'W' represent the white pixels, the 'B'
    represent the black pixels, and the '.' represent the transparent pixels.
    """

    size, __, xormasks, andmasks = cursor
    width, height = size
    byte_cols = width / 8

    text = ''

    text += 'xormasks:\n'
    for idx, i in enumerate(xormasks):
        text += '{:08b}'.format(i).replace('0', '.').replace('1', 'B')
        if idx % byte_cols:
            text += '\n'

    text += '\nandmasks:\n'
    for idx, i in enumerate(andmasks):
        text += '{:08b}'.format(i).replace('0', '.').replace('1', 'W')
        if idx % byte_cols:
            text += '\n'

    return text


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Custom cursor')

    # sets the window size
    pygame.display.set_mode((400, 400))

    # custom cursor string
    thickarrow_strings = (
        "XX                      ",
        "XXX                     ",
        "XXXX                    ",
        "XX.XX                   ",
        "XX..XX                  ",
        "XX...XX                 ",
        "XX....XX                ",
        "XX.....XX               ",
        "XX......XX              ",
        "XX.......XX             ",
        "XX........XX            ",
        "XX........XXX           ",
        "XX......XXXXX           ",
        "XX.XXX..XX              ",
        "XXXX XX..XX             ",
        "XX   XX..XX             ",
        "     XX..XX             ",
        "      XX..XX            ",
        "      XX..XX            ",
        "       XXXX ......      ",
        "       XX XXXXXXXXXX    ",
        "                        ",
        "                        ",
        "                        "
    )

    # compiles the string
    xormasks, andmasks = pygame.cursors.compile(thickarrow_strings)

    # cursor size
    size = (24, 24)

    # point of selection of the cursor
    hotspot = (0, 0)

    # custom cursor properties
    cursor = (size, hotspot, xormasks, andmasks)
    

    # sets the cursor
    pygame.mouse.set_cursor(*cursor)

    # infinite loop
    while True:
        # gets a single event from the event queue
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

    # finalizes Pygame
    pygame.quit()



main()

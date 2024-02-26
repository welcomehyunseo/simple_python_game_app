import pygame

if __name__ == "__main__":
    print("Hello, World!")

    # pygame setup
    pygame.init()
    icon_img = pygame.image.load("icon.png")
    pygame.display.set_icon(icon_img)
    pygame.display.set_caption("Simple App")
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        # ...

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
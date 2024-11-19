import pygame
import random

def main():
    try:
        pygame.init()
        
        # Set up screen and grid dimensions
        SCREEN_WIDTH = 640  # 20 squares * 32 pixels
        SCREEN_HEIGHT = 512  # 16 squares * 32 pixels
        GRID_SIZE = 32

        # Create the screen
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-A-Mole")

        # Load and scale the mole image
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (GRID_SIZE, GRID_SIZE))

        # Initial mole position (top-left corner)
        mole_x, mole_y = 0, 0

        # Set up the clock for controlling the frame rate
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Check if the mole is clicked
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        # Move mole to a random grid position
                        mole_x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
                        mole_y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)

            # Fill the screen with a background color
            screen.fill("light green")

            # Draw the grid
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))

            # Draw the mole at its current position
            screen.blit(mole_image, (mole_x, mole_y))

            # Update the display
            pygame.display.flip()
            clock.tick(60)  # Limit to 60 frames per second

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()



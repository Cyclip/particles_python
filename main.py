import numpy as np
import pygame

import positions
import colours

# Simulation constants
PARTICLE_COUNT = 100
X_SPAN = (0, 100)
Y_SPAN = (0, 100)
COLOUR_SPAN = (0, 3)

# Graphics constants
SCREEN_SIZE = (1200, 750)
BACKGROUND_COLOUR = (0, 0, 0)
PARTICLE_SIZE = 3


def determinePosition(pos):
    """Determine the position of a particle on the screen.

    Args:
        pos (np.array): Position array

    Returns:
        (float, float): x, y graphical coordinates
    """
    x = pos[0] * SCREEN_SIZE[0] / X_SPAN[1]
    y = pos[1] * SCREEN_SIZE[1] / Y_SPAN[1]
    return (x, y)


def main():
    # Create particles
    particles = np.zeros(PARTICLE_COUNT, dtype=[('position', float, 2),
                                                ('velocity', float, 2),
                                                ('colour', float, 1)])

    # Set random positions
    positions.update_random(particles, X_SPAN, Y_SPAN)

    # Set random colours
    colours.update_random(particles, COLOUR_SPAN)

    # Get colour hashmap
    colourMap = colours.get_colour_map(COLOUR_SPAN)

    # Display particles
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BACKGROUND_COLOUR)

        # Draw particles
        for particle in particles:
            # Get particle details
            x, y = particle['position']
            colour = particle['colour']

            # Draw particle
            pygame.draw.circle(
                screen,
                colourMap[colour],
                determinePosition((x, y)),
                PARTICLE_SIZE
            )

        # Update display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
import numpy as np
import pygame

import positions
import colours
import behaviour

# Simulation constants
PARTICLE_COUNT = 500
X_SPAN = (0, 700)
Y_SPAN = (0, 700)
COLOURS = 7
MIN_DISTANCE = 1
MAX_VELOCITY = 100
RESISTANCE = 0.9
NEARBY_DISTANCE = 40

# Graphics constants
SCREEN_SIZE = (1200, 750)
BACKGROUND_COLOUR = (0, 0, 0)
PARTICLE_SIZE = 2


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
                                                ('colour', int, 1)])

    # Set random positions
    positions.update_random(particles, X_SPAN, Y_SPAN)

    # Set random colours
    colours.update_random(particles, COLOURS)

    # Get colour hashmap
    colourMap = colours.get_colour_map(COLOURS)

    # Create behaviour matrix
    behaviourMatrix = behaviour.new_behaviour_matrix(COLOURS)

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

        # Update particles
        behaviour.update(
            particles,
            behaviourMatrix,
            X_SPAN,
            Y_SPAN,
            MIN_DISTANCE,
            MAX_VELOCITY,
            RESISTANCE,
            NEARBY_DISTANCE
        )

        # print("Position", particles['position'])

        # Clear screen
        screen.fill(BACKGROUND_COLOUR)

        # Split span into 10
        xSpan = X_SPAN[1] / 10
        ySpan = Y_SPAN[1] / 10

        # Draw grid
        for x in range(0, 10):
            pygame.draw.line(
                screen,
                (12, 12, 12, 128),
                determinePosition((xSpan * x, 0)),
                determinePosition((xSpan * x, Y_SPAN[1]))
            )

        for y in range(0, 10):
            pygame.draw.line(
                screen,
                (12, 12, 12, 128),
                determinePosition((0, ySpan * y)),
                determinePosition((X_SPAN[1], ySpan * y))
            )

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

        # Draw colour legend
        for x in range(0, COLOURS):
            # Draw colour
            pygame.draw.circle(
                screen,
                colourMap[x],
                (65 + x * 50, 15),
                10
            )
        
        # and for y
        for y in range(0, COLOURS):
            # Draw colour
            pygame.draw.circle(
                screen,
                colourMap[y],
                (15, 50 + y * 50),
                10
            )

        # Draw matrix onscreen
        for x in range(0, COLOURS):
            for y in range(0, COLOURS):
                attraction = behaviourMatrix[x][y]

                # If attraction is positive, draw green
                if attraction > 0:
                    colour = (0, 255, 0)
                else:
                    colour = (255, 0, 0)

                # Draw text
                text = f"{attraction:.2f}"

                # Draw
                screen.blit(
                    pygame.font.SysFont('monospace', 15).render(text, True, colour),
                    (40 + x * 50, 40 + y * 50)
                )

        # Update display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
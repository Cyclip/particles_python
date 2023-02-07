import numpy as np

def update_random(particles, colourSpan):
    """Set all particles to a random colour within ranges.

    Args:
        particles (np.array): Array of particle details
        colourSpan (tuple[float, float]): Range of colour
    """
    # Generate random colour integer
    colour = np.random.randint(colourSpan[0], colourSpan[1], len(particles))

    # Set colours
    particles['colour'] = colour


def get_colour_map(colourSpan):
    """Get a hashmap of colours.

    Args:
        colourSpan (tuple[float, float]): Range of colour

    Returns:
        dict[int, (int, int, int)]: Colour hashmap
    """
    # Create colour map
    colourMap = {}

    # Add colours to map
    for i in range(colourSpan[0], colourSpan[1]):
        randomColour = np.random.randint(0, 255, 3)
        colourMap[i] = randomColour

    return colourMap
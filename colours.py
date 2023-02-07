import numpy as np

def update_random(particles, colourSpan):
    """Set all particles to a random colour within ranges.

    Args:
        particles (np.array): Array of particle details
        colourSpan (tuple[float, float]): Range of colour
    """
    # Generate random colour integer
    colour = np.random.randint(0, colourSpan, len(particles))

    # Set colours
    particles['colour'] = colour


def get_colour_map(colourSpan):
    """Get a hashmap of colours.

    Args:
        colourSpan (int): Number of colours

    Returns:
        dict[int, (int, int, int)]: Colour hashmap
    """
    # Create colour map
    colourMap = {}

    # Add colours to map
    for i in range(0, colourSpan):
        randomColour = np.random.randint(0, 255, 3)
        colourMap[i] = randomColour

    return colourMap
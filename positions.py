import numpy as np

def update_random(particles, xSpan, ySpan):
    """Set all particles to a random position within ranges.

    Args:
        particles (np.array): Array of particle details
        xSpan (tuple[float, float]): Range of x
        ySpan (tuple[float, float]): Range of y
    """
    # Gen random positions
    x = np.random.uniform(xSpan[0], xSpan[1], len(particles))
    y = np.random.uniform(ySpan[0], ySpan[1], len(particles))

    # Set positions
    particles['position'] = np.column_stack((x, y))
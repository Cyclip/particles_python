import numpy as np

def new_behaviour_matrix(colours):
    """Create a new behaviour matrix.

    A behaviour matrix determines how a particle will react to other particles
    based on their colour; whether they are attracted (+1), repelled (-1) or
    indifferent (0).
    
    Args:
        colours (int): Number of colours
    
    Returns:
        np.array: Behaviour matrix
    """
    # Create random matrix
    matrix = np.random.uniform(-1, 1, (colours, colours))

    return matrix


def update(particles, behaviour, xSpan, ySpan, minDistance, maxVelocity, resistance, nearbyDistance):
    """Update particles based on the behaviour matrix

    Args:
        particles (np.array): Particles data
        behaviour (np.array): Behaviour matrix
    """
    # Get colours
    colours = particles['colour']

    # Get velocities
    velocities = particles['velocity'] * resistance

    # Get positions
    positions = particles['position']

    # Update velocities
    for thisIndex in range(0, len(particles)):
        # Get nearby particles
        nearby = get_nearby(particles, positions[thisIndex], nearbyDistance)

        # Determine attraction/repulsion to nearby particles
        for nearbyIndex in range(0, len(nearby)):
            # Get colour
            colour = nearby[nearbyIndex]['colour']

            # Get velocity
            velocity = nearby[nearbyIndex]['velocity']

            # Get attraction/repulsion
            distance = np.linalg.norm(positions[thisIndex] - positions[nearbyIndex])
            attraction = getAttraction(behaviour, colours[thisIndex], colour, distance, minDistance)

            # Vector to particle
            vector = nearby[nearbyIndex]['position'] - positions[thisIndex]

            # Update velocity
            velocities[thisIndex] += vector * attraction * 0.01

        # Limit velocity
        if np.linalg.norm(velocities[thisIndex]) > maxVelocity:
            velocities[thisIndex] = velocities[thisIndex] / np.linalg.norm(velocities[thisIndex]) * maxVelocity
        
        # Update position and print change
        positions[thisIndex] += velocities[thisIndex]
    
    # Wrap all particles so it loops around the screen
    positions[positions < xSpan[0]] += xSpan[1] - xSpan[0]
    positions[positions > xSpan[1]] -= xSpan[1] - xSpan[0]

    positions[positions < ySpan[0]] += ySpan[1] - ySpan[0]
    positions[positions > ySpan[1]] -= ySpan[1] - ySpan[0]

    # Update particles
    particles['velocity'] = velocities
    particles['position'] = positions
    

def get_nearby(particles, position, radius):
    """Get nearby particles.

    Args:
        particles (np.array): Particles data
        position (np.array): Position of particle
        radius (float): Radius of nearby particles

    Returns:
        np.array: Nearby particles
    """
    # Get positions
    positions = particles['position']

    # Get distances
    distances = np.linalg.norm(positions - position, axis=1)

    # Get nearby particles
    nearby = particles[distances <= radius]

    return nearby


def getAttraction(behaviour, thisColour, otherColour, distance, minDistance):
    """Get the attraction between two particles.

    Args:
        behaviour (np.array): Behaviour matrix
        thisColour (int): Colour of particle
        otherColour (int): Colour of other particle
        minDistance (float): Minimum distance between particles

    Returns:
        float: Attraction
    """
    if distance < minDistance:
        # Too close, repel
        attraction = (1 / minDistance) * distance - 5
    else:
        # Get attraction
        attraction = behaviour[thisColour][otherColour]

    return attraction
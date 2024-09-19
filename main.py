
earth_acceleration = 9.81


def calc_gravitation_force(start, end, earth_acceleration):
    range = (end - start) * 2
    range = int(range)
    for i in range(range):
        force = earth_acceleration * (i / 2 + start)
        print(force)

calc_gravitation_force(2.5, 580, earth_acceleration)
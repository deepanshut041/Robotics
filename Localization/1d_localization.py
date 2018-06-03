class SDLocalization():

    def __init__(self, world, belief, measurement_sensor, motion_sensor):
        self.world = world
        self.belief = belief 
        self.measurement_sensor = measurement_sensor
        self.motion_sensor = motion_sensor

    def sense(self, measurement):
        for i in range(0, len(self.belief)):
            z = (self.world[i] == measurement)
            self.belief[i] = self.belief[i] * (z  * self.measurement_sensor[0] + (1-z) * self.measurement_sensor[1])
        belief_sum = sum(self.belief)
        for i in range(0, len(self.belief)):
            self.belief[i] = self.belief[i] / belief_sum

    def move(self):
        pass

if __name__ == "main":
    p=[0.2, 0.2, 0.2, 0.2, 0.2]
    world=['green', 'red', 'red', 'green', 'green']
    measurements = ['red', 'green']
    motions = [1, 1]
    pHit = 0.6
    pMiss = 0.2
    pExact = 0.8
    pOvershoot = 0.1
    pUndershoot = 0.1
    local = SDLocalization(world, p, [pHit, pMiss], [pUndershoot, pExact, pOvershoot])

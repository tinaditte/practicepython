from Robot import Robot
import random

class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " will take care of you!")

    def heal(self):
        Robot.health_level = random.uniform(Robot.health_level, 1)
        print(Robot.name + " has been healed by " + self.name + "!")

doc = PhysicianRobot("Dr. Frankenstein")
rob_list = []
for i in range(5):
    x = Robot("Marvin " + str(i))
    if x.needs_a_doc():
        print("health_level of " + x.name + " before healing: ", x.health_level)
        doc.heal(x)
        print("Current health_level of " + x.name + ": " + x.health_level)
    rob_list.append((x.name, x.health_level))

print(rob_list)

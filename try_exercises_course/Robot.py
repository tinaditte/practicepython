import random
class Robot:

    Three_Laws = (
        """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
        """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
        """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
        )

    def __init__(self, name=None,build_year=None):
        self.name = name
        #self.build_year = build_year
        self.health_level = random.random()

    #def __repr__(self):
    #    return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    #def __str__(self):
    #    return "Name: " + self.name + ", Build year: " + str(self.build_year)


    def say_hi(self):
        if self.name:
            print("Hi! I am " + self.name)
        else:
            print("Hi! I am a Robot without a name")
        #if self.build_year:
        #    print("I was build in " + str(self.build_year))
        #else:
        #    print("My year of creation is unknown")

    def needs_a_doc(self):
        if self.health_level < 0.8:
            return True
        else:
            return False

    # def set_name(self, name):
    #     self.name = name
    #
    # def get_name(self):
    #     return self.name
    #
    # def set_build(self, by):
    #     self.build_year = by
    #
    # def get_build(self):
    #     return self.build_year


# if __name__ == "__main__":
#     x = Robot("Marvin", 1979)
#
# x_repr = repr(x)
# print(x_repr, type(x_repr))
# new = eval(x_repr)
# print(new)
# print("Type of new: ", type(new))
#
# for number, text in enumerate(Robot.Three_Laws):
#     print(str(number+1) + ":\n" + text)

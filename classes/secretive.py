
class Secretive:

    @staticmethod
    def __inaccessible():
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()
s.accessible()

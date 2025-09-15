
class FunkyFace:
    def __init__(self, eyes="0", mouth="__"):
        self.eyes = eyes
        self.mouth = mouth

    def show(self):
        print("   /////   ")
        print("  | o o |  ".replace("o", self.eyes))
        print(" (   ^   ) ")
        print("  |  " + self.mouth + "  | ")
        print("   -----   ")

# Example usage
face1 = FunkyFace()
face1.show()

print("\nAnother funky face 😎")
face2 = FunkyFace(eyes="*", mouth="~~")
face2.show()

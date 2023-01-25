class MoveCharacter:
    def movebkwd(self):
        print("Move backward one step")

    def movefwd(self):
        print("Move frontward one step")

class JumpCharacter(): # When parentclass MoveCharacter was inherited here , the following error message is displayed -MoveCharacter TypeError: Cannot create a consistent method resolution
                        #order (MRO) for bases MoveCharacter, JumpCharacter , to avaoid that removed parentclass MoveCharacter from here
                        #refer -https://nsikakimoh.com/blog/how-to-fix-cannot-create-a-consistent-mro
    def onelevelup(self):
        print("Move one level up")

    def twolevelup(self):
        print("Move two level up")

class pokeman(MoveCharacter,JumpCharacter):
    def movebwd(self):
        print("pokeman is moving")

p=pokeman()
p.movebwd()
p.onelevelup()
print(pokeman.mro())

class Micky(MoveCharacter,JumpCharacter):
    pass

obj1 = Micky()
obj1.onelevelup()
obj1.movefwd()
obj1.movebkwd()
obj1.twolevelup()
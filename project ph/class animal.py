class Предмети:
    def існувати(self):
        print("існувати")
class Неживі(Предмети):
    pass
class Живі(Предмети):
    def розвивати(self):
        print("розвивається")
        
class Тварини(Живі):
    def дихати(self):
        print("дихає")
    def рухатися(self):
        print("рухаеться")
    def харчуватися_їжею(self):
        print("харчуватися їжею")
        
class Ссавці(Тварини):
    def готувати_дитинчат_молоком(self):
        print("годує дитинчат")

class Жирафи(Ссавці):
    def їсти_листя_з_дерев(self):
        print("їсть листя")
        
    def шукати_їжу(self):
        self.рухатися()
        print("я знайшов їжу!")
        self.харчуватися_їжею()

    
реджинальд= Жирафи()
гарольд= Жирафи()
реджинальд.рухатися()
корова=Ссавці()
корова.готувати_дитинчат_молоком()
корова.дихати()
реджинальд.існувати()

    
    
        

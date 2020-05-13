#Задание 2

class DelenieNaNull:
    def __init__(self, chislo_1, chislo_2):
        self.chislo_1 = chislo_1
        self.chislo_2 = chislo_2


    @staticmethod
    def Delenie_Null(chislo_1,chislo_2):
        try:
            return chislo_1 / chislo_2
        except:
            return f'На ноль делить нельзя'



print(DelenieNaNull.Delenie_Null(2,0))
print(DelenieNaNull.Delenie_Null(2,1))


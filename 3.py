#Задание 3



class Proverka:
    def __init__(self, *args):
        self.my_list = []


    def my_List(self):

        while True:
            try:
               chislo = int(input("Введите число --> "))
               self.my_list.append(chislo)
               print('Промежуточная проверка списка', self.my_list)
            except:
              print("!Недопустимое значение!")
              q = input('Ввкдите Q, если хоите законичть, или Enter для продолжения')
              if q == ('Q'):
                  print('Конечный вариант списка:', self.my_list)
                  return f'До свидания'
              else:
               print(try_except.my_List())




try_except = Proverka(1)
print(try_except.my_List())




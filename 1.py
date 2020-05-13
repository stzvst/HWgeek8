#Задание 1

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        print(my_date)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        day = int(my_date[0])
        month = int(my_date[1])
        year =  int(my_date[2])

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Проверка прошла успешно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Дата: {Data.extract(self.day_month_year)}'


today = Data('13 - 5 - 2020')
print(today)
print(Data.valid("11 - 11 - 2022"))
print(today.valid("11 - 13 - 2011"))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid('1 - 11 - 2000'))

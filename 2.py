school = {"1А" : 20, "1Б" : 31, "2А" : 25, "2Б" : 26, "3А" : 27, "6А" : 29}
children = 0
print(school)
print("выберите действие")
print("1) изменение количества учеников в одном из классов ")
print("2) добавление нового класса(с количеством учеников)")
print("3) удаление класса")
print("4) подсчет общего количества учащихся в школе")
choose = int(input())
if choose == 1:
   new_class = input("какой класс изменить?")
   count_children = input("Сколько человек?")
   if new_class not in school:
       print("такого класса нет в школе")
   else:
       school[new_class] = count_children
       print("данные обновлены")
       print(new_class, count_children)
elif choose == 2:
    new_class = input("какой класс добавить")
    count_children = input("сколько человек?")
    school[new_class] = count_children
    print("новый класс создан")
    print(school)
elif choose == 3:
    rem_class = input("каой класс удалить?")
    school.pop(rem_class)
    print(school)
elif choose == 4:
    children = sum(school.values())
    print(children)


# Имеется квадрат со сторонами 20см. Пользователь вводит радиусы 2-х кругов.
# Определить могут ли эти круги быть вписанными в указанный квадрат без
# пересечений между собой и со стенками.

a, b = map(int, input().split())
d = (20**2 + 20**2)**(1 / 2)
print((a + b) <= d)

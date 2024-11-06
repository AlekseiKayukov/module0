# Задача 1 (просто) "Арифметика":
# 1st program
from xmlrpc.client import boolean

number = 9;
degree = 0.5;
multiplication = 5;
result = 9**0.5*5;
print("(Задача 1) Результат вычисления: " + str(int(result)));

# Задача 2 (просто) "Логика":
# 2nd program

firstNumber = 9.99;
secondNumber = 9.98;
third = 1000;
fourth = 1000.1;
if (firstNumber > secondNumber and third != fourth):
    print("(Задача 2) Выражение верное");
else:
    print("(Задача 2) Выражение неверное");

# Задача 3 (средне) "Школьная загадка":
# 2nd program

resultFirst = 2*2+2;
resultSecond = 2*(2+2);
resultThird = False;

if (resultFirst == resultSecond):
    resultThird = True;
else:
    resultThird = False;
    print("(Задача 3)" + "\n" + "Результат первого выражения: " + str(resultFirst) + "\n" +
          "Результат второго выражения: " + str(resultSecond) + "\n" +
          "Результат сравнения двух выражения '==': " + str(resultThird));

# Задача 4 (сложно) "Первый после точки":
# 4th program

stroke = "123.456";
print("(Задача 4) Результат первого значения после запятой: " + str((int(float(stroke)*10))%10));
########## 1 TASK ##########

#  Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.


def tribonachchi_gen(val):
    pre_prev, prev, current = 0, 0, 1
    while val > 0:
        val -= 1
        yield current
        pre_prev, prev, current = prev, current, pre_prev + prev + current


tr = tribonachchi_gen(35)
print(list(tr))


########## 2 TASK ##########

# Создайте итерируемый объект, возвращающий генератор чисел из ряда Лейбница, возвращающий новые элементы до тех пор,
# пока сумма полученных элементов не приблизится к ожидаемой сумме ряда с точностью
# в 2 знака после и выведите эти числа.

def leibnits_gen(expected_sum):
    n = 0
    sum = 0
    while round(sum, 2) != round(expected_sum, 2):
        element = ((-1) ** n) / (2 * n + 1)
        yield element
        sum += element
        n += 1


leib = leibnits_gen(0.87)
print(list(leib))

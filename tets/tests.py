import pytest
import functions


# Тест функции, которая определяет n чисел Фибоначчи
class Test_Fibonacci:
    # Функция возвращает число для массива Фибоначчи
    @pytest.fixture
    def numbFibonacci(self):
        return 12

    # Функция возвращает массив чисел фиббоначи от 12 чисел
    @pytest.fixture
    def massFibonacci(self):
        return [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    def test_fibonacci(self, massFibonacci, numbFibonacci):
        assert functions.fibonacci(numbFibonacci) == massFibonacci, \
            "При вычислении чисел фибоначчи возникла ошибка, данные не совпали"

# Тест функции, которая сортирует массив по возрастанию и убыванию методом пузырька
class Test_BubbleSort:
    # Функция возвращает массив несортированных чисел
    @pytest.fixture
    def not_sorted(self):
        return [10, 9, -1, 12, 0, -4, 11]

    # Функция возвращает массив сортированных чисел по возрастанию
    @pytest.fixture
    def sorted_up(self, not_sorted):
        return sorted(not_sorted, reverse=False)

    # Функция возвращает массив сортированных чисел по убыванию
    @pytest.fixture
    def sorted_down(self, not_sorted):
        return sorted(not_sorted, reverse=True)

    def test_bubleSort_up(self, not_sorted, sorted_up):
        assert functions.bubleSort(not_sorted, 1) == sorted_up, \
            "При сортировке по возрастанию возникла ошибка, данные не совпали"

    def test_bubleSort_down(self, not_sorted, sorted_down):
        assert functions.bubleSort(not_sorted, 0) == sorted_down, \
            "При сортировке по убыванию возникла ошибка, данные не совпали"

# Тест функции, которая производит калькуляцию между двумя числами
class Test_Calculate:

    def test_calculate_plus(self):
        assert functions.calculate(4, 12, '+') == 16, \
            "При сложении возникла ошибка, данные не совпали"

    def test_calculate_minus(self):
        assert functions.calculate(4, 12, '-') == -8, \
            "При вычитании возникла ошибка, данные не совпали"

    def test_calculate_multiplication(self):
        assert functions.calculate(4, 12, '*') == 48, \
            "При умножении возникла ошибка, данные не совпали"

    def test_calculate_division(self):
        assert functions.calculate(4, 16, '/') == 0.25, \
            "При делении возникла ошибка, данные не совпали"

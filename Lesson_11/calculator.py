def input_int_number(text: str) -> int:
    try:
        while True:
            return int(input(text))
    except ValueError as e:
        print("Ошибка", e)


class CalculationExitException(Exception):
    pass


def calculate(left: int, right: int, operation: str):
    match operation:
        case "+":
            return left + right
        case "-":
            return left - right
        case "/":
            return left / right
        case "*":
            return left * right
        case "!":
            raise CalculationExitException
        case _:
            raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
        try:
            left = input_int_number("Введите первое число: ")
            right = input_int_number("Введите второе число: ")
            operation = input("Введите операцию: ")
            res = calculate(left, right, operation)
            print(f"{left} {operation} {right} = {res}")
        except (ValueError, ZeroDivisionError) as e:
            print("Ошибка: ", e, end="\n\n")
        except CalculationExitException:
            print("Exit")
            break


if __name__ == "__main__":
    main()

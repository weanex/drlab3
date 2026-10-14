# task7_rpn_calculator.py

from task4_structures import Stack


def rpn_calc(expr):
    stack = Stack()
    tokens = expr.split()

    for token in tokens:
        if token in ("+", "-", "*", "/", "**", "^"):
            if stack.size() < 2:
                raise ValueError(f"Недостаточно операндов для {token}")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                if b == 0:
                    raise ValueError("Деление на ноль")
                stack.push(a / b)
            elif token in ("**", "^"):
                stack.push(a ** b)
        elif token == "neg":
            if stack.is_empty():
                raise ValueError("Недостаточно операндов для neg")
            stack.push(-stack.pop())
        else:
            try:
                stack.push(float(token))
            except ValueError:
                raise ValueError(f"Некорректный токен: {token!r}")

    if stack.size() != 1:
        raise ValueError("Некорректное выражение: в стеке не один результат")
    return stack.pop()


if __name__ == "__main__":
    print(" Задание №7:")

    cases_ok = [
        ("3 4 +", 7),
        ("3 4 + 2 *", 14),
        ("5 1 2 + 4 * + 3 -", 14),
        ("2 3 **", 8),
        ("2 3 ^", 8),
        ("7 2 /", 3.5),
        ("4 neg", -4),
        ("3 4 + 2 * 7 /", 2.0),
    ]

    for expr, expected in cases_ok:
        got = rpn_calc(expr)
        print(f"{expr!r} = {got} (ожидалось {expected})")
        assert abs(got - expected) < 1e-9, (expr, got, expected)

    cases_bad = [
        "3 +",
        "3 4",
        "3 4 + +",
        "abc",
        "1 0 /",
        "",
    ]

    for expr in cases_bad:
        try:
            rpn_calc(expr)
            assert False, f"Должно быть исключение для {expr!r}"
        except ValueError as e:
            print(f"{expr!r} -> ValueError: {e}")
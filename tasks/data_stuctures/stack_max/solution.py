class StackMax:
    """
    Стек с поддержкой получения максимума за O(1).
    """

    def __init__(self):
        # Основной стек значений
        self._values = []

        # Стек текущих максимумов
        self._max_values = []

    def push(self, x: int) -> None:
        self._values.append(x)

        # Новый максимум — либо x, либо предыдущий максимум
        max_value = x if not self._max_values else max(x, self._max_values[-1])
        self._max_values.append(max_value)

    def pop(self) -> str | None:
        if not self._values:
            return "error"

        self._values.pop()
        self._max_values.pop()
        return None

    def get_max(self) -> int | str | None:
        if not self._values:
            return "None"
        return self._max_values[-1]
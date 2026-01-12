class DoubleConnectedNode:
    """
    Узел двусвязного списка.
    Не содержит логики — только данные.
    """

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(head: DoubleConnectedNode) -> DoubleConnectedNode:
    """
    Разворачивает двусвязный список in-place.
    Возвращает новую голову списка.
    """

    current = head
    new_head = None

    while current:
        # Меняем местами ссылки next и prev
        current.prev, current.next = current.next, current.prev

        # Последний обработанный узел станет новой головой
        new_head = current

        # Двигаемся дальше по старому next (теперь это prev)
        current = current.prev

    return new_head
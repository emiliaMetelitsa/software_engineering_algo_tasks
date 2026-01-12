from tasks.data_stuctures.double_connected_node.solution import DoubleConnectedNode, solution


def build_list(values):
    """Вспомогательная функция для сборки списка"""
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0]


def to_list(head):
    """Преобразует список в Python-массив"""
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def test_single_node():
    node = DoubleConnectedNode(1)
    assert solution(node) is node


def test_reverse_list():
    head = build_list([1, 2, 3, 4])
    assert to_list(solution(head)) == [4, 3, 2, 1]


def test_prev_links_integrity():
    head = build_list([1, 2, 3])
    new_head = solution(head)

    prev = None
    cur = new_head
    while cur:
        assert cur.prev is prev
        prev = cur
        cur = cur.next

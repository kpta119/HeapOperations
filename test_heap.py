from nary_heap import NaryHeap


def test_build_heap2():
    heap2 = NaryHeap(2, [3,1,5,6,3,8,9])
    table = heap2.get_table()
    for i, key in enumerate(table[:len(table)//2]):
        for x in range(2):
            if heap2.get_child_of(x, i) < len(table):
                assert key >= table[heap2.get_child_of(x, i)]


def test_build_heap2_more_elements():
    heap2 = NaryHeap(2, [3,1,5,6,3,8,9,2,4,3,2,1,2,1,2,5])
    table = heap2.get_table()
    for i, key in enumerate(table[:len(table)//2]):
        for x in range(2):
            if heap2.get_child_of(x, i) < len(table):
                assert key >= table[heap2.get_child_of(x, i)]


def test_build_heap5():
    heap5 = NaryHeap(5, [3,1,5,6,3,8,9,3,4,2,1,5])
    table = heap5.get_table()
    for i, key in enumerate(table[:len(table)//5]):
        for x in range(5):
            if heap5.get_child_of(x, i) < len(table):
                assert key >= table[heap5.get_child_of(x, i)]


def test_build_heap5_more_elements():
    heap5 = NaryHeap(5, [3,1,5,6,3,8,9,3,4,2,1,5,4,3,2,4,6,7,8,5,6,4,7,3])
    table = heap5.get_table()
    for i, key in enumerate(table[:len(table)//5]):
        for x in range(5):
            if heap5.get_child_of(x, i) < len(table):
                assert key >= table[heap5.get_child_of(x, i)]


def test_build_heap7():
    heap7 = NaryHeap(7, [3,1,5,6,3,8,9,3,1,4,8,2,1])
    table = heap7.get_table()
    for i, key in enumerate(table[:len(table)//7]):
        for x in range(7):
            if heap7.get_child_of(x, i) < len(table):
                assert key >= table[heap7.get_child_of(x, i)]


def test_build_heap7_more_elements():
    heap7 = NaryHeap(7, [3,1,5,6,3,8,9,3,1,4,8,2,1,5,4,2,3,4,2,1,2,5,10,2,4,3])
    table = heap7.get_table()
    for i, key in enumerate(table[:len(table)//7]):
        for x in range(7):
            if heap7.get_child_of(x, i) < len(table):
                assert key >= table[heap7.get_child_of(x, i)]


def test_pop_method_heap2():
    heap2 = NaryHeap(2, [2,4,3,5,3,10,4,9])
    n = len(heap2.get_table())
    assert heap2.get_table()[0] == 10
    heap2.pop()
    assert len(heap2.get_table()) == n - 1
    assert heap2.get_table()[0] == 9


def test_pop_method_heap5():
    heap5 = NaryHeap(5, [2,3,1,2,3,10,9,4])
    n = len(heap5.get_table())
    assert heap5.get_table()[0] == 10
    heap5.pop()
    assert len(heap5.get_table()) == n - 1
    assert heap5.get_table()[0] == 9


def test_pop_method_heap7():
    heap7 = NaryHeap(7, [1,2,3,10,5,3,9,0])
    n = len(heap7.get_table())
    assert heap7.get_table()[0] == 10
    heap7.pop()
    assert len(heap7.get_table()) == n - 1
    assert heap7.get_table()[0] == 9


def test_push_method_heap2():
    heap2 = NaryHeap(2, [2,3,1,4,6,5,9,1])
    n = len(heap2.get_table())
    key = 8
    heap2.push(key)
    assert len(heap2.get_table()) == n + 1
    key_index = heap2.get_table().index(key)
    for x in range(2):
        if heap2.get_child_of(x, key_index) < len(heap2.get_table()):
            assert key >= heap2.get_table()[heap2.get_child_of(x, key_index)]
    if key_index > 0:
        assert key <= heap2.get_table()[heap2.get_parent_of(key_index)]


def test_push_method_heap5():
    heap5 = NaryHeap(2, [3,3,3,3,2,6,5,9,1,4])
    n = len(heap5.get_table())
    key = 8
    heap5.push(key)
    assert len(heap5.get_table()) == n + 1
    key_index = heap5.get_table().index(key)
    for x in range(5):
        if heap5.get_child_of(x, key_index) < len(heap5.get_table()):
            assert key >= heap5.get_table()[heap5.get_child_of(x, key_index)]
    if key_index > 0:
        assert key <= heap5.get_table()[heap5.get_parent_of(key_index)]


def test_push_method_heap7():
    heap7 = NaryHeap(7, [1,4,6,5,9,1,4,3,2,1,6,1,1,1,2])
    n = len(heap7.get_table())
    key = 8
    heap7.push(key)
    assert len(heap7.get_table()) == n + 1
    key_index = heap7.get_table().index(key)
    for x in range(7):
        if heap7.get_child_of(x, key_index) < len(heap7.get_table()):
            assert key >= heap7.get_table()[heap7.get_child_of(x, key_index)]
    if key_index > 0:
        assert key <= heap7.get_table()[heap7.get_parent_of(key_index)]

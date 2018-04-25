import time


def create_set():
    a = {i**2 for i in range(10)}
    print(type(a))
    print(a)
    return a


def add_elem_in_set(Set):
    elem = 100
    start_time = time.time()
    Set.add(elem)
    print(Set)
    print("--- %s seconds ---" % (time.time() - start_time))


def find_elem_in_set(Set):
    elem = 10000
    start_time2 = time.time()
    elem in Set
    print("--- %s seconds ---" % (time.time() - start_time2))


def create_array():
    b = [i**2 for i in range(10)]
    print(type(b))
    print(b)
    return b


def add_elem_in_array(Array):
    elem = 100
    start_time3 = time.time()
    Array.append(elem)
    print(Array)
    print("--- %s seconds ---" % (time.time() - start_time3))


def find_elem_in_array(Array):
    elem = 100
    start_time4 = time.time()
    Array.index(elem)
    print("--- %s seconds ---" % (time.time() - start_time4))


def main():
    s = create_set()
    add_elem_in_set(s)
    find_elem_in_set(s)
    a = create_array()
    add_elem_in_array(a)
    find_elem_in_array(a)


if __name__ == '__main__':
    main()

a = 1
b = [1, 2, 3]

def test_data(b):
    b = b + 1
    return b


def test_list(c):
    c.append(10)
    return c


if __name__ == '__main__':
    data_trans = test_data(a)
    print(a, data_trans, a)
    object_trans = test_list(b)
    print(b, object_trans, b)
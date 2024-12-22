from matrix_with_fraction import Matrix, Vector
from fraction import Fraction


# ==================== Tests for Fraction =====================
def test_fraction_create_from_int():
    a = Fraction(2)
    assert a.get() == (2, 1)


def test_fraction_create_numerator_0():
    a = Fraction(0, 4)
    assert a.get() == (0, 1)


def test_fraction_create_denominator_0():
    a = Fraction(9, 0)
    assert a is None


def test_fraction_bring_to_general_fraction_simplifiable():
    a = Fraction(9, 12)
    a.bring_to_general()
    assert a.get() == (3, 4)


def test_fraction_bring_to_general_negative_denominator():
    a = Fraction(3, -7)
    a.bring_to_general()
    assert a.get() == (-3, 7)


def test_fraction_bring_to_general_fraction_not_simplifiable():
    a = Fraction(11, 13)
    a.bring_to_general()
    assert a.get() == (11, 13)


def test_fraction_bring_to_general_fraction_not_simplifiable_bigger_numerator():
    a = Fraction(27, 13)
    a.bring_to_general()
    assert a.get() == (27, 13)


def test_fraction_bring_to_general_2_fractions():
    a = Fraction(3, 4)
    b = Fraction(1, 2)
    c = Fraction(a, b)
    c.bring_to_general()
    assert c.get() == (3, 2)


def test_fraction_bring_to_general_2_fractions_negative_denominator():
    a = Fraction(3, 4)
    b = Fraction(-1, 2)
    c = Fraction(a, b)
    c.bring_to_general()
    assert c.get() == (-3, 2)


def test_fraction_get_int_part_0():
    a = Fraction(0, 2)
    b = a.get_integer()
    assert b == 0


def test_fraction_get_int_part_1():
    a = Fraction(1, 2)
    b = a.get_integer()
    assert b == 1


def test_fraction_get_int_part_int():
    a = Fraction(16, 4)
    b = a.get_integer()
    assert b == 4


def test_fraction_get_remainder_part_0():
    a = Fraction(0, 3)
    b = a.get_remainder()
    assert b == (1, 1)


def test_fraction_get_remainder_part_1():
    a = Fraction(1, 2)
    b = a.get_remainder()
    assert b == (1, 2)


def test_fraction_get_remainder_part_int():
    a = Fraction(16, 4)
    b = a.get_remainder()
    assert b == (1, 4)


def test_fraction_get_remainder_part_negative():
    a = Fraction(-5, 4)
    b = a.get_remainder()
    assert b == (1, 4)


def test_fraction_add_fraction_to_fraction():
    a = Fraction(3, 4)
    b = Fraction(1, 2)
    c = a.add(b)
    assert c.get() == (10, 8)


def test_fraction_add_fraction_to_int():
    a = Fraction(3, 4)
    b = Fraction(3)
    c = a.add(b)
    assert c.get() == (15, 4)


def test_fraction_add_fraction_to_negative_fraction():
    a = Fraction(3, 4)
    b = Fraction(-1, 2)
    c = a.add(b)
    assert c.get() == (2, 8)


def test_fraction_sub_fraction():
    a = Fraction(19, 23)
    b = Fraction(3, 7)
    c = a.sub(b)
    c.bring_to_general()
    assert c.get() == (64, 161)


def test_negative_fraction_sub_fraction():
    a = Fraction(-19, 23)
    b = Fraction(3, 7)
    c = a.sub(b)
    c.bring_to_general()
    assert c.get() == (-202, 161)


def test_fraction_sub_negative_fraction():
    a = Fraction(19, 23)
    b = Fraction(-3, 7)
    c = a.sub(b)
    c.bring_to_general()
    assert c.get() == (202, 161)


def test_negative_fraction_sub_int():
    a = Fraction(5, 8)
    b = Fraction(3)
    c = a.sub(b)
    c.bring_to_general()
    assert c.get() == (-19, 8)


def test_fraction_mul_fraction():
    a = Fraction(5, 7)
    b = Fraction(3, 2)
    c = a.mul(b)
    assert c.get() == (15, 14)


def test_negative_fraction_mul_fraction():
    a = Fraction(-5, 7)
    b = Fraction(3, 2)
    c = a.mul(b)
    assert c.get() == (-15, 14)


def test_fraction_mul_int():
    a = Fraction(5, 7)
    b = Fraction(3)
    c = a.mul(b)
    assert c.get() == (15, 7)


def test_fraction_mul_0():
    a = Fraction(-5, 7)
    b = Fraction(0, 2)
    c = a.mul(b)
    assert c.get() == (0, 1)


def test_fraction_mul_negative_fraction():
    a = Fraction(-5, 2)
    b = Fraction(-2, 6)
    c = a.mul(b)
    assert c.get() == (10, 12)


def test_fraction_div_fraction():
    a = Fraction(7, 9)
    b = Fraction(5, 2)
    c = a.div(b)
    assert c.get() == (14, 45)


def test_fraction_div_int():
    a = Fraction(5, 2)
    b = Fraction(2)
    c = a.div(b)
    assert c.get() == (5, 4)


def test_fraction_div_0():
    a = Fraction(5, 2)
    b = Fraction(0)
    c = a.div(b)
    assert c is None


def test_fraction_power_1():
    a = Fraction(4, 3)
    b = a.power(1)
    assert b.get() == (4, 3)


def test_fraction_power_0():
    a = Fraction(4, 3)
    b = a.power(0)
    assert b.get() == (1, 1)


def test_fraction_power_int():
    a = Fraction(4, 3)
    b = a.power(3)
    assert b.get() == (64, 27)


# ==================== Tests for Matrix =====================
def test_matrix_add_matrix():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4)],
        [Fraction(3, 4), Fraction(4, 5)]
    ])
    B = Matrix([
        [Fraction(4,3), Fraction(2,1)],
        [Fraction(1,2), Fraction(0, 1)]
    ])
    C = ([
        [(2, 1), (11, 4)],
        [(5, 4), (4, 5)]
    ])
    D = A.add(B)
    assert D.get() == C


def test_matrix_add_matrix_negative():
    A = Matrix([
        [2, 3],
        [3, 4]
    ])
    B = Matrix([
        [4, 2, 3],
        [1, 0, 1]
    ])
    D = A.add(B)
    assert D is None


def test_matrix_sub_matrix():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4)],
        [Fraction(3, 4), Fraction(4, 5)]
    ])
    B = Matrix([
        [Fraction(4, 3), Fraction(2, 1)],
        [Fraction(1, 2), Fraction(0, 1)]
    ])
    C = ([
        [(-2, 3), (-5, 4)],
        [(1, 4), (4, 5)]
    ])
    D = A.sub(B)
    assert D.get() == C


def test_matrix_sub_matrix_negative():
    A = Matrix([
        [2, 3, 4],
        [3, 4, 2]
    ])
    B = Matrix([
        [4, 2],
        [1, 0]
    ])
    D = A.sub(B)
    assert D is None


def test_matrix_prod_matrix():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4), Fraction(5, 6)],
        [Fraction(3, 4), Fraction(4, 5), Fraction(2, 3)]
    ])
    B = Matrix([
        [Fraction(4, 5), Fraction(2, 3)],
        [Fraction(1, 2), Fraction(0, 1)],
        [Fraction(5, 6), Fraction(3, 4)]
    ])

    C = ([
        [(577, 360), (77, 72)],
        [(14, 9), (1, 1)]
    ])
    D = A.prod(B)
    assert D.get() == C


def test_matrix_prod_matrix_negative():
    A = Matrix([
        [2, 3],
        [3, 4],
        [5, -1]
    ])
    B = Matrix([
        [4, 2],
        [1, 0],
        [5, 3]
    ])
    D = A.prod(B)
    assert D is None


def test_matrix_prod_int():
    A = Matrix([
        [-2, 3, 5],
        [3, 4, -2]
    ])
    l = 4
    C = ([
        [(-8, 1), (12, 1), (20, 1)],
        [(12, 1), (16, 1), (-8, 1)]
    ])
    D = A.prod(l)
    assert D.get() == C


def test_matrix_prod_fraction():
    A = Matrix([
        [Fraction(-2, 3), Fraction(3, 4), Fraction(5,6)],
        [Fraction(3, 4), Fraction(4, 5), Fraction(-2, 3)]
    ])
    l = Fraction(1,2)
    C = ([
        [(-1, 3), (3, 8), (5, 12)],
        [(3, 8), (2, 5), (-1, 3)]
    ])
    D = A.prod(l)
    assert D.get() == C


def test_matrix_prod_vector():
    A = Matrix([
        [-2, 3, 5],
        [3, 4, -2]
    ])
    B = Vector([2, 3, 4])
    C = ([(25, 1), (10, 1)])
    D = A.prod(B)
    assert D.get_vector() == C


def test_matrix_transpose():
    A = Matrix([
        [2, 3, 4],
        [3, 4, 5],
        [1, 2, 3],
    ])
    AT = [
        [(2, 1), (3, 1), (1, 1)],
        [(3, 1), (4, 1), (2, 1)],
        [(4, 1), (5, 1), (3, 1)]
    ]
    A_transpose = A.transpose()
    assert A_transpose.get() == AT


def test_matrix_transposed_transpose():
    A = Matrix([
        [2, 3, 4],
        [3, 4, 5],
        [1, 2, 3],
    ])
    A_transpose = A.transpose()
    A_transposed_transpose = A_transpose.transpose()
    assert A_transposed_transpose.get() == A.get()
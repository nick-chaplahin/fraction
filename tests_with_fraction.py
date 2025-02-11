"""
Copyright by Nick Chaplahin 2024. All rights reserved, but you can use it, if do not forget to mention me as an author.
Part of Entire Math project.
"""
from matrix_with_fraction import *
from fraction import Fraction
import pytest


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


def test_fraction_add_fraction_to_short_fraction():
    a = Fraction(3, 4)
    b = Fraction(3)
    c = a.add(b)
    assert c.get() == (15, 4)


def test_fraction_add_fraction_to_int():
    a = Fraction(3, 4)
    b = 3
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


def test_negative_fraction_sub_short_fraction():
    a = Fraction(5, 8)
    b = Fraction(3)
    c = a.sub(b)
    c.bring_to_general()
    assert c.get() == (-19, 8)


def test_negative_fraction_sub_int():
    a = Fraction(5, 8)
    b = 3
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


def test_fraction_mul_short_fraction():
    a = Fraction(5, 7)
    b = Fraction(3)
    c = a.mul(b)
    assert c.get() == (15, 7)


def test_fraction_mul_int():
    a = Fraction(5, 7)
    b = 3
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


def test_fraction_div_short_fraction():
    a = Fraction(5, 2)
    b = Fraction(2)
    c = a.div(b)
    assert c.get() == (5, 4)


def test_fraction_div_int():
    a = Fraction(5, 2)
    b = 2
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
        [Fraction(4, 3), Fraction(2, 1)],
        [Fraction(1, 2), Fraction(0, 1)]
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
    multiplier = 4
    C = ([
        [(-8, 1), (12, 1), (20, 1)],
        [(12, 1), (16, 1), (-8, 1)]
    ])
    D = A.prod(multiplier)
    assert D.get() == C


def test_matrix_prod_fraction():
    A = Matrix([
        [Fraction(-2, 3), Fraction(3, 4), Fraction(5, 6)],
        [Fraction(3, 4), Fraction(4, 5), Fraction(-2, 3)]
    ])
    multiplier = Fraction(1, 2)
    C = ([
        [(-1, 3), (3, 8), (5, 12)],
        [(3, 8), (2, 5), (-1, 3)]
    ])
    D = A.prod(multiplier)
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


def test_matrix_E_transpose():
    A = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])
    A_transpose = A.transpose()
    assert A_transpose.get() == A.get()


def test_matrix_euclidean_norm_base():
    A = Matrix([
        [2, 3, 4],
        [1, 4, 5],
        [3, 2, 3],
        [2, 1, 2]
    ])
    a_norm = A.euclidean_norm_base()
    assert a_norm == (102, 1)


def test_matrix_trace_positive():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)],
        [Fraction(3, 4), Fraction(4, 5), Fraction(5, 6)],
        [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)],
    ])
    tr_A = A.trace()
    assert tr_A.get() == (133, 60)


def test_matrix_trace_negative():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)],
        [Fraction(3, 4), Fraction(4, 5), Fraction(5, 6)],
    ])
    tr_A = A.trace()
    assert tr_A is None


def test_matrix_trace_nontracable():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)],
        [Fraction(3, 4), Fraction(-4, 5), Fraction(5, 6)],
        [Fraction(1, 2), Fraction(2, 3), Fraction(2, 15)],
    ])
    tr_A = A.trace()
    assert tr_A.get() == (0, 1)


def test_matrix_frobenius_norm_with_trace():
    A = Matrix([
        [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)],
        [Fraction(3, 4), Fraction(-4, 5), Fraction(5, 6)],
        [Fraction(1, 2), Fraction(2, 3), Fraction(2, 15)],
    ])
    A_euclid_norm_base = A.euclidean_norm_base()
    step1 = A.transpose()
    step2 = A.prod(step1)
    A_frobenius_norm_base = step2.trace()
    assert A_euclid_norm_base == A_frobenius_norm_base.get()


def test_matrix_ortogonal_i():
    A = Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    assert A.is_ortogonal()


def test_matrix_ortogonal_E():
    A = Matrix([
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ])

    assert A.is_ortogonal()


def test_matrix_ortogonal_val():
    A = Matrix([
        [Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)],
        [Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2)],
    ])

    assert A.is_ortogonal()


def test_matrix_ortogonal_val_negative():
    A = Matrix([
        [Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)],
        [Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2)],
    ])

    assert not A.is_ortogonal()


def test_matrix_ortogonal_negative():
    A = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]
    ])

    assert not A.is_ortogonal()


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_has_zeros():
    A = Matrix([
        [0, 2, 1],
        [1, 0, 3],
        [4, 5, 6]
    ])

    assert A.determinant().get() == (17, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_no_zeros():
    A = Matrix([
        [1, 2, 3],
        [1, -3, 2],
        [1, 1, 1]
    ])
    assert A.determinant().get() == (9, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_negative():
    A = Matrix([
        [1, 2, 3, 4],
        [1, -3, 2, 3],
        [1, 1, 1, 2]
    ])
    assert A.determinant() is None


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_transponded():
    A = Matrix([
        [1, 2, 3],
        [1, -3, 2],
        [1, 1, 1]
    ])
    B = A.transpose()
    assert A.determinant().get() == B.determinant().get()


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_4x4():
    matrix = [
        [1, 2, 3, -4],
        [1, -3, 2, 3],
        [1, 1, 1, 2],
        [5, 2, -1, 2]
    ]
    A = Matrix(matrix)
    assert A.determinant().get() == (-234, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_rows_swap():
    matrix = [
        [1, 2, 3, -4],
        [1, -3, 2, 3],
        [1, 1, 1, 2],
        [5, 2, -1, 2]
    ]
    A = Matrix(matrix)
    matrix_swap_rows = [matrix[1], matrix[3], matrix[0], matrix[2]]
    B = Matrix(matrix_swap_rows)
    assert A.determinant().get_numerator() == -B.determinant().get_numerator()


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_zero_row():
    A = Matrix([
        [1, 2, 3, -4],
        [0, 0, 0, 0],
        [1, 1, 1, 2],
        [5, 2, -1, 2]
    ])
    assert A.determinant().get() == (0, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_zero_column():
    A = Matrix([
        [1, 2, 0, -4],
        [1, -3, 0, 3],
        [1, 1, 0, 2],
        [5, 2, 0, 2]
    ])
    assert A.determinant().get() == (0, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_determinant_I():
    A = Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    assert A.determinant().get() == (1, 1)


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_minors():
    matrix = [
        [Fraction(1), Fraction(2), Fraction(3), Fraction(-4)],
        [Fraction(1), Fraction(-3), Fraction(2), Fraction(3)],
        [Fraction(1), Fraction(1), Fraction(1), Fraction(2)],
        [Fraction(5), Fraction(2), Fraction(-1), Fraction(2)]
    ]
    A = Matrix(matrix)
    minor_1_1 = [
        [(1, 1), (3, 1), (-4, 1)],
        [(1, 1), (1, 1), (2, 1)],
        [(5, 1), (-1, 1), (2, 1)]
    ]
    minor_0_2 = [
        [(1, 1), (-3, 1), (3, 1)],
        [(1, 1), (1, 1), (2, 1)],
        [(5, 1), (2, 1), (2, 1)]
    ]
    minor_3_3 = [
        [(1, 1), (2, 1), (3, 1)],
        [(1, 1), (-3, 1), (2, 1)],
        [(1, 1), (1, 1), (1, 1)],
    ]
    minor_0_0 = [
        [(-3, 1), (2, 1), (3, 1)],
        [(1, 1), (1, 1), (2, 1)],
        [(2, 1), (-1, 1), (2, 1)]
    ]
    assert A.minor(1, 1).get_matrix_frac_values() == minor_1_1
    assert A.minor(0, 2).get_matrix_frac_values() == minor_0_2
    assert A.minor(3, 3).get_matrix_frac_values() == minor_3_3
    assert A.minor(0, 0).get_matrix_frac_values() == minor_0_0


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_inverse_2x2():
    A = Matrix([
        [1, 2],
        [1, 4],
    ])
    B = [
        [(4, 2), (-2, 2)],
        [(-1, 2), (1, 2)]
    ]
    C = A.inverse()
    assert C.get_matrix_frac_values() == B


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_inverse_3x3():
    A = Matrix([
        [0, 2, 1],
        [1, 0, 3],
        [4, 5, 6]
    ])
    B = [
        [(-15, 17), (-7, 17), (6, 17)],
        [(6, 17), (-4, 17), (1, 17)],
        [(5, 17), (8, 17), (-2, 17)],
    ]
    C = A.inverse()
    assert C.get_matrix_frac_values() == B


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_inverse_negative_non_square_matrix():
    A = Matrix([
        [0, 2, 1, 4],
        [1, 0, 3, 5],
        [4, 5, 6, 1]
    ])

    C = A.inverse()
    assert C is None


@pytest.mark.skipif(matrix_version_num < 1.0, reason="Functionality is not supported in this version")
def test_matrix_inverse_negative_determinant_zero():
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    C = A.inverse()
    assert C is None

import random
from matrix_with_fraction import Matrix, Vector
from fraction import Fraction
import numpy as np


# ==================== ADDITIONAL SERVICE FUNCTIONS =====================
def frac_description(frac, structure):
    """
       Function to automate display
    """
    print("Structure is: {}".format(structure))
    print("ORIGINAL Fraction before bringing to general is: {}".format(frac.describe()))
    print("ORIGINAL Fraction before bringing to general get() is: {}".format(frac.get()))
    frac.bring_to_general()
    print("ORIGINAL Fraction after bringing to general is {}".format(frac.describe()))
    print("ORIGINAL Fraction after bringing to general get() is: {}".format(frac.get()))
    print("Where:\n Numerator: {}\n Denominator: {}\n Absolute Value:{}".format(frac.get_numerator(),
                                                                                frac.get_denominator(),
                                                                                frac.get_absolute_result()))


def matrix_description(matrix):
    line = ""
    for idx in range(matrix.get_rows()):
        line = line + "["
        for idy in range(matrix.get_cols()):
            numerator,denominator = matrix.matrix[idx][idy].get()
            line = line + "{}/{} ".format(numerator, denominator)
        line = line + "]\n"
    return"[{}]".format(line)


def Matrix_Fractions_Demo_integers():
    print("\n\n==================== OPERATION WITH MATRIX OF FRACTIONS AND COMPARE RESULT WITH NUMPY")
    matrix = [
        [3, 6, 9],
        [4, 8, 12],
        [5, 7, 11]
    ]
    A = Matrix(matrix)
    A_np = np.matrix(matrix)
    print("Fraction Matrix Values: \n {}".format(matrix_description(A)))
    print("Numpy Matrix Values: \n {}".format(A_np))
    multiplier_1 = Fraction(1, 7)
    print("Multiplier 1: {}/{}".format(multiplier_1.get_numerator(), multiplier_1.get_denominator()))
    multiplier_2 = Fraction(1, 13)
    print("Multiplier 2: {}/{}".format(multiplier_2.get_numerator(), multiplier_2.get_denominator()))
    multiplier_3 = Fraction(7, 1)
    print("Multiplier 3: {}/{}".format(multiplier_3.get_numerator(), multiplier_3.get_denominator()))
    multiplier_4 = Fraction(13, 1)
    print("Multiplier 4: {}/{}".format(multiplier_4.get_numerator(), multiplier_4.get_denominator()))
    print("========== STEP 1. Multiply matrix by 1/7")
    B = A.prod(multiplier_1)
    B_np = (1/7) * A_np
    print("Fraction Matrix * 1/7: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 1/7: \n {}".format(B_np))
    print("========== STEP 2. Multiply matrix by 1/13")
    B = B.prod(multiplier_2)
    B_np = (1/13) * B_np
    print("Fraction Matrix * 1/13: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 1/13: \n {}".format(B_np))
    print("========== STEP 3. Multiply matrix by Multiplier 3")
    B = B.prod(multiplier_3)
    B_np = 7.0 * B_np
    print("Fraction Matrix * 7: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 7: \n {}".format(B_np))
    print("========== STEP 4. Multiply matrix by Multiplier 4")
    B = B.prod(multiplier_4)
    B_np = 13.0 * B_np
    print("Fraction Matrix * 13: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 13: \n {}".format(B_np))
    print("Resulting Fraction Matrix Values: \n {}".format(np.matrix(B.get_matrix_absolute_values())))


def Matrix_Fractions_Demo_fractions():
    print("\n\n==================== OPERATION WITH MATRIX OF FRACTIONS AND COMPARE RESULT WITH NUMPY")
    matrix = [
        [Fraction(1, 3), Fraction(1, 6), Fraction(1, 9)],
        [Fraction(1, 4), Fraction(1, 8), Fraction(1, 12)],
        [Fraction(1, 5), Fraction(1, 7), Fraction(1, 11)]
    ]
    matrix_np = [
        [1/3, 1/6, 1/9],
        [1/4, 1/8, 1/12],
        [1/5, 1/7, 1/11]
    ]
    A = Matrix(matrix)
    A_np = np.matrix(matrix_np)
    print("Fraction Matrix Values: \n {}".format(matrix_description(A)))
    print("Numpy Matrix Values: \n {}".format(A_np))
    multiplier_1 = Fraction(1, 7)
    print("Multiplier 1: {}/{}".format(multiplier_1.get_numerator(), multiplier_1.get_denominator()))
    multiplier_2 = Fraction(1, 13)
    print("Multiplier 2: {}/{}".format(multiplier_2.get_numerator(), multiplier_2.get_denominator()))
    multiplier_3 = Fraction(7, 1)
    print("Multiplier 3: {}/{}".format(multiplier_3.get_numerator(), multiplier_3.get_denominator()))
    multiplier_4 = Fraction(13, 1)
    print("Multiplier 4: {}/{}".format(multiplier_4.get_numerator(), multiplier_4.get_denominator()))
    print("========== STEP 1. Multiply matrix by 1/7")
    B = A.prod(multiplier_1)
    B_np = (1/7) * A_np
    print("Fraction Matrix * 1/7: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 1/7: \n {}".format(B_np))
    print("========== STEP 2. Multiply matrix by 1/13")
    B = B.prod(multiplier_2)
    B_np = (1/13) * B_np
    print("Fraction Matrix * 1/13: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 1/13: \n {}".format(B_np))
    print("========== STEP 3. Multiply matrix by Multiplier 3")
    B = B.prod(multiplier_3)
    B_np = 7.0 * B_np
    print("Fraction Matrix * 7: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 7: \n {}".format(B_np))
    print("========== STEP 4. Multiply matrix by Multiplier 4")
    B = B.prod(multiplier_4)
    B_np = 13.0 * B_np
    print("Fraction Matrix * 13: \n {}".format(matrix_description(B)))
    print("Numpy    Matrix * 13: \n {}".format(B_np))
    print("Resulting Fraction Matrix Values: \n {}".format(np.matrix(B.get_matrix_absolute_values())))


def Fraction_Demo():
    print("\n========== EXAMPLE 1 =====")
    frac1 = Fraction(Fraction(-3, 2), Fraction(7, 5))
    frac_description(frac1, "Fraction(Fraction(-3, 2), Fraction(7, 5))")

    print("\n========== EXAMPLE 2 =====")
    frac2 = Fraction(3, Fraction(10, 5))
    frac_description(frac2, "Fraction(3, Fraction(10, 5))")

    print("\n========== EXAMPLE 3 =====")
    frac3 = frac1.add(frac2)
    frac_description(frac3, "frac1.add(frac2)")

    print("\n========== EXAMPLE 4 =====")
    print("===== ALL OPERATIONS =====")
    fracA = Fraction(3, 4)
    frac_description(fracA, "Fraction(3, 4)")
    fracB = Fraction(2, 3)
    frac_description(fracB, "Fraction(2, 3)")

    print("\n\n========== RESULTS =====")
    print("\n===== ADD ==========")
    frac = fracA.add(fracB)
    frac_description(frac, "fracA.add(fracB)")

    print("\n===== SUB ==========")
    frac = fracA.sub(fracB)
    frac_description(frac, "fracA.sub(fracB)")

    print("\n======MUL ==========")
    frac = fracA.mul(fracB)
    frac_description(frac, "fracA.mul(fracB)")

    print("\n===== DIV ==========")
    frac = fracA.div(fracB)
    frac_description(frac, "fracA.div(fracB)")

    print("\n===== POWER 3 ==========")
    frac = fracA.power(3)
    frac_description(frac, "fracA.power(3)")

    print("\n===== POWER -1 ==========")
    frac = fracB.power(-2)
    frac_description(frac, "fracB.power(-2)")

    print("\n ===== 1/7 * 11/13 * 7 * 13 ==========")
    frac_A = Fraction(1, 7)
    num_a = 1/7
    print(num_a)
    frac_B = Fraction(11, 13)
    num_b = 11/13
    print(num_b)
    frac_C = frac_A.mul(frac_B)
    num_c = num_a * num_b
    print(num_c)
    frac_C = frac_C.mul(7).mul(13)
    num_c = num_c * 7 * 13
    frac_description(frac_C, "1/7 * 11/13 * 7 * 13")
    print(" Result after consecutive Python math execution of operations: {}".format(num_c))

    print("\n ===== 7/13 * 1/7 * 11/13 * 7 * 13 ==========")
    frac_base = Fraction(7, 13)
    num_base = 7/13
    frac_A = Fraction(1, 7)
    num_a = 1/7
    print(num_a)
    frac_B = Fraction(11, 13)
    num_b = 11/13
    print(num_b)
    frac_C = frac_base.mul(frac_A).mul(frac_B)
    num_c = num_base * num_a * num_b
    print(num_c)
    frac_C = frac_C.mul(7).mul(13)
    num_c = num_c * 7 * 13
    frac_description(frac_C, "7/13 * 1/7 * 11/13 * 7 * 13")
    print(" Result after consecutive Python math execution of operations: {}".format(num_c))

Fraction_Demo()

Matrix_Fractions_Demo_integers()
Matrix_Fractions_Demo_fractions()
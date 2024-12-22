import random
from matrix_with_fraction import Matrix, Vector
from fraction import Fraction

# ==================== ADDITIONAL SERVICE FUNCTIONS =====================
def generate_matrix(rows=random.randint(2,10), cols=random.randint(2,10), max_data=20):
    matrix = []
    for idx in range(rows):
        line = []
        for idy in range(cols):
            line.append(Fraction(random.randint(1,max_data)))
        matrix.append(line)
    return matrix.copy()

def generate_scalar(rows=random.randint(2,10), max_data=20):
    matrix = []
    for idx in range(rows):
        matrix.append(Fraction(random.randint(1,max_data)))
    return matrix.copy()

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


def Matrix_Demo():
   A = Matrix(generate_matrix(3,5))
   B = Matrix(generate_matrix(5,2))
   B2 = Matrix(generate_matrix(3,5))
   C = A.transpose()
   D = A.prod(B)
   E = A.hadamard_prod(B2)
   A.describe()
   C.describe()
   B.describe()
   D.describe()
   E.describe()

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

Matrix_Demo()
Fraction_Demo()
"""
Copyright by Nick Chaplahin 2024. All rights reserved, but you can use it, if do not forget to mention me as an author.
Part of Entire Math project.
"""
from fraction import Fraction

matrix_version_num = 1.0

class Vector:
    def __init__(self, vector):
        """
        :param matrix:
        """
        if not isinstance(vector, list):
            print("ERROR: Parameters is not vector")
        if isinstance(vector[0], list):
            print("ERROR: Parameters is wider than vector")
        for idx in range(len(vector)):
            if not isinstance(vector[idx], Fraction):
                vector[idx] = Fraction(vector[idx])
        self.vector = vector
        self.rows = len(vector)

    def get_rows(self):
        return self.rows

    def get(self):
        return self.vector

    def get_vector(self):
        new_vector = []
        for idx in range(self.rows):
            new_vector.append(self.vector[idx].get())
        return new_vector

    def prod(self, second):
        if not isinstance(second, Vector) and not isinstance(second, int) and not isinstance(second, Fraction):
            print("ERROR: multiplier is not Vector and not integer or Fraction")
            return None
        if isinstance(second, int):
            second = Fraction(second)
        if isinstance(second, Vector):
            if self.rows != second.get_rows():
                print("ERROR: vectors have different lengths, not multipliable")
                return None
            new_vector = []
            for idx in range(self.rows):
                tmp = Fraction(0)
                for idy in range(second.get_rows()):
                    tmp = tmp.add(self.vector[idx].mul(second.vector[idy]))
                tmp.bring_to_general()
                new_vector.append(tmp)
            return Vector(new_vector)
        if isinstance(second, Fraction):
            new_vector = []
            for idx in range(self.rows):
                tmp = self.vector[idx].mul(second)
                tmp.bring_to_general()
                new_vector.append(tmp)
            return Vector(new_vector)

    def get_vector_absolute_values(self):
        new_vector = []
        for idx in range(self.rows):
            new_vector.append(self.vector[idx].get_absolute_result())
        return new_vector

class Matrix:
    def __init__(self, matrix):
        """
        :param matrix:
        """
        if not isinstance(matrix, list):
            print("ERROR: Parameters is not an array")
        if not isinstance(matrix[0], list):
            print("ERROR: Parameters is not a matrix")
        new_matrix = []
        for idx in range(len(matrix)):
            line = []
            for idy in range(len(matrix[0])):
                if not isinstance(matrix[idx][idy], Fraction):
                    line.append(Fraction(matrix[idx][idy]))
                else:
                    line.append(matrix[idx][idy])
            new_matrix.append(line)
        self.matrix = new_matrix
        self.rows = len(new_matrix)
        self.cols = len(new_matrix[0])

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_dimension(self):
        return self.rows, self.cols

    def add(self, second):
        if not isinstance(second, Matrix) and \
                not isinstance(second, int) and \
                not isinstance(second, Fraction):
            print("ERROR: not a matrix or integer or Fraction")
        if isinstance(second, int):
            second = Fraction(second)
        if isinstance(second, Matrix):
            if self.get_dimension() != second.get_dimension():
                print("ERROR: Addition is impossible cause matrices has different dimensions")
                return None
            new_matrix = []
            for idx in range(self.rows):
                line = []
                for idy in range(self.cols):
                    tmp = self.matrix[idx][idy].add(second.matrix[idx][idy])
                    tmp.bring_to_general()
                    line.append(tmp)
                new_matrix.append(line)
            return Matrix(new_matrix)

    def sub(self, second):
        if not isinstance(second, Matrix) and \
                not isinstance(second, int) and \
                not isinstance(second, Fraction):
            print("ERROR: not a matrix or integer or Fraction")
        if isinstance(second, int):
            second = Fraction(second)
        if isinstance(second, Matrix):
            if self.get_dimension() != second.get_dimension():
                print("ERROR: Subtraction is impossible cause matrices has different dimensions")
                return None
            new_matrix = []
            for idx in range(self.rows):
                line = []
                for idy in range(self.cols):
                    tmp = self.matrix[idx][idy].sub(second.matrix[idx][idy])
                    tmp.bring_to_general()
                    line.append(tmp)
                new_matrix.append(line)
            return Matrix(new_matrix)

    def prod(self, second):
        if not isinstance(second, Matrix) and \
                not isinstance(second, Vector) and \
                not isinstance(second, int) and \
                not isinstance(second, Fraction):
            print("ERROR: not a Matrix, vector, int or Fraction")
            return None
        if isinstance(second, int):
            second = Fraction(second)
        if isinstance(second, Matrix):
            if self.cols != second.get_rows():
                print("ERROR: self Height doesn't match second Width, not multipliable")
                return None
            new_matrix = []
            for m in range(self.rows):
                line = []
                for p in range(second.get_cols()):
                    tmp = Fraction(0)
                    for n in range(self.cols):
                        tmp = tmp.add(self.matrix[m][n].mul(second.matrix[n][p]))
                        tmp.bring_to_general()
                    line.append(tmp)
                new_matrix.append(line)
            return Matrix(new_matrix)
        if isinstance(second, Fraction):
            new_matrix = self.get_matrix()
            for m in range(self.rows):
                for p in range(self.cols):
                    second.bring_to_general()
                    new_matrix[m][p] = new_matrix[m][p].mul(second)
                    new_matrix[m][p].bring_to_general()
            return Matrix(new_matrix)
        if isinstance(second, Vector):
            if self.cols != second.get_rows():
                print("ERROR: Number of cols in Matrix doesn't equal to Vector's length, not multipliable")
                return None
            new_vector = []
            for idx in range(self.rows):
                tmp = Fraction(0)
                for idy in range(self.cols):
                    tmp = tmp.add(self.matrix[idx][idy].mul(second.vector[idy]))
                tmp.bring_to_general()
                new_vector.append(tmp)
            return Vector(new_vector)

    def hadamard_prod(self, second):
        if not isinstance(second, Matrix):
            print("ERROR: not a matrix")
            return None
        if self.get_dimention() != second.get_dimention():
            print("ERROR: HADAMARD product impossible cause matrices has different dimensions")
            return None
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].mul(second.matrix[idx][idy]))
            new_matrix.append(line)
        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = []
        for idx in range(self.cols):
            new_line = []
            for idy in range(self.rows):
                new_line.append(self.matrix[idy][idx])
            new_matrix.append(new_line)
        return Matrix(new_matrix)

    def trace(self):
        if not self.is_square():
            print("ERROR: Matrix is not square, trace of main diagonal is not available")
            return None
        trace = Fraction(0)
        for idx in range(self.rows):
            trace = trace.add(self.matrix[idx][idx])
        trace.bring_to_general()
        return trace

    def euclidean_norm_base(self):
        sum = Fraction(0)
        for idx in range(self.rows):
            for idy in range(self.cols):
                sum = sum.add(self.matrix[idx][idy].mul(self.matrix[idx][idy]))
        sum.bring_to_general()
        return sum.get()


    def minor(self, row, col):
        sub_matrix = [row[:col] + row[col + 1:] for row in self.matrix[:row]+self.matrix[row+1:]]
        return Matrix(sub_matrix)

    def determinant(self):
        if not self.is_square():
            print("ERROR: Matrix is not square, determinant not calculable")
            return None
        if self.rows < 3:
            if self.rows == 0:
                return None
            if self.rows == 1:
                return self.matrix[0][0]
            if self.rows == 2:
                return self.matrix[0][0].mul(self.matrix[1][1]).sub(self.matrix[1][0].mul(self.matrix[0][1]))
        if self.rows == 3:
            return self.matrix[0][0].mul(self.matrix[1][1]).mul(self.matrix[2][2]).add(
                self.matrix[1][0].mul(self.matrix[2][1]).mul(self.matrix[0][2])).add(
                self.matrix[2][0].mul(self.matrix[0][1]).mul(self.matrix[1][2])).sub(
                self.matrix[2][0].mul(self.matrix[1][1]).mul(self.matrix[0][2])).sub(
                self.matrix[1][0].mul(self.matrix[0][1]).mul(self.matrix[2][2])).sub(
                self.matrix[0][0].mul(self.matrix[2][1]).mul(self.matrix[1][2]))
        else:
            determinant = Fraction(0)
            for idx in range(self.cols):
                sub_matrix = self.minor(0, idx)
                determinant = determinant.add(self.matrix[0][idx].mul(sub_matrix.determinant().mul((-1) ** idx)))
            return determinant

    def inverse(self):
        if not self.is_square():
            print("ERROR: Matrix is not square, determinant not calculable")
            return None
        matrix_determinant = self.determinant()
        if matrix_determinant is None:
            print("ERROR: Determinant is not calculated.")
            return None
        if matrix_determinant.get() == (0, 1):
            print("WARNING: Determinant is 0, matrix is not invertable.")
            return None
        determinant_inverted = Fraction(1).div(matrix_determinant)
        determinant_inverted.bring_to_general()
        transposed_matrix = self.transpose()
        matrix_algebraic_additions = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                minor_determinant = transposed_matrix.minor(idx,idy).determinant()
                sign = Fraction(-1).power(idx+idy)
                line.append(sign.mul(minor_determinant).mul(determinant_inverted))
            matrix_algebraic_additions.append(line)
        return Matrix(matrix_algebraic_additions)


    def get(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].get())
            new_matrix.append(line)
        return new_matrix

    def is_square(self):
        if self.rows != self.cols:
            return False
        return True

    def is_ortogonal(self):
        if not self.is_square():
            return False
        e_matrix = [[(0,1) for idy in range(self.cols)] for idx in range(self.rows)]
        for idx in range(self.rows):
            e_matrix[idx][idx] = (1,1)
        transpose = self.transpose()
        prod_result = self.prod(transpose)
        if prod_result.get_matrix_frac_values() == e_matrix:
            return True
        else:
            return False

    def get_matrix(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy])
            new_matrix.append(line)
        return new_matrix

    def get_matrix_frac_values(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].get())
            new_matrix.append(line)
        return new_matrix

    def get_matrix_absolute_values(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].get_absolute_result())
            new_matrix.append(line)
        return new_matrix

    def describe(self):
        print("\nMatrix height {} width {}:".format(self.rows, self.cols))
        for idx in range(self.rows):
            line = ""
            for idy in range(self.cols):
                line = line + " {}/{}".format(str(self.matrix[idx][idy].get_numerator()),
                                              str(self.matrix[idx][idy].get_denominator()))
            print(" {}".format(line))



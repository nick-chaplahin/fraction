from fraction import Fraction

class Scalar:
    def __init__(self, scalar):
        """

        :param matrix:
        """
        if not isinstance(scalar, list):
            print("ERROR: Parameters is not scalar")
        if isinstance(scalar[0], list):
            print("ERROR: Parameters is wider than scalar")
        for idx in range(len(scalar)):
            if not isinstance(scalar[idx], Fraction):
                scalar[idx] = Fraction(scalar[idx])
        self.scalar = scalar
        self.rows = len(scalar)

    def get_rows(self):
        return self.rows

    def prod(self, second):
        if not isinstance(second, Scalar) and not isinstance(second, int) and not isinstance(second, Fraction):
            print("ERROR: multiplier is not Scalar and not integer or Fractin")
            return None
        if isinstance(second, Scalar):
            new_scalar = []
            for idx in range(self.get_rows()):
                tmp = Fraction(0)
                for idy in range(second.get_rows()):
                    tmp = tmp.add(self.scalar[idx].mul(second.scalar[idy]))
                new_scalar.append(tmp)
            return Scalar(new_scalar)
class Matrix:

    def __init__(self, matrix):
        """

        :param matrix:
        """
        if not isinstance(matrix, list):
            print("ERROR: Parameters is not an array")
        if not isinstance(matrix[0], list):
            print("ERROR: Parameters is not a matrix")
        for idx in range(len(matrix)):
            for idy in range(len(matrix[0])):
                if not isinstance(matrix[idx][idy], Fraction):
                    matrix[idx][idy] = Fraction(matrix[idx][idy])
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_dimention(self):
        return self.rows, self.cols

    def add(self, second):
        if not isinstance(second, Matrix) and \
                not isinstance(second, int) and \
                not isinstance(second, Fraction):
            print("ERROR: not a matrix or integer or Fraction")
        if isinstance(second, int):
            second = Fraction(second)
        if isinstance(second, Matrix):
            if self.get_dimention() != second.get_dimention():
                print("ERROR: Addition is impossible cause matrices has different dimensions")
                return None
            new_matrix = []
            for idx in range(self.get_rows()):
                line = []
                for idy in range(self.get_cols()):
                    line.append(self.matrix[idx][idy].add(second.matrix[idx][idy]))
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
            if self.get_dimention() != second.get_dimention():
                print("ERROR: Subtraction is impossible cause matrices has different dimensions")
                return None
            new_matrix = []
            for idx in range(self.get_rows()):
                line = []
                for idy in range(self.get_cols()):
                    line.append(self.matrix[idx][idy].sub(second.matrix[idx][idy]))
                new_matrix.append(line)
            return Matrix(new_matrix)

    def prod(self, second):
        if not isinstance(second, Matrix) and \
                not isinstance(second, Scalar) and \
                not isinstance(second, int) and \
                not isinstance(second, Fraction):
            print("ERROR: not a Matrix, scalar, int or Fraction")
            return None
        if isinstance(second, Matrix):
            if self.get_cols() != second.get_rows():
                print("ERROR: self Height doesn't match second Width, not multipliable")
                return None
            new_matrix = []
            for m in range(self.get_rows()):
                line = []
                for p in range(second.get_cols()):
                    tmp = Fraction(0)
                    for n in range(self.get_cols()):
                        tmp = tmp.add(self.matrix[m][n].mul(second.matrix[n][p]))
                    line.append(tmp)
                new_matrix.append(line)
            return Matrix(new_matrix)
        if isinstance(second, int):
            new_matrix = self.get_matrix()
            for m in range(self.get_rows()):
                for p in range(self.get_cols()):
                    new_matrix[m][p] = new_matrix[m][p].mul(second)
            return Matrix(new_matrix)

    def hadamard_prod(self, second):
        if not isinstance(second, Matrix):
            print("ERROR: not a matrix")
            return None
        if self.get_dimention() != second.get_dimention():
            print("ERROR: HADAMARD product impossible cause matrices has different dimensions")
            return None
        new_matrix = []
        for idx in range(self.get_rows()):
            line = []
            for idy in range(self.get_cols()):
                line.append(self.matrix[idx][idy].mul(second.matrix[idx][idy]))
            new_matrix.append(line)
        return Matrix(new_matrix)

    def div(self, second):
        if not isinstance(second, Matrix) and not isinstance(second, Scalar):
            print("ERROR: not a matrix or scalar")

    def transpose(self):
        new_matrix = []
        for idx in range(self.cols):
            new_line = []
            for idy in range(self.rows):
                new_line.append(self.matrix[idy][idx])
            new_matrix.append(new_line)
        return Matrix(new_matrix)

    def get(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].get())
            new_matrix.append(line)
        return new_matrix

    def get_matrix(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy])
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




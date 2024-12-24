from fraction import Fraction

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
            if self.get_dimention() != second.get_dimention():
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
        if self.rows != self.cols:
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

    def get(self):
        new_matrix = []
        for idx in range(self.rows):
            line = []
            for idy in range(self.cols):
                line.append(self.matrix[idx][idy].get())
            new_matrix.append(line)
        return new_matrix

    def is_ortogonal(self):
        if self.rows != self.cols:
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




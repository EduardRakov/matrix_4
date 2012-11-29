class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, matrix):
        if self.get_rows() == matrix.get_rows() and self.get_cols() == matrix.get_cols():
            result = [0] * self.get_rows()

            for row in range(self.get_rows()):
                result[row] = [0] * self.get_cols()
                for col in range(self.get_cols()):
                    result[row][col] = self.matrix[row][col] + matrix[row][col]

            return result
        else:
            raise Exception('Matrices are not proportional')

    def get_cols(self):
        return len(self.matrix[0])

    def get_rows(self):
        return len(self.matrix)


class Foo():
    def __init__(self, size):
        self.size = size
        self.weight = [0] * self.size
        for i in range(size):
            self.weight[i] = [0] * self.size


    def bar(self, vector):
        matrix_2 = list(vector)
        matrix= list()
        matrix.append(matrix_2)
        matrix_1 = map(lambda *vector: list(vector), *matrix)
        identity = [0] * len(matrix_2)
        matrix_3 = [0] * len(matrix_2)
        matrix_4 = [0] * len(matrix_2)
        for i in range(len(matrix_2)):
            identity[i] = [0] * len(matrix_3)
            identity[i][i] = 1
            matrix_3[i] = [0] * len(matrix_2)
            matrix_4[i] = [0] * len(matrix_2)
            for j in range(len(matrix_2)):
                matrix_3[i][j] = matrix_2[j] * matrix_1[i][0]
                matrix_4[i][j] = matrix_3[i][j] - identity[i][j]
                self.weight[i][j] = self.weight[i][j] + matrix_4[i][j]
#        print("matrix1", matrix_1)
#        print("matrix2", matrix_2)
#        print("matrix3", matrix_3)
#        print("matrix4", matrix_4)

    def baz(self, vector):
        inputMatrix = list(vector)
        columnMatrix_1 = [0] * len(self.weight)
        result_vector = list()

        #get cols from weight and put it into columnMatrix
        for i in range(len(self.weight)):
            columnMatrix_1[i] = [0] * len(self.weight)
            for j in range(len(self.weight)):
                columnMatrix_1[i][j] += self.weight[i][j]

        for k in range(len(self.weight)):
            result = 0
            for j in range(len(self.weight)):
                result += inputMatrix[j] * columnMatrix_1[j][k]
#            print("result", result)
            if result > 0:
                result_vector.append(True)
            else:
                result_vector.append(False)

#            print("result", result)
#        print("weight", self.weight)
        print(result_vector)
        return result_vector
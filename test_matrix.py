import unittest
from matrix import Foo
from matrix import Matrix

#class TestMatrixFunction(unittest.TestCase):
#    matrix_1 = Matrix([[5, 1, 1], [1, 4, 1]])
#    matrix_2 = Matrix([[2, 2, 5], [3, 5, 3]])
#    test_matrix = matrix_2
#
#    def test_correct_result(self):
#        self.matrix_3 = self.matrix_1 + self.matrix_2
#        self.assertEqual([[7, 3, 6], [4, 9, 4]], self.matrix_3)
#
#    def test_proportional_matrix(self):
#        self.assertEqual(self.matrix_1.get_cols(), self.matrix_2.get_cols())
#        self.assertEqual(self.matrix_1.get_rows(), self.matrix_2.get_rows())
#
#    def test_get_rows_and_cols(self):
#        self.assertEqual(self.matrix_1.get_rows(), 2)
#        self.assertEqual(self.matrix_1.get_cols(), 3)


class TestFooFunction(unittest.TestCase):
    matrix_foo = Foo(4)
    matrix_foo.bar([-1, -1, -1, -1])
    matrix_foo.baz([-1, -1, 1, 1])

    def test_bar(self):
        self.assertIsNotNone(self.matrix_foo.baz([-1, -1, 1, 1]))
        self.assertNotEqual([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], self.matrix_foo.weight)

    def test_baz(self):
        self.assertEqual([False, False, False, False], self.matrix_foo.baz(([-1, -1, -1, -1])))

from matrix import Foo

matrix_foo_1 = Foo(4)
matrix_foo_2 = Foo(4)
matrix_foo_3 = Foo(4)
matrix_foo_4 = Foo(4)

matrix_foo_1.bar([-1, 1, 1, 1])
matrix_foo_1.baz([-1, 1, 1, 1])

matrix_foo_2.bar([-1, -1, 1, 1])
matrix_foo_2.baz([-1, -1, 1, 1])

matrix_foo_3.bar([-1, -1, -1, 1])
matrix_foo_3.baz([-1, -1, -1, 1])

matrix_foo_4.bar([-1, -1, -1, -1])
matrix_foo_4.baz([-1, -1, -1, -1])
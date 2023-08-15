#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 5), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Rectangle(10, 5), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        r1 = Rectangle(10, 5)
        r2 = Rectangle(11, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_two_args(self):
        r1 = Rectangle(10, 5)
        r2 = Rectangle(5, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 5)
        r2 = Rectangle(5, 5, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Rectangle(10, 5, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, 2, 7, 8)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5).__width)

    def test_width_getter(self):
        self.assertEqual(5, Rectangle(5, 10, 0, 0, 1).width)

    def test_width_setter(self):
        r = Rectangle(5, 10, 0, 0, 1)
        r.width = 8
        self.assertEqual(8, r.width)

    def test_height_getter(self):
        self.assertEqual(10, Rectangle(5, 10, 0, 0, 1).height)

    def test_height_setter(self):
        r = Rectangle(5, 10, 0, 0, 1)
        r.height = 7
        self.assertEqual(7, r.height)

    def test_x_getter(self):
        self.assertEqual(0, Rectangle(5, 10, 0, 0, 1).x)

    def test_y_getter(self):
        self.assertEqual(0, Rectangle(5, 10, 0, 0, 1).y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing width initialization of the Rectangle class."""

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 5)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 5)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 5)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 5)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 5)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 5)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 5)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 5)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 5)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 5)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 5)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 5)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)


class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing height initialization of the Rectangle class."""

    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"a": 1, "b": 2})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, True)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -5)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)


class TestRectangleX(unittest.TestCase):
    """Unittests for testing x initialization of the Rectangle class."""

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, {"a": 1, "b": 2})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, memoryview(b'abcedfg'))


class TestRectangleY(unittest.TestCase):
    """Unittests for testing y initialization of the Rectangle class."""

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 2, memoryview(b'abcedfg'))


class TestRectangleArea(unittest.TestCase):
    """Unittests for testing the area calculation of the Rectangle class."""

    def test_area(self):
        self.assertEqual(Rectangle(5, 10).area(), 50)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10).area(2)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for testing the display method of the Rectangle class."""

    def setUp(self):
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_no_offset(self):
        r = Rectangle(4, 3)
        r.display()
        self.assertEqual(sys.stdout.getvalue(), "####\n####\n####\n")

    def test_display_with_offset(self):
        r = Rectangle(4, 3, 2, 1)
        r.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n  ####\n  ####\n  ####\n")


class TestRectangleStr(unittest.TestCase):
    """Unittests for testing the __str__ method of the Rectangle class."""

    def test_str(self):
        r = Rectangle(4, 3, 2, 1, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 2/1 - 4/3")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for testing the update method of the Rectangle class with *args."""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10, 1)

    def test_update_no_args(self):
        self.r.update()
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_one_arg(self):
        self.r.update(89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self):
        self.r.update(89, 2)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_args(self):
        self.r.update(89, 2, 3)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_args(self):
        self.r.update(89, 2, 3, 4)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_more_than_four_args(self):
        self.r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/10 - 2/3")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for testing the update method of the Rectangle class with **kwargs."""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10, 1)

    def test_update_kwargs_id(self):
        self.r.update(id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs_width(self):
        self.r.update(width=2)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 2/10")

    def test_update_kwargs_height(self):
        self.r.update(height=3)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/3")

    def test_update_kwargs_x(self):
        self.r.update(x=4)
        self.assertEqual(str(self.r), "[Rectangle] (1) 4/10 - 10/10")

    def test_update_kwargs_y(self):
        self.r.update(y=5)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/5 - 10/10")

    def test_update_kwargs_all(self):
        self.r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for testing the to_dictionary method of the Rectangle class."""

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 10)
        self.assertEqual(r.to_dictionary(), {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10})


if __name__ == '__main__':
    unittest.main()

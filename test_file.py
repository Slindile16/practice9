import unittest
from main import *

class TestFunctions(unittest.TestCase):

    def test_separate_even_odd(self):
        self.assertEqual(separate_even_odd([1,2,3,4]), ([2,4],[1,3]))

    def test_flatten_once(self):
        self.assertEqual(flatten_once([[1,2],[3,[4]]]), [1,2,3,[4]])

    def test_index_map(self):
        self.assertEqual(index_map(['a','b','c']), {'a':0,'b':1,'c':2})

    def test_lowest_value_key(self):
        self.assertEqual(lowest_value_key({'a':5,'b':2,'c':3}), 'b')

    def test_sort_by_last_letter(self):
        self.assertEqual(sort_by_last_letter(["cat","dog","bat"]), ["dog","bat","cat"])

    def test_categorize_products(self):
        data = [
            {"name":"Milk","category":"Dairy"},
            {"name":"Cheese","category":"Dairy"},
            {"name":"Apple","category":"Fruit"}
        ]
        expected = {
            "Dairy":["Milk","Cheese"],
            "Fruit":["Apple"]
        }
        self.assertEqual(categorize_products(data), expected)

    def test_reverse_dict(self):
        self.assertEqual(reverse_dict({'a':1,'b':2}), {1:'a',2:'b'})

    def test_shift_left(self):
        self.assertEqual(shift_left([1,2,3,4],1), [2,3,4,1])

    def test_sort_by_username(self):
        emails = ["bob@gmail.com","alice@yahoo.com"]
        self.assertEqual(sort_by_username(emails), ["alice@yahoo.com","bob@gmail.com"])

    def test_has_common_elements(self):
        self.assertTrue(has_common_elements([1,2],[3,2]))
        self.assertFalse(has_common_elements([1,2],[3,4]))

    def test_safe_get(self):
        self.assertEqual(safe_get({'a':1},'a'), 1)
        self.assertEqual(safe_get({'a':1},'b'), "Missing")

    def test_cumulative_sum(self):
        self.assertEqual(cumulative_sum(5), 15)

    def test_custom_fibonacci(self):
        self.assertEqual(custom_fibonacci(5), [1,1,2,3,5])


if __name__ == "__main__":
    unittest.main()
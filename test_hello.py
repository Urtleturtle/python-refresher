import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertAlmostEqual(hello.sin(1), 0.8414709848078965,4)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertAlmostEqual(hello.cos(1), 0.5403023058681398,4)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertAlmostEqual(hello.tan(1), 1.5574077246549023,4)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertAlmostEqual(hello.cot(1), 0.6420926159343306,4)


if __name__ == "__main__":
    unittest.main()

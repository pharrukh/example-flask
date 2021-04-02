import unittest

import azure.functions as func
from __init__ import hello_world

class TestFunction(unittest.TestCase):
    def hellow_world_test(self):
        self.assertEqual(
            hello_world(),
            'Hello World!',
        )


if __name__ == "__main__":
    unittest.main()


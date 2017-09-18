import unittest
import os
from shifu.util.helper import Helper


class TestHelper(unittest.TestCase):
    def setUp(self):
        self._current_script_path = os.path.dirname(os.path.abspath(__file__))

    def test_get_current_path(self):
        self.assertEqual(Helper.get_current_path(), self._current_script_path)

    def test_run_shell(self):
        self.assertEqual(Helper.run_shell(['pwd', ]).strip(), self._current_script_path)

    def test_get_environment_variable(self):
        self.assertEqual(Helper.get_environment_variable("PWD"), self._current_script_path)


if __name__ == '__main__':
    unittest.main()

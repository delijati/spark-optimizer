import unittest
import pytest

from spark_optimizer.cli import main


class TestCLI(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_cli(self):
        with pytest.raises(SystemExit) as ex:
            main([])
        self.assertEqual(ex.value.code, 1)
        out, err = self.capsys.readouterr()
        self.assertTrue("Two args are needed! (type, number nodes)" in out)
        # working
        with pytest.raises(SystemExit) as ex:
            main(["me", "c4.xlarge", "4"])
        self.assertEqual(ex.value.code, 0)
        out, err = self.capsys.readouterr()
        self.assertTrue("spark.default.parallelism" in out)

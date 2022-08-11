from gendiff.run_gendiff import generate_diff
import os
basedir = os.path.abspath(os.getcwd())
print(basedir)

def test_diff():
    f = open(f'{basedir}/gendiff/tests/fixtures/result1.txt', "r")
    assert generate_diff("gendiff/tests/fixtures/file1.json", "gendiff/tests/fixtures/file2.json") == f.read()
    f.close()

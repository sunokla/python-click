""" Test suite for the core.config module.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the package is actually
being tested. If the package is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from os import environ
from pathlib import Path
import sys
import os

# 当前文件的路径
pwd = os.getcwd()
print("当前运行文件路径" + pwd)

# 当前文件的父路径
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
print("运行文件父路径" + father_path)

# 当前文件的前两级目录
grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")

grader_father1 = os.path.abspath(os.path.dirname(father_path) + os.path.sep + "..")

print("运行文件父路径的父路径" + grader_father1)
sys.path.append(grader_father1)

import pytest
from src.span.core.config import *  # tests __all__


class YamlConfigTest(object):
    """ Test suite for the YamlConfig class.

    """
    @classmethod
    @pytest.fixture
    def files(cls, tmp_path):
        """ Return configuration files for testing.

        """
        files = "conf1.yml", "conf2.yml"
        #E:\feichuang\项目工作\workspace\span\test\data
        return tuple(Path("E:/feichuang/项目工作/workspace/span/test/data", item) for item in files)

    @classmethod
    @pytest.fixture
    def params(cls):
        """ Define configuration parameters.

        """
        environ.update({"env1": "ENV1", "env2": "ENV2"})
        return {"var1": "VAR1", "var2": "VAR2", "var3": "VAR3", "env2": "VAR2"}

    def test_item(self):
        """ Test item access.

        """
        config = YamlConfig()
        config["root"] = {}
        config["root"]["key"] = "value"
        assert config["root"]["key"] == "value"
        return

    def test_attr(self):
        """ Test attribute access.

        """
        config = YamlConfig()
        config.root = {}
        config.root.key = "value"
        assert config.root.key == "value"
        return

    @pytest.mark.parametrize("root", (None, "root"))
    def test_init(self, files, params, root):
        """ Test the __init__() method for loading a file.

        """
        merged = {"url": "123", "usrname": "sunlei", "password": "123"}
        config = YamlConfig(files, root, params)

        if root:
            assert config == {root: merged}
        else:
            assert config == merged
        return

    @pytest.mark.parametrize("root", (None, "root"))
    def test_load(self, files, params, root):
        """ Test the load() method.

        """
        merged = {"url": "123", "usrname": "sunlei", "password": "123"}
        config = YamlConfig()
        config.load(files, root, params)
        if root:
            assert config == {root: merged}
        else:
            assert config == merged
        return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))

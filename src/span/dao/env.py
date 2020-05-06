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
print(sys.path)
from pathlib import Path
from src.span.core.config import *

def GetMainConnectString():
    config = YamlConfig()
    config.load("E:/feichuang/项目工作/workspace/span/etc/config.yml", None, None)
    return config.get('url')

def GetMainConnectString1():
    config = YamlConfig()
    config.load("E:/feichuang/项目工作/workspace/span/etc/config.yml", None, None)
    return config.get('url1')


# def main():
#     GetMainConnectString()
#
# if __name__ == "__main__":
#     try:
#         status = main()
#     except:
#
#         raise  # print stack trace
#     else:
#         raise SystemExit(status)


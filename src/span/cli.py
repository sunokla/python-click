""" Implementation of the command line interface.

"""
from argparse import ArgumentParser
from inspect import getfullargspec
import sys
import os
# 当前文件的路径
# pwd = os.getcwd()
# print("当前运行文件路径" + pwd)
#
# # 当前文件的父路径
# father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# print("运行文件父路径" + father_path)
#
# # 当前文件的前两级目录
# grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
#
# grader_father1 = os.path.abspath(os.path.dirname(father_path) + os.path.sep + "..")
#
# print("运行文件父路径的父路径" + grader_father1)
# sys.path.append(father_path)
# print(sys.path)
from .api import paraservice
from .core.logger import logger
import fire
import datetime
__all__ = "main"

def main(argv=None) -> int:
    """ Execute the application CLI.

    :param argv: argument list to parse (sys.argv by default)
    :return: exit status
    """
    # args = _args(argv)
    # logger.start(args.warn or "DEBUG")  # can't use default from config yet
    # logger.debug("starting execution")
    # config.load(args.config)
    # config.core.config = args.config
    # if args.warn:
    #     config.core.logging = args.warn
    logger.stop()  # clear handlers to prevent duplicate records
    logger.start()

    #command = args.command
    # args = vars(args)
    # spec = getfullargspec(command)
    # if not spec.varkw:
    #     # No kwargs, remove unexpected arguments.
    #     args = {key: args[key] for key in args if key in spec.args}
    try:

       fire.Fire(Building)

    except RuntimeError as err:
        logger.critical(err)
        return 1
    logger.debug("successful completion")
    return 0


class Building(object):

    def __init__(self, name, type=1):
        self.name = name
        self.type = type

    def __str__(self):
        return f'name: {self.name}, type: {self.type}'

    def method_a1(self,a, b):
        paraservice.ParaA.method_a1(None, a, b)
        return 0
    def method_b2(a, b, c, d):
        paraservice.ParaB.method_b2(a, b, c, d)
        return 0
    def method_d(a):
        paraservice.ParaD.method_d1(a)
        return 0

# Make the module executable.

if __name__ == "__main__":
    try:
        status = main()
    except:
        logger.critical("shutting down due to fatal error")
        raise  # print stack trace
    else:
        raise SystemExit(status)

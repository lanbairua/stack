# coding=utf-8
from stack_base import *


class Stack(StackBase):
    def __getattribute__(self, item):
        """ 实例化后is_insurance为真, 可以直接访问peek """
        return super(StackBase if item in ["peek"] else Stack, self).__getattribute__(item)
        # 暂时没有想到什么魔法方法替代peek

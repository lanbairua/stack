# coding=utf-8
class Node(object):
    """ 栈的节点 """

    def __init__(self, items, Next=None, count=0):
        # type: (object, object, int) -> None
        """  """
        super(Node, self).__setattr__("items", items)
        super(Node, self).__setattr__("next", Next)
        super(Node, self).__setattr__("count", count)

    def __getattribute__(self, name):
        # type: (str) -> None
        """ 修改成员信息时做出拦截处理 """

    def __setattr__(self, key, value):
        # type: (str, object) -> None
        """ 获取成员信息时做出拦截处理 """


class StackBase(object):
    top = None

    def __new__(cls, name=None, is_insurance=False):
        # type: (StackBase, str, bool) -> object or None
        """ 根据栈名返还实例, 重复的栈名从节点获取之前对应的实例并返还 """
        if name is None:
            return
        instance = getattr(Node, name, None)
        if instance is None:
            return object.__new__(cls)
        return instance

    def __init__(self, name=None, is_insurance=False):
        # type: (str, bool) -> None
        """ 实例化栈 """
        if getattr(Node, name, None) is None:
            super(StackBase, self).__setattr__("name", name)
            super(StackBase, self).__setattr__("is_insurance", is_insurance)
            setattr(Node, name, self)
        else:
            del self

    def __len__(self):
        # type: () -> int
        """ 可以通过len()方法获取栈的大小 """
        top = super(StackBase, self).__getattribute__("top")
        if top is None:
            return 0
        return super(Node, top).__getattribute__("count")

    def __repr__(self):
        # type: () -> object
        """ 可以通过repr()方法获取字符串形式的栈顶元素 """
        return repr(super(StackBase, self).__getattribute__("peek")())

    def __str__(self):
        # type: () -> str
        """ 可以通过str()方法获取栈的名字 """
        return super(StackBase, self).__getattribute__("name")

    def __iter__(self):
        # type: () -> object
        """ 迭代器，生成迭代对象时调用，返回值必须是对象自己,然后for可以循环调用next方法 """
        return self

    def __getattribute__(self, name):
        # type: (str) -> str
        """ 获取成员信息时, 根据是否加密做出拦截处理 """
        is_insurance = super(StackBase, self).__getattribute__("is_insurance")
        if not is_insurance:
            return super(StackBase, self).__getattribute__(name)
        else:
            errorInfo = "成员信息已被加密, 不可调用"
            raise Warning(errorInfo)

    def __setattr__(self, key, value):
        # type: (str, object) -> None
        """ 修改成员信息时, 根据是否加密做出拦截处理 """
        is_insurance = super(StackBase, self).__getattribute__("is_insurance")
        if key in ["top", "name", "count", "is_insurance"]:
            errorInfo = "%s成员不允许修改" % key
            raise Warning(errorInfo)
        elif not is_insurance:
            super(StackBase, self).__setattr__(key, value)
        else:
            errorInfo = "成员信息已被加密"
            raise Warning(errorInfo)

    def __getattr__(self, name):
        # type: (str) -> None
        """ 防止栈报错 """
        return None

    def __call__(self, *args):
        # type: (dir) -> None
        """ 方便懒比实例化后入栈 """
        push = super(StackBase, self).__getattribute__("push")
        for items in args:  # python3千万别直接用map(push, args)替代!!!
            push(items)

    def __add__(self, other):
        # type: (object) -> int
        """  """
        push = super(StackBase, self).__getattribute__("push")
        push(other)
        return len(self)

    def __sub__(self, other):
        # type: (object) -> int
        """  """
        top = super(StackBase, self).__getattribute__("peek")()
        if top == other:
            super(StackBase, self).__getattribute__("pop")()
        return len(self)

    def __next__(self):  # python3
        # type: () -> object
        """ 迭代器迭代中会栈顶元素， 栈顶元素会改变 """
        if len(self):
            return super(StackBase, self).__getattribute__("pop")()
        else:
            raise StopIteration()

    def next(self):  # python2
        # type: () -> object
        """ 迭代器迭代中会栈顶元素， 栈顶元素会改变 """
        if len(self):
            return super(StackBase, self).__getattribute__("pop")()
        else:
            raise StopIteration()

    def is_empty(self):
        # type: () -> bool
        """ 判断栈是否为空 """
        top = super(StackBase, self).__getattribute__("top")
        return top is None

    def push(self, items):
        # type: (object) -> None
        """ 栈的压入, 先入后出 """
        top = Node(items, super(StackBase, self).__getattribute__("top"), len(self) + 1)
        super(StackBase, self).__setattr__("top", top)

    def pop(self):
        # type: () -> object
        """ 栈顶弹出，原来的栈顶元素会改变 """
        top = super(StackBase, self).__getattribute__("top")
        Next = super(Node, top).__getattribute__("next")
        if top is None:
            raise ValueError
        super(StackBase, self).__setattr__("top", Next)
        return super(Node, top).__getattribute__("items")

    def peek(self):
        # type: () -> object
        """ 返还栈顶元素 """
        top = super(StackBase, self).__getattribute__("top")
        if top is None:
            error_info = ValueError("空栈无法任何元素")
            raise error_info
        return super(Node, top).__getattribute__("items")

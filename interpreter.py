# -*- coding: utf-8 -*-  
# --------------------------------
# hasattr(object, name)
# 判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
# 需要注意的是name要用括号括起来
# 如 hasattr(datetime.datetime, "now") -> True
# -------------------------------- 
# getattr(object, name[,default])
# 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
# 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
# 可以在后面添加一对括号。
# 如 getattr(datetime.datetime, "now") -> now()
# ---------------------------------
# setattr(object, name, values)
# 给对象的属性赋值，若属性不存在，先创建再赋值。
# ----------------------------------


import datetime

what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)
                     ],
    "numbers": [7, 5],
    "names": ["a", "b"]
}


class Interpreter(object):
    """docstring for Interpreter"""

    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]
        if instruction in numbers:
        	argument = what_to_execute["numbers"][argument]
        elif instruction in names:
        	argument = what_to_execute["names"][argument]
        return argument

    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if argument is None:
            	bytecode_method()
            else:
            	bytecode_method(argument)



interpt = Interpreter()
interpt.run_code(what_to_execute)



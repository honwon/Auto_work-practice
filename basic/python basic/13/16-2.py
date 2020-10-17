class simpleTest:
    def __init__(self):
        self.prefix = "you said: "
        self.postfix = "\n"+"-"*20+"\n"

    def print_with_fix(self, string):
        print(self.prefix +string + self.postfix)


simple = simpleTest()
simple.print_with_fix("ㅠㅠㅠ 어떻게 되는거")



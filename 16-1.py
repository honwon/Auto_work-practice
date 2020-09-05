class simpleTest:

    def ddd():
        print("testttt")

    def print_skip(self, string):
        if 'skip' in string:
            print("Skip")
            return
        
        print(string)

simplt = simpleTest()
simplt.print_skip('bad')
simplt.print_skip("skip text")
simplt.print_skip("fastcampus")





class SimpleTest:
    def print_skip(self, string):
        if 'skip' in string:
            print('Skip')
            return

        print(string)

simple = SimpleTest()

simple.print_skip('bad')
simple.print_skip('skip text')
simple.print_skip('fastcampus')

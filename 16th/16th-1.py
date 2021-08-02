class SimpleTest:
    def __init__(self):
        self.my_data = 100
        print('Call init!')

simple = SimpleTest()
simple2 = SimpleTest()
simple3 = SimpleTest()
print(simple.my_data)
print(simple2.my_data)
print(simple3.my_data)

simple.my_data = 10
simple2.my_data = 20
simple3.my_data = 30
print(simple.my_data)
print(simple2.my_data)
print(simple3.my_data)

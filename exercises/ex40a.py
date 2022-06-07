import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple']
mystuff.apple()
mystuff.tangerine

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

mystuff['apples']

mystuff.apples()
print(mystuff.tangerine)

thing = MyStuff()
thing.apples()
print(thing.tangerine)






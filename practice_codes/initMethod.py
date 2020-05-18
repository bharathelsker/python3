class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is {} CPU with {} RAM'.format(self.cpu, self.ram))

    def bye(self):
        print('BYE!!!')


comp1 = computer('i5', 16)
comp2 = computer('i3', 8)

comp1.config()
comp2.config()

comp2.bye()


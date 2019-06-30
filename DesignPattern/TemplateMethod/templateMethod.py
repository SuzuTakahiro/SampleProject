
class AbstractCalculator:

    def inputParam(self):
        pass
    def calc(self):
        pass
    def printResult(self):
        pass
    def execute(self):
        self.inputParam()
        self.calc()
        self.printResult()

class AddCaluculator(AbstractCalculator):
    def inputParam(self):
        self.x = 10
        self.y = 15
    def calc(self):
        self.result = self.x + self.y
    def printResult(self):
        print(self.result)

class MultiCaluculator(AbstractCalculator):
    def inputParam(self):
        self.x = 10
        self.y = 15.5
    def calc(self):
        self.result = self.x * self.y
    def printResult(self):
        print(self.result)

if __name__ == '__main__':

    addCaluculator = AddCaluculator()
    multiCaluculator = MultiCaluculator()

    addCaluculator.execute()
    multiCaluculator.execute()

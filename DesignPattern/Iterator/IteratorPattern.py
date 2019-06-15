class Iterator:
    def hasNext(self):
        return
    def next(self):
        return

class Aggregate:
    def iterator(self):
        return

class OddIterator(Iterator):
    def __init__(self,numbers):
        self.numbers=numbers
        self.index = 0
    def hasNext(self):
        if self.index < len(self.numbers):
            return True
        else :
            return False
    def next(self):
        number = self.numbers[self.index]
        self._countup()
        return number
    def _countup(self):
        while True:
            self.index += 1
            if self.index > len(self.numbers) - 1:
                break
            elif self.numbers[self.index] % 2 == 0:
                break

class EvenIterator(Iterator):
    def __init__(self,numbers):
        self.numbers=numbers
        self.index = 0

    def hasNext(self):
        if self.index < len(self.numbers):
            if self.numbers[self.index] == 0:
                self._countup()
                return self.hasNext()
            return True
        else :
            return False

    def next(self):
        number = self.numbers[self.index]
        self._countup()
        return number

    def _countup(self):
        while True:
            self.index += 1
            if self.index > len(self.numbers) - 1:
                break
            elif self.numbers[self.index] > 0 and self.numbers[self.index] % 2 == 1:
                break


class NormalIterator(Iterator):
    def __init__(self,numbers):
        self.numbers=numbers
        self.index = 0
    def hasNext(self):
        if self.index < len(self.numbers):
            return True
        else :
            return False
    def next(self):
        number = self.numbers[self.index]
        self.index +=1
        return number
class Numbers(Aggregate):
    def __init__(self):
        self.numbers=[0,1,2,3,4,5,6,7,8,9,10]
    def iterator(self):
        # return NormalIterator(self.numbers)
        # return EvenIterator(self.numbers)
        return OddIterator(self.numbers)

if __name__ == '__main__':
    numbers = Numbers()
    iterator = numbers.iterator()
    while iterator.hasNext():
        print(iterator.next())

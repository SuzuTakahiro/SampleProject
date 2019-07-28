import os
class AbstractFactory:
    def create(self,owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p
    def createProduct(self,owner):
        pass
    def registerProduct(self,product):
        pass
        
class Product:
    def use(self):
        pass

class UnitTestFolderFactory(AbstractFactory):
    def __init__(self,basename):
        self.unittest_base =os.path.dirname(__file__)
        if basename != "":
            self.unittest_base = os.path.join(self.unittest_base,basename)
        self.unittest =[]
    def createProduct(self,folder):
        if(folder==""):
            print("フォルダ名が不明です")
            return None
        self.path = os.path.join(self.unittest_base,folder)
        return UnitTestFolder(self.path)

    def registerProduct(self,folder):
        if folder is None :
            return
        self.unittest.append(folder.unittestName())

    def printUnittestFolderList(self):
        print("登録されている作成予定リスト")
        for child in self.unittest:
            print(child)


class UnitTestFolder(Product):

    def __init__(self,folder):
        print(folder+"を作成します。")
        self.folder = folder
    def use(self):
        children = ["src","input","output"]
        if self.folder =="" :
            print("フォルダ名が不明です")
            return
        os.makedirs(self.folder)
        for child in children:
            path = os.path.join(self.folder,child)
            os.makedirs(path)
    def unittestName(self):
        return os.path.basename(self.folder)

if __name__ == '__main__':
    factory = UnitTestFolderFactory("unittest")
    unit0 = factory.create("unittest0")
    unit1 = factory.create("unittest1")
    unit2 = factory.create("unittest2")
    unit0.use()
    unit1.use()
    unit2.use()
    factory.printUnittestFolderList()

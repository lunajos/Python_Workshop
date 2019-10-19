class handleData:
    def __init__(object, num, name, func):
        object.num = num
        object.name = str(name)
        object.func = str(func)

    def showNames(self):
            print(self.name);

data = handleData(23, 'Jose', 'sd')
data.showNames()
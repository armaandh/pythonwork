class person:
    def __init__(self):
        self.__name=''
        self.__creditcardnumber = ''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value
# documentation added 
p = person()
p.name = "Steve jobs"
print(p.name)

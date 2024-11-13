class fileManager:
    def __init__(self,openFile='') -> None:
        self.contents = ''
        self.header = openFile
        try:
            f = open(openFile,"r")
            self.contents = f.read()
            f.close()
        except FileNotFoundError:
            print('error: file does not exist')

    def overwrite(self,text):
        temp = open(self.header,'w')
        temp.write(text)
        temp.close()

    def __str__(self) -> str:
        return self.contents
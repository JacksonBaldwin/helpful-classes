import json
class cookies: #interact with json objects and files
    def __init__(self,fname='cookies.json') -> None:
        self.fname = fname
        try:
            files = open(fname,'r')
        except:
            files = open(fname,'x')
        f = files.read()
        if f == '':
            f = "{" + "}"
        self.cookies = json.loads(f)
        files.close()

    def new(self,name,val=0) -> bool: #to change content of a preexisting key, call new with the name and new value
        """create a new json object within current session"""
        try:
            self.cookies.update({name:val})
            return True
        except:
            return False
        
    def update(self):
        """save current json to opened file"""
        files = open(self.fname,'w')
        files.write(json.dumps(self.cookies))
        files.close()
    
    def remove(self,item):
        """delete json object from the current opened session"""
        del self.cookies[item]
        return True
    
    def verify(self,user=['username','password']):
        if user[0] in self.cookies:
            uval = self.cookies[user[0]]
            if uval == user[1]:
                return True
        return False

    def __str__(self) -> str:
        return str(self.cookies)
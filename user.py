class user:
    userid={"pinid":"class"}
    def __init__(self,username,pin,accnum,usermoney,realmoney,emoney):
        self.__username=username
        self.__pin=pin
        self.__usermoney=usermoney
        self.__emoney=emoney
        self.__realmoney=realmoney
        self.__accnum=accnum
        user.userid.setdefault(self.__accnum,self)
        
    @property
    def userInfo(self):
        return {"username":self.__username,"pin":self.__pin,"accountnumber":self.__accnum}
    
    @property
    def userCash (self):
        return {"usercash":self.__usermoney,"emoney":self.__emoney,"realmoney":self.__realmoney}
    
    @userCash.setter
    def userCash(self,cashChanges):
        self.__usermoney=cashChanges[0]
        self.__emoney=cashChanges[1]
    
    @userCash.deleter
    def userCash(self):
        self.__usermoney=0
        self.__emoney=0
    
    @classmethod
    def get(cls, value):
        return [cls.userid[pin] for pin in cls.userid if  pin == value]

    

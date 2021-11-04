from user import user
class atm_machine:
    def __init__(self,script,cardInserted=False,moneyLeft=2000000000):
        self.__transc="none"
        self.__script=open(str(script),"a+")
        self.__cardInserted=cardInserted
        self.__moneyLeft=moneyLeft
        self.__active=False
    def releaseCard(self):
        if self.__cardInserted==True:
            self.__cardInserted=False
        else:
            return "The card hasn\'t inserted yet"
    @property
    def condATM(self):
        return "active:{}\nCardInside:{}".format(self.__cardInserted,self.__active)
    @condATM.setter
    def condATM(self,cond):
        self.__cardInserted,self.__active=cond[0],cond[1]
    def getactive(self):
        return self.__active
    def cardgetter(self):
        return self.__cardInserted
    
    def decorator(func):
        def decorate_it(*args,**kwargs):
            for ast in range(0,10):
                if ast==0:
                    print("*"*60)
                elif ast==len(list(range(0,10)))//2:
                    func(*args,**kwargs)
        return decorate_it
    @decorator
    def pinchecker(self,instc):
        self.__script.truncate(0)
        try:
            input_pin=input("""Please input your pin...:\n""")
            return int(input_pin)== instc.userInfo["pin"]
        except:
            return False
    def setTransc(self,transaction):
        self.__transc=transaction
    @decorator
    def selectTransaction(self,instc):
        while True:
            inputTransc=input("""
        What the transaction do you want ?
        (A)Withdraw money
        (B)Transfer
        (C)Check cash
        (D)E-money payment
        (E)cancel\n """)
            if inputTransc.upper()=="A" or inputTransc.upper()=="B":
                self.__script.write("{} is choosing \"Withdraw money\"\n".format(instc.userInfo["username"])) if inputTransc.upper()=="A" else self.__script.write("{} is choosing \"Transfer\"\n".format(instc.userInfo["username"]))
                return self.WithdrawMoney(instc) if inputTransc.upper()=="A" else self.Transfer(instc)
            elif inputTransc.upper()=="C" or inputTransc.upper()=="D":
                self.__script.write("{} is choosing \"Check cash\"\n".format(instc.userInfo["username"])) if inputTransc.upper()=="B" else self.__script.write("{} is choosing \"emoney payment\"\n".format(instc.userInfo["username"]))
                return self.checkUserMoney(instc) if inputTransc.upper()=="C" else self.emoneyPayment(instc)
            elif inputTransc.upper()=="E":
                self.__script.write("{} is choosing \"cancel\"\n".format(instc.userInfo["username"]))
                self.condATM=[False,True]
            else:
                pass
    @decorator
    def checkcash(self):
        return self.__moneyLeft
    @decorator
    def checkUserMoney(self,instc):
        self.__script.write(("{} is checking his/her  ").format(instc.userInfo["username"]))
        print("""Your cash is Rp{:,}""".format(instc.userCash["usercash"]))
        return self.looper("TransferSucceeded",instc)
    @decorator
    def emoneyPayment(self,instc):
        while True:
            inputamm=input("""
        how many cash do you want
        (A)Rp10.000
        (B)Rp50.000
        (C)Rp100.000
        (D)Rp200.000
        (E)Cancel\n
         """)
            if inputamm.upper()=="A" or inputamm.upper()=="B":
                self.__script.write("{} is choosing \"Rp10.000\"\n".format(instc.userInfo["username"])) if inputamm.upper()=="A" else self.__script.write("{} is choosing \"Rp50.000\"\n".format(instc.userInfo["username"]))
                instc.userCash["emoney"]+=10000 if inputamm.upper()=="A" else  instc.userCash["emoney"]+50000
                instc.userCash["usercash"]-=10000 if inputamm.upper()=="A" else  instc.userCash["usercash"]-50000
            elif inputamm.upper()=="C" or inputamm.upper()=="D":
                self.__script.write("{} is choosing \"Rp100.000\"\n".format(instc.userInfo["username"])) if inputamm.upper()=="B" else self.__script.write("{} is choosing \"Rp200.000\"\n".format(instc.userInfo["username"]))
                instc.userCash["emoney"]+=100000 if inputamm.upper()=="B" else instc.userCash["emoney"]+200000
                instc.userCash["usercash"]-=100000 if inputamm.upper()=="A" else  instc.userCash["usercash"]-200000
            elif inputamm.upper()=="E":
                self.__script.write("{} is choosing \"cancel\"\n".format(instc.userInfo["username"]))
                return self.selectTransaction(instc)
            return self.looper("TransferSucceeded",instc)
    @decorator
    def WithdrawMoney(self,instc):
        while True:
            inputamm=input("""Input How many money do you want to take:\n""")
            if inputamm=="cancel":
                self.__script.write("{} is choosing \"cancel\"\n".format(instc.userInfo["username"]))
                self.selectTransaction(instc)
            elif inputamm.isnumeric():
                self.__script.write("{} is taking his/her money back in Rp{} \n".format(instc.userInfo["username"],inputamm))
                instc.userCash["realmoney"]+=int(inputamm)
                self.__moneyLeft-=int(inputamm)
                return self.looper("TransferSucceeded",instc)

    @decorator
    def Transfer (self,instc):
        while True:
            inputTarget=int(input("""What is the reciever's account number ?"""))
            print(inputTarget)
            if inputTarget in instc.__class__.userid :
                inputAmmount=int(input(""" How much money are you going to transfer?"""))
                instc.__class__.get(inputTarget)[0].userCash["usercash"]+=inputAmmount
                self.__script.write("{} is transfering his/her money  in Rp{:,} to {} \n".format(instc.userInfo["username"],inputAmmount,instc.__class__.get(inputTarget)[0].userInfo["username"]))
                return self.looper("TransferSucceeded",instc)
    @decorator
    def looper(self,cond,instc):
        if cond=="TransferSucceeded":
            inputforLooper=input("""
            Do you want to do a transfer again?
            (A)Yes
            (B)No
            """)
            if inputforLooper.upper()=="A":
                return self.selectTransaction(instc) 
            else:
                return None
            

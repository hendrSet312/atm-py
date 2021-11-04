from atm import atm_machine
from user import user

#self,name,pin,id account,balance,realmoney,emoney
atm1= atm_machine("record.txt",True)
#userExample= user("John Doe",123456,894327837878,70000,60000,80000)
user1= user("{Name}","{pin}","{id account}","{balance}","{real money}","{e-money}")
user2= user("{Name}","{pin}","{id account}","{balance}","{real money}","{e-money}")
#inserting the atm-card and activate the atm machine 
atm1.condATM=[True,True]
#run the atm program
atmcond,atminserted= atm1.condATM.split("\n")
def main():
while atminserted=='CardInside:True':
    pin=atm1.pinchecker(user1)
    if pin==False:
        break
    else:
        atm_run= atm1.selectTransaction(user1)
        if atm_run==None:
            atm1.releaseCard()
            print("The transaction is finished, you can see the log file for your current activities")
            break



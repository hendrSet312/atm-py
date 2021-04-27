from atm import atm_machine
from user import user

#self,username,pin,accnum,usermoney,realmoney,emoney
atm1= atm_machine("record.txt",True)
user1= user("Yogi Pangayo",123456,894327837878,70000,60000,80000)
user2= user("Devin setiawan ",123426,24689012992,80000,90000,100000)
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
            print("The transaction is finished, you can see the log for activities")
            break



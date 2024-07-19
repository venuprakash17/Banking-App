import json
import os
from Services.createAccount import createJSONFile
from datetime import datetime
def createJSONFileDep(data):
    with open('user.json','w') as f:
        json.dump(data, f, indent=4)


def WithdrawDeposite(opp):
    with open('user.json', 'r') as f:
        content = json.load(f)
    print(content['customers'])
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    Amount = int(input('Enter your amount'))
    for i in content['customers']:
        print(i,"\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
            print(i["balance"])
            now = datetime.now()
            if opp == 'W':
                finalBalance = i["balance"] - Amount
                Transaction_str = "DEBIT: "+"------"+str(Amount)+ "--- Closing Balance:"+str(finalBalance) + "  @  "+ str(now)
                i["Transactions"].append(Transaction_str)
            else:
                finalBalance = i["balance"] + Amount
                Transaction_str = "Credit: " + "------" + str(Amount) + "--- Closing Balance: " + str(finalBalance)+ "   @  " + str(now)
                i["Transactions"].append(Transaction_str)
            i["balance"] = finalBalance
            print('vaildated')
            os.remove('C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
            createJSONFileDep(content)

'''
def deposite():
    with open('user.json', 'r') as f:
        content = json.load(f)
    print(content['customers'])
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    deposite_Amount = int(input('Enter your amount'))
    for i in content['customers']:
        print(i,"\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
            print(i["balance"])
            finalBalance = i["balance"]+deposite_Amount
            i["balance"] = finalBalance
            print('vaildated')
            os.remove('C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
            createJSONFileDep(content)
    # print(atmNumberInp)
    # print(atmPinInp)
def Withdraw():
    with open('user.json', 'r') as f:
        content = json.load(f)
    print(content['customers'])
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    Withdraw_Amount = int(input('Enter your amount'))
    for i in content['customers']:
        print(i,"\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
            print(i["balance"])
            finalBalance = i["balance"]-Withdraw_Amount
            i["balance"] = finalBalance
            print('vaildated')
            os.remove('C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
            createJSONFileDep(content)
'''
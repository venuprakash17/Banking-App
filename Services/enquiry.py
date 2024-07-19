import json


def enquiry(option):
    with open('user.json', 'r') as f:
        content = json.load(f)
    # print(content['customers'])
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    # Amount = int(input('Enter your amount'))
    for i in content['customers']:
        # print(i, "\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
            if (option == "E"):
                print('Hello, ', i['name'])
                print('Your available Balance: ', i['balance'])
                print('Your transactions: ', i["Transactions"])
            elif option == 'M':
                print('Your recent 4 transactions: ')
                for k in i["Transactions"][-4:]:
                    print(k)
            # print('Your available Balance: ', i['balance'])


'''
def MiniStatement():
    with open('user.json', 'r') as f:
        content = json.load(f)
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    # Amount = int(input('Enter your amount'))
    for i in content['customers']:
        # print(i, "\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
'''

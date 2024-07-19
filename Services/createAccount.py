import random
import json


def createAccount():
    '''This is a function to create a bank account'''
    # print('Account created')
    name = input('enter your name').strip().title()
    fatherName = input('enter your father name').strip().title()
    DOB = input("Enter your DOB DD/MM/YYYY ")
    aadharNumber = input('Enter your adhar')
    phoneNumber = input('Enter your Phone number')
    panNumber = input('Enter your PAN Number use caps for all letters')
    balance = 10000
    Monthly_Income = int(input("Enter your monthly income"))
    Transactions = []
    loans = {}
    atmNumber = random.randint(111111111111111, 9999999999999999)
    atmCVV = random.randint(111, 999)
    atmPin = random.randint(1111, 9999)
    accountNumber = random.randint(1111111111, 9999999999)
    return {"name": name,
            "fatherName": fatherName,
            "DOB": DOB,
            "aadharNumber": aadharNumber,
            "phoneNumber": phoneNumber,
            "panNumber": panNumber,
            "atmNumber": atmNumber,
            "atmCVV": atmCVV,
            "atmPin": atmPin,
            "accountNumber": accountNumber,
            "balance": balance,
            "Transactions": Transactions,
            "Monthly_Income": Monthly_Income,
            "loans": loans}


def createJSONFile(data):
    final_dict = {"customers": [data]}
    print(final_dict)
    with open('user.json', 'w') as f:
        json.dump(final_dict, f, indent=4)


def addUserJSON(data):
    with open('user.json', 'r') as f:
        content = json.load(f)
    print(content['customers'])
    lst = content['customers']
    lst.append(data)
    print(content)
    print(lst)
    final_dict = {"customers": lst}
    with open('user.json', 'w') as file:
        json.dump(final_dict, file, indent=4)

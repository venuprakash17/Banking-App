import json
import os
from Services.Withdraw_deposite import createJSONFileDep


def pinChange():
    with open('user.json', 'r') as f:
        content = json.load(f)
    # print(content['customers'])
    # atmNumberInp = int(input("enter your ATM number"))
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    pin_1 = int(input('Enter your new to update'))
    pin_2 = int(input('Confirm your pin update'))
    for i in content['customers']:
        # print(i, "\n")
        if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp and pin_1 == pin_2:
            i["atmPin"] = pin_1
            # print('vaildated')
            os.remove('C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
            createJSONFileDep(content)

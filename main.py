import json
import os
from Services.createAccount import createAccount
from Services.createAccount import createJSONFile
from Services.createAccount import addUserJSON
from Services.Withdraw_deposite import WithdrawDeposite
from Services.pin_change import pinChange
from Services.enquiry import enquiry
from Services.Loans import loan
print("""
0 -> create account
1 -> Enquiry
2 -> Deposite
3 -> Withdraw
4 -> Pin change
5 -> Apply for a loan
6 -> Mini Statments
""")

# Featured - ATM, test PIN -
#  Helps the user to select option for banking

while True:
    option = int(input('Select options above'))
    if option == 0:
        print('0 -> create account')
        dict_user = createAccount()
        print(dict_user)
        if os.path.exists('user.json') and os.path.getsize('user.json') != 0:
            addUserJSON(dict_user)
        else:
            createJSONFile(dict_user)
        break
    elif option == 1:
        enquiry('E')
        print('1 -> Enquiry')
        break
    elif option == 2:
        WithdrawDeposite('D')
        # Deposite
        break
    elif option == 3:
        WithdrawDeposite('W')
        print('3 -> Withdraw')
        break
    elif option == 4:
        pinChange()
        print('4 -> Pin change')
        break
    elif option == 5:
        loan()
        # print('5 -> Apply for a loan')
        break
    elif option == 6:
        enquiry('M')
    else:
        print('Your selection is wrong')
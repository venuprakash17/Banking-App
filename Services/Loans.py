import json
import os
from Services.Withdraw_deposite import createJSONFileDep

dict_loan = {
    "home": 6,  # 6 time of user montly income.
    "gold": 3500,  # times per gram
    "education": {
        90: 600000,
        80: 500000,
        70: 400000,
        60: 300000
    },
    "crop": 50000  # times per  acre
}

dict_intrest = {
    "home": 12,  # intrest per year.
    "gold": 16,
    "education": 8,
    "crop": 10
}


def education_Loan(percent):
    if percent >= 90:
        loan_amount = dict_loan["education"][90]
    elif percent < 90 and percent >= 80:
        loan_amount = dict_loan["education"][80]
    elif percent < 80 and percent >= 70:
        loan_amount = dict_loan["education"][70]
    elif percent < 70 and percent >= 60:
        loan_amount = dict_loan["education"][60]
    else:
        loan_amount = 0
    if loan_amount != 0:
        term = int(input("Enter your EMI period in years"))  # 5
        intrest_amount = ((dict_intrest["education"] * term) * loan_amount) / 100  # 432000
        total_paying_amount = loan_amount + intrest_amount
        EMI = total_paying_amount / (term * 12)  # 19200
        return {"EMI": EMI,
                "total_paying_amount": total_paying_amount,
                "loan_amount": loan_amount,
                "intrest_amount": intrest_amount,
                "Tenure": term * 12}
    else:
        return 0


def Gold_crop_home_loan(loanType, number):  # home - 50000 , gold = 50, crop=5 a
    loan_amount = dict_loan[loanType] * number  # 35000 # 500000
    term = int(input("Enter your EMI period in years"))  # 5
    intrest_amount = ((dict_intrest[loanType] * term) * loan_amount) / 100  # 28000
    total_paying_amount = loan_amount + intrest_amount  # 63000
    EMI = total_paying_amount / (term * 12)  # 1050
    return {"EMI": EMI,
            "total_paying_amount": total_paying_amount,
            "loan_amount": loan_amount,
            "intrest_amount": intrest_amount,
            "Tenure": term * 12}


def loan():
    with open('user.json', 'r') as f:
        content = json.load(f)
    # print(content['customers'])
    atmNumberInp = int(input("enter your ATM number"))
    atmPinInp = int(input('Enter your ATM pin'))
    suretyInp = int(input("enter your surety account number"))
    Succ_surety = False
    for k in content['customers']:
        if k["accountNumber"] == suretyInp:
            print("Surety added successfully")
            print('Your Surety:', k["name"])
            Succ_surety = True
            break
    if Succ_surety:
        for i in content['customers']:
            if i["atmNumber"] == atmNumberInp and i["atmPin"] == atmPinInp:
                loan_opp = int(input('''
                Select your loan type below:
                1: Home loan,
                2: Gold Loan,
                3: Education Loan,
                4: Crop loan
                '''))
                if loan_opp == 1:
                    # print(Home_loan(i["Monthly_Income"]))
                    homeLoan = Gold_crop_home_loan('home', i["Monthly_Income"])
                    i["loans"]["Home"] = homeLoan
                    os.remove(
                        'C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
                    createJSONFileDep(content)
                    # print(i["loans"])
                    # print(i)
                    print(i["loans"]["Home"])
                elif loan_opp == 2:
                    grams = int(input("Enter number of gms you want to deposit"))
                    goldLoan = Gold_crop_home_loan('gold', grams)
                    i["loans"]["Gold"] = goldLoan
                    os.remove(
                        'C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
                    createJSONFileDep(content)
                    print("Gold loan")
                    print(i["loans"]["Gold"])
                elif loan_opp == 3:
                    percentage = int(input("Enter your percentage"))
                    educationLoan = education_Loan(percentage)
                    if educationLoan !=0:
                        i["loans"]["Education"] = educationLoan
                        os.remove('C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
                        createJSONFileDep(content)
                        # print("Crop Loan")
                        print(i["loans"]["Crop"])
                        print("Education loan")
                    else:
                        print("You can't get a loan with your percentage")
                elif loan_opp == 4:
                    a = int(input("Total land"))
                    cropLoan = Gold_crop_home_loan('crop', a)
                    i["loans"]["Crop"] = cropLoan
                    os.remove(
                        'C:/Users/thimm/Documents/Python_end_to_end/Capstone_final_project/Bank_APP_end_to_end/user.json')
                    createJSONFileDep(content)
                    print("Crop Loan")
                    print(i["loans"]["Crop"])
                else:
                    print("You entered an invalid option")
    else:
        print("Your Surety not valid")

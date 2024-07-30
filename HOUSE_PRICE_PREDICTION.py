#HOUSE PRICE PRDICTION
user_name=[]
user_aadhar=[]
pass_word=[]
phone_no=[]
while True:
    print("1.sign-in 2.log-in 3.change-password")
    ch=int(input("Enter You Are Choice : "))
    if(ch==1):
        ua=int(input('Enter The User Aadhar Number : '))
        if ua not in user_aadhar:
            uno=int(input('Enter Mobile Number'))
            if uno not in phone_no:
                un=input("Enter User Name : ")
                up=input("Enter The Password : ")
                user_name.append(un)
                user_aadhar.append(ua)
                pass_word.append(up) 
                phone_no.append(uno)
                print("Signed-in Successfully!!!")
            else:
                print('Phone Number Already Exist')
        else:
            print("User Already Exist")
    elif(ch==2):
        un=input("Enter User Name : ")
        up=input("Enter Password : ")
        if user_name.index(un)==pass_word.index(up):
            price_data = {
                "area": {
                    "ANDRAL": 100000,
                    "GANDHI-NAGAR": 150000,
                    "TALUR-ROAD": 200000,
                    "MG-ROAD": 250000,
                    "VIDYA-NAGAR": 300000
                },
                "house_type": {
                    "Duplex": 1.5,
                    "Apartment": 1.2,
                    "Individual House": 1.8
                },
                "bedroom_multiplier": 50000
            }
            print("Available Areas:")
            for area in price_data['area']:
                print(area)
            selected_area = input("Select an area: ")
            selected_area=selected_area.upper()
            print("\nAvailable House Types:")
            for house_type in price_data['house_type']:
                print(house_type)
            selected_house_type = input("Select a house type: ")
            selected_house_type=selected_house_type.upper()
            num_bedrooms = int(input("Enter the number of bedrooms b/w(1-4): "))
            base_price = price_data['area'].get(selected_area, 0)
            multiplier = price_data['house_type'].get(selected_house_type, 1)
            total_price = base_price * multiplier + num_bedrooms * price_data['bedroom_multiplier']
            total_price_inr = total_price * 74.25  # Conversion rate from USD to INR
            print("\nPredicted House Price: ₹{:,.2f}".format(total_price_inr))
    elif(ch==3):
        ua=int(input("Enter User Aadhar Number"))
        print(user_aadhar.index(ua))
        uno=int(input("Enter User Registered Phone Number : "))
        if user_aadhar.index(ua)==phone_no.index(uno):
            up=input("Enter The New Password")
            pass_word[user_aadhar.index(ua)]=up
            print('Password Changed Successfully!!!')
        else:
            print('Wrong Details.....')
    elif(ch==4):
        break
    else:
        print('Invalid Choice')

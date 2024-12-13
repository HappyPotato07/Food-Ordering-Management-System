#WONG BIN JIE
#TP060875
#TAI RUI XIAN
#TP060922

import time
# Display main page when access system
def main_menu():
    print("\n--------------------ONLINE FOOD ORDERING MANAGEMENT SYSTEM-----------------")
    print("------------------WELCOME TO SPIDERMAN ONLINE FOOD SERVICES----------------")
    print("---------------------------------------------------------------------------")
    print("---------------------------------MAIN PAGE---------------------------------")
    print("(1) View as Guest\n(2) Login as Customer\n(3) Login as Admin\n(4) Exit\n")
    choice = str(input("Please Enter A Number To Proceed: "))
    if choice == "1":
        print("\nRedirecting To Guest Page...")
        time.sleep(1)
        guest_main_page()
    elif choice == "2":
        print("\nRedirecting To Registered Customer Page...")
        time.sleep(1)
        def_login()
    elif choice == "3":
        print("\nRedirecting To Admin Page...\n")
        time.sleep(1)
        admin_login()
    elif choice == "4":
        print("\n\t\t\t\t\t\t\t\t  EXITING...\n\t\t\t\t  >>>Thank You For Using The System>>>")
        exit()
    else:
        print("\nInvalid Input! Please Try Again")
        main_menu()
# Display main page of guest
def guest_main_page():
    print("\n-------------------------------GUEST MAIN PAGE-----------------------------\n(1) View Menu\n(2) Sign Up as Customer\n(3) Back\n")
    option = str(input("Please Enter An Option To Proceed: "))
    if option == "1":
        print("\n------------------------------------MENU-----------------------------------")
        def_menu()
        print("\n(1) Back\n")
        while True:
            option = str(input("Please Enter An Option: "))
            if option == "1":
                guest_main_page()
            else:
                print("\nInvalid Input! Please Try Again")
    elif option == "2":
        print("Do You Want To Register An Account?")
        option = str(input("y = Yes  n = No "))
        if option == "y" or option == "Y":
            addnew()
        else:
            guest_main_page()
    elif option == "3":
        main_menu()
    else:
        print("\nInvalid Input! Please Try Again")
        guest_main_page()
# Display menu
def def_menu():
    print("\n\n                             R O T I  C A N A I                          \n")
    with open("roticanai.txt","r") as file:
        for i in file.readlines():
            data = i.split(",")
            code = data[0]
            name = data[1]
            price = data[2]
            print("\t\t{0:10s} {1:42s} RM {2:10s}".format(code, name, price.strip()))
    print("=============================================================================")
    print("                               M U R T A B A K                       ")
    with open("murtabak.txt","r") as file:
        for item in file.readlines():
            data = item.split(",")
            code = data[0]
            name = data[1]
            price = data[2]
            print("\t\t{0:10s} {1:42s} RM {2:10s}".format(code, name, price.strip()))
    print("=============================================================================")
    print("                             N A S I  G O R E N G                      ")
    with open("nasigoreng.txt","r") as file:
        for item in file.readlines():
            data = item.split(",")
            code = data[0]
            name = data[1]
            price = data[2]
            print("\t\t{0:10s} {1:42s} RM {2:10s}".format(code, name, price.strip()))
    print("=============================================================================")
    print("                                    M E E                            ")
    with open("mee.txt", "r") as file:
        for item in file.readlines():
            data = item.split(",")
            code = data[0]
            name = data[1]
            price = data[2]
            print("\t\t{0:10s} {1:42s} RM {2:10s}".format(code, name, price.strip()))
    print("=============================================================================")
    print("                                 M I N U M A N                         ")
    with open("mee.txt", "r") as file:
        for item in file.readlines():
            data = item.split(",")
            code = data[0]
            name = data[1]
            price = data[2]
            print("\t\t{0:10s} {1:42s} RM {2:10s}".format(code, name, price.strip()))
    print("=============================================================================")

# Guest sign up page
def addnew():
    print("\n-----------------------------------SIGN UP---------------------------------")
    filename_cd = "customer_detail.txt"
    file_cd = open(filename_cd, "a")
    filename_cdl = "customer_detail_log.txt"
    file_cdl = open(filename_cdl, "a")
    customer_name = str(input("Please Enter Your Name: "))
    file_cdl.write(customer_name.upper() + "; ")

    length_u = False
    while not length_u:
        guest_username = str(input("Please Enter Username: "))
        if len(guest_username) >= 3:
            file_cd.write(guest_username + "," )
            file_cdl.write(guest_username + "; ")
            break
        else:
            length_u = False
            print("Username Must At Least 3 Letters. Please Try Again.")

    password = False
    while not password:
        new_password = str(input("Please Enter Password: "))
        new_password1 = str(input("Please Confirm Your Password: "))
        if len(new_password) >= 5 and new_password == new_password1:
            password = True
            file_cd.write(new_password + ",")
            file_cd.write(new_password1 + "\n")
            break
        if len(new_password) >= 5 and new_password != new_password1:
            print("Password Unmatch! Please Try Again.")
        else:
            print("Password Must Contains At Least 5 Numbers. Please Try Again.")

    customer_telephone = str(input("Please Enter Your Contact Number: "))
    file_cdl.write(customer_telephone + "; ")
    customer_address = str(input("Please Enter Your Address: "))
    file_cdl.write(customer_address.upper() + "\n")
    file_cd.close()
    file_cdl.close()
    print("\nSign Up successful! Welcome", guest_username.upper())
    while True:
        user_input = str(input("Enter '1' To Re-Login; '2' To Exit\n"))
        if user_input == "1":
            def_login()
        elif user_input == "2":
            print("\n\t\t\t\t\t\t\t\t\t\tEXITING...\n\t\t\t\t\t\t>>>Thank You For Using The System>>>")
            break
        else:
            print("Invalid Input! Please Try Again\n")

# Customer login page
def def_login():
    print("\n------------------------------------LOG IN----------------------------------")
    with open("customer_detail.txt", "r") as login:
        username_list = []
        password_list = []
        password_1_list = []
        for line in login.readlines():
            data = line.split(",")
            s_username = data[0]
            s_password = data[1]
            s_password_c = data[2]
            username_list.append(s_username)
            password_list.append(s_password)
            password_1_list.append(s_password_c)
        username = str(input("Please Enter Username: "))
        password = str(input("Please Enter Password: "))
        password1 = str(input("Please Confirm Your Password: "))
        if password in password_list and password1 == password and username in username_list:
            if username_list.append(username) == password_list.append(password) == password_1_list.append(password1):
                print("\nLogin Successful! Welcome", username.upper(), "\n")
                customer_main_page()
        else:
            print("\nInvalid Username Or Password. Please Try Again ")
            def_login()

# Display customer main page
def customer_main_page():
    print("\n------------------------------CUSTOMER MAIN PAGE---------------------------")
    print("(1) View Food Category\n(2) View Food Item\n(3) Add to Cart & Order\n(4) Back\n(5) Exit\n")
    user_input = str(input("Please Enter An Option To Proceed: "))
    if user_input == "1":
        def_foodcategory()
    elif user_input == "2":
        print("\n------------------------------------MENU-------------------------------------")
        def_menu()
        print("\n(1) Back\n(2) Order\n")
        while True:
            user_input = str(input("Please Select An Option To Proceed: "))
            if user_input == "1":
                customer_main_page()
            elif user_input == "2":
                user_input = str(input("Do You Want To Proceed Order?\ny = yes  n = no "))
                if user_input == "y" or user_input == "Y":
                    cust_order_payment()
                    break
                else:
                    def_menu()
                    print("\n(1) Back\n(2) Order\n")
            else:
                print("\nInvalid Input! Please Try Again")
    elif user_input == "3":
        cust_order_payment()
    elif user_input == "4":
        main_menu()
    elif user_input == "5":
        print("\n\t\t\t\t\t\t\t\t\t\tEXITING...\n\t\t\t\t\t\t>>>Thank You For Using The System>>>")
        exit()
    else:
        print("Invalid Input! Please Try Again")
        customer_main_page()

# Categorize food
def def_foodcategory():
    print("\n--------------------------------FOOD  CATEGORY-----------------------------")
    print("(1) ROTI CANAI\n(2) MURTABAK\n(3) NASI GORENG\n(4) MEE\n(5) MINUMAN\n\n(6) Back to Main Page")
    choice = input("\nPlease Select An Option To Proceed: ")
    if choice == "1":
        print("\n\t\t\t\tRoti Canai Menu")
        print("\t\t", "=" * 45)
        with open("roticanai.txt", "r") as file:
            for item in file:
                data = item.split(',')
                code = data[0]
                name = data[1]
                price = data[2]
                print("\t\t  {0:6s} {1:25s} RM {2:10s}".format(code, name, price.strip()))
            while True:
                back = str(input("\nBack To Previous Page\nPress B: "))
                if back == "b" or back == "B":
                    def_foodcategory()
                else:
                    print("\nInvalid Input! Please Try Again")
    elif choice == "2":
        print("\n\t\t\t\t  Murtabak Menu")
        print("\t\t", "=" * 45)
        with open("murtabak.txt", "r") as file:
            for item in file:
                data = item.split(",")
                code = data[0]
                name = data[1]
                price = data[2]
                print("\t\t  {0:6s} {1:25s} RM {2:10s}".format(code, name, price.strip()))
            while True:
                back = str(input("\nBack To Previous Page\nPress B: "))
                if back == "b" or back == "B":
                    def_foodcategory()
                else:
                    print("\nInvalid Input! Please Try Again")
    elif choice == "3":
        print("\n\t\t\t\t Nasi Goreng Menu")
        print("\t\t", "=" * 45)
        with open("nasigoreng.txt", "r") as file:
            for item in file:
                data = item.split(",")
                code = data[0]
                name = data[1]
                price = data[2]
                print("\t\t  {0:6s} {1:25s} RM {2:10s}".format(code, name, price.strip()))
            while True:
                back = str(input("\nBack To Previous Page\nPress B: "))
                if back == "b" or back == "B":
                    def_foodcategory()
                else:
                    print("\nInvalid Input! Please Try Again")
    elif choice == "4":
        print("\n\t\t\t\t\   Mee Menu")
        print("\t\t", "=" * 45)
        with open("mee.txt", "r") as file:
            for item in file:
                data = item.split(",")
                code = data[0]
                name = data[1]
                price = data[2]
                print("\t\t  {0:6s} {1:25s} RM {2:10s}".format(code, name, price.strip()))
            while True:
                back = str(input("\nBack To Previous Page\nPress B: "))
                if back == "b" or back == "B":
                    def_foodcategory()
                else:
                    print("\nInvalid Input! Please Try Again")
    elif choice == "5":
        print("\n\t\t\t\tMinuman Menu")
        print("\t\t", "=" * 45)
        with open("minuman.txt", "r") as file:
            for item in file:
                data = item.split(",")
                code = data[0]
                name = data[1]
                price = data[2]
                print("\t\t  {0:6s} {1:25s} RM {2:10s}".format(code, name, price.strip()))
            while True:
                back = str(input("\nBack To Previous Page\nPress B: "))
                if back == "b" or back == "B":
                    def_foodcategory()
                else:
                    print("\nInvalid Input! Please Try Again")
    elif choice == "6":
        customer_main_page()
    else:
        print("\nInvalid Input! Please Try Again\n")
        def_foodcategory()


def get_next_id():
    with open("id.txt", "r") as fh:
        rec = fh.read().split()
        nxtid = rec[0]
        tmp = str(int(nxtid[3:]) + 1)
        if len(tmp) == 1:
            nxtid = "ORD" + "000" + tmp
        elif len(tmp) == 2:
            nxtid = "ORD" + "00" + tmp
        elif len(tmp) == 3:
            nxtid = "ORD" + "0" + tmp
        elif len(tmp) == 4:
            nxtid = "ORD" + tmp
    with open("id.txt","w") as fh:
        fh.write(nxtid)
    return nxtid
# Display customer order page
def cust_order_payment():
    with open("customer_detail.txt", "r") as order_record_file:
        username = []
        for line in order_record_file.readlines():
            data = line.split(",")
            s_name = data[0]
            username.append(s_name)
        username1 = str(input("Please Re-Enter Username Before Proceed Order: "))
        if username1 in username:
            from time import ctime
            with open("customer_order_records.txt", "a") as f:
                f.write(get_next_id() + "," + username1.upper() + "," + ctime() + ",")

            current_cart = []
            cart_count = 1
            new_cart = "yes"
            roticanailist = []
            murtabaklist = []
            nasigorenglist = []
            meelist = []
            minumanlist = []

            while new_cart == "y" or new_cart == "yes" or new_cart == "Y":
                while True:
                    with open("order_page.txt", "r") as order_page_file:
                        read_file = order_page_file.read()
                        print("Ms/Mr", username1.upper(), ",Welcome to Order Page")
                        print(read_file)
                    option = input("\nPlease Select An Option To Proceed: ")
                    if option == "1":
                        with open("roticanai.txt") as order_record_file:
                            for line in order_record_file:
                                roticanailist.append([(line.split(",")[0]), (line.split(",")[1]),float(line.split(",")[2].strip(" ").strip("\n"))])
                        while True:
                            opt = item_menu("Roti Canai", roticanailist)
                            choice = []
                            for i in range(0, len(roticanailist)):
                                choice.append(str(i + 1))
                            if opt in (number(roticanailist)):
                                ask = str(input("Add " + roticanailist[int(opt) - 1][1] + " To The Cart? (y/n): "))
                                if ask == "y":
                                    current_cart.append([roticanailist[int(opt) - 1][1], roticanailist[int(opt) - 1][2]])
                                    print("\nNote*", roticanailist[int(opt) - 1][1], "Successfully Added Into Cart")
                                    input("\nHit ENTER To Continue\n")
                            elif opt == "b" or opt == "B":
                                with open("order_page.txt", "r") as order_page_file:
                                    read_file = order_page_file.read()
                                    print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                                    print(read_file)
                                    break
                            else:
                                input("\nInvalid Input! Hit 'ENTER' To Try Again")
                    elif option == "2":
                        with open("murtabak.txt") as order_record_file:
                            for line in order_record_file:
                                murtabaklist.append([(line.split(",")[0]), (line.split(",")[1]),
                                                     float(line.split(",")[2].strip(" ").strip("\n"))])
                        while True:
                            opt = item_menu("Murtabak", murtabaklist)
                            choice = []
                            for i in range(0, len(murtabaklist)):
                                choice.append(str(i + 1))
                            if opt in (number(murtabaklist)):
                                ask = str(input("Add " + murtabaklist[int(opt) - 1][1] + " To The Cart? (y/n): "))
                                if ask == "y":
                                    current_cart.append([murtabaklist[int(opt) - 1][1], murtabaklist[int(opt) - 1][2]])
                                    print("\nNote*", murtabaklist[int(opt) - 1][1], "Successfully Added Into Cart")
                                    input("\nHit ENTER To Continue\n")
                            elif opt == "b" or opt == "B":
                                with open("order_page.txt", "r") as order_page_file:
                                    read_file = order_page_file.read()
                                    print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                                    print(read_file)
                                    break
                            else:
                                input("\nInvalid Input! Hit 'ENTER' To Try Again")
                    elif option == "3":
                        with open("nasigoreng.txt") as order_record_file:
                            for line in order_record_file:
                                nasigorenglist.append([(line.split(",")[0]), (line.split(",")[1]),
                                                       float(line.split(",")[2].strip(" ").strip("\n"))])
                        while True:
                            opt = item_menu("Nasi Goreng", nasigorenglist)
                            choice = []
                            for i in range(0, len(nasigorenglist)):
                                choice.append(str(i + 1))
                            if opt in (number(nasigorenglist)):
                                ask = str(input("Add " + nasigorenglist[int(opt) - 1][1] + " to the Cart? (y/n): "))
                                if ask == "y":
                                    current_cart.append(
                                        [nasigorenglist[int(opt) - 1][1], nasigorenglist[int(opt) - 1][2]])
                                    print("\nNote*", nasigorenglist[int(opt) - 1][1], "Successfully Added Into Cart")
                                    input("\nHit ENTER To Continue\n")
                            elif opt == "b" or opt == "B":
                                with open("order_page.txt", "r") as order_page_file:
                                    read_file = order_page_file.read()
                                    print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                                    print(read_file)
                                    break
                            else:
                                input("\nInvalid Input! Hit 'ENTER' To Try Again")
                    elif option == "4":
                        with open("mee.txt") as order_record_file:
                            for line in order_record_file:
                                meelist.append([(line.split(",")[0]), (line.split(",")[1]),
                                                float(line.split(",")[2].strip(" ").strip("\n"))])
                        while True:
                            opt = item_menu("Mee", meelist)
                            choice = []
                            for i in range(0, len(meelist)):
                                choice.append(str(i + 1))
                            if opt in (number(meelist)):
                                ask = str(input("Add " + meelist[int(opt) - 1][1] + " To The Cart? (y/n): "))
                                if ask == "y":
                                    current_cart.append([meelist[int(opt) - 1][1], meelist[int(opt) - 1][2]])
                                    print("\nNote*", meelist[int(opt) - 1][1], "Successfully Added Into Cart")
                                    input("\nHit ENTER To Continue\n")
                            elif opt == "b" or opt == "B":
                                with open("order_page.txt", "r") as order_page_file:
                                    read_file = order_page_file.read()
                                    print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                                    print(read_file)
                                break
                            else:
                                input("\nInvalid Input! Hit 'ENTER' To Try Again")
                    elif option == "5":
                        with open("minuman.txt") as order_record_file:
                            for line in order_record_file:
                                minumanlist.append([(line.split(",")[0]), (line.split(",")[1]),
                                                    float(line.split(",")[2].strip(" ").strip("\n"))])
                        while True:
                            opt = item_menu("Minuman", minumanlist)
                            choice = []
                            for i in range(0, len(minumanlist)):
                                choice.append(str(i + 1))
                            if opt in (number(minumanlist)):
                                ask = str(input("Add " + minumanlist[int(opt) - 1][1] + " to the Cart? (y/n): "))
                                if ask == "y":
                                    current_cart.append(
                                        [minumanlist[int(opt) - 1][1], minumanlist[int(opt) - 1][2]])
                                    print("\nNote*", minumanlist[int(opt) - 1][1], "Successfully Added Into Cart")
                                    input("\nHit ENTER To Continue\n")
                            elif opt == "b" or opt == "B":
                                with open("order_page.txt", "r") as order_page_file:
                                    read_file = order_page_file.read()
                                    print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                                    print(read_file)
                                    break
                            else:
                                input("\nInvalid Input! Hit 'ENTER' To Try Again")
                    elif option == "v" or option == "V":
                        from time import ctime
                        print("\n\t\t\t\t" + ctime())
                        print("\t\t\t\tContents of Cart\n")
                        print("\t\t\t\t {0:31s} {1:4s}".format("Item Description", "Price"))
                        print("\t\t\t\t==================\t\t=======")
                        for n in current_cart:
                            print("\t\t\t\t{0:20s}\t\tRM{1:5.2f}".format(n[0], n[1]))
                        input("\nHit ENTER To Continue")
                        with open("order_page.txt", "r") as order_page_file:
                            read_file = order_page_file.read()
                            print("\n\nMs/Mr", username1.upper(), ",Welcome to Order Page")
                            print(read_file)
                    elif option == "c" or option == "C":
                        from time import ctime
                        print("\n\t\t\t" + ctime())
                        print("\t\t\tSummary of shopping cart:\n")
                        print("\t\t\t  Items\t\t\t\t     Price")
                        print("\t\t\t================\t\t    =========")
                        for i in current_cart:
                            print("\t\t\t{0:20s}\t\t     RM {1:4.2f}".format(i[0], i[1]))
                        total_cost = 0
                        for i in range(len(current_cart)):
                            total_cost += current_cart[i][1]
                        print("\n\t\t\tTotal:{0:2} Items\t\tTotal Price: RM {1:4.2f}".format(len(current_cart), total_cost))
                        break
                    elif option == "b" or option == "B":
                        customer_main_page()
                    else:
                        print("\nInvalid Input! Please Try Again")


                newcart = str(input("\nDo You Want To Proceed? (y|n)\ny = Proceed To Payment\nn = Cancel Order\n"))
                if newcart == 'no' or newcart == "n" or newcart == "N":
                    new_cart = 'yes'
                    current_cart = []
                    cart_count += 1
                elif newcart == "yes" or newcart == "y" or newcart == "Y":
                    new_cart = True
                    order = open("temp_order_records.txt", "w")
                    for data in current_cart:
                        order.write(",".join(map(str, data)))
                        order.write("\n")
                    order.close()
                    f1 = open("temp_order_records.txt", "r")
                    for line in f1:
                        data = line.split(",")
                        name = data[0]
                        price = data[1]
                        f2 = open("customer_order_records.txt", "a")
                        f2.write(name + ";" + price.strip() + "\t")
                    f2.write("," + str(len(current_cart)) + "," + str(total_cost) + ",")
                    f1.close()
                    f2.close()
                    print("\t\t\t\t    Please Hold On\n\t\t\t   >>>Redirecting To Payment Page>>>\n\n")
                    time.sleep(1)
                    print("\t\t", "=" * 49, "\n\t\t\t\t P a y m e n t  P a g e", "\n\t\t", "=" * 49)
                    print("\n\t\t\t(1) Debit/Credit Card\n\t\t\t(2) Touch n Go\n\t\t\t(3) Back")

                    option = str(input("\n\n\t\t Please Select Your Payment Option: "))
                    if option == "1":
                        with open("customer_order_records.txt", "a") as order_record_file:
                            order_record_file.write("Debit/Credit Card," + "\n")
                        while True:
                            card_det = str(input("\t\t Please Enter Credit/Debit Card Number: "))
                            if len(card_det) == 16:
                                confirmation = str(input("\t\t Please Enter Card Number Again: "))
                                if confirmation == card_det:
                                    holdername = str(input("\t\t Please Enter Card Holder Name: "))
                                    type_c = str(input("\t\t Please Enter Card Type (Visa/Mastercard): "))
                                    expiry_date = str(input("\t\t Please Enter the Card Expiry Date (MM/YY): "))
                                    cvc = str(input("\t\t Please Enter your Card's CVC number(xxx): "))
                                    print("\t\t", "=" * 49,
                                          "\n\t\t\t\t    Please Hold On...\n\t\t\t >>>Your Details Is Being Processed>>>\n\n")
                                    time.sleep(2)
                                    print(f"\t\t Card Number: {card_det}")
                                    print(f"\t\t Name of Card Holder: Mr/Mrs {holdername.upper()}")
                                    print(f"\t\t Card Type: {type_c}")
                                    print(f"\t\t Card Expiry Date: {expiry_date}")
                                    print(f"\t\t Card's CVC number: {cvc}")
                                    print("\t\t Total Of your Order: RM {:.2f}".format(total_cost))
                                    confirmation = str(input("\n\t\t Press Y To Confirm Payment: "))
                                    if confirmation == "y" or "Y":
                                        print(
                                            "\n\t\t\t\t    Please Hold On...\n\t\t\t >>>Payment Is Being Proccessed>>>")
                                        time.sleep(2)
                                        print("")
                                        print("\n\t\t >>>Your Payment Has Been Successfully Received!>>>"
                                              "\n\t     >>>Thank You For Using Spiderman Online Food Services>>>"
                                              "\n\t\t>>>Your Order will Be Delivered As Soon As Possible!>>>"
                                              "\n\t\t\t\t>>>Have A Nice Day>>>")
                                        time.sleep(5)
                                        break
                                    else:
                                        print("Order Has Been Cancelled\nRedirecting Back To Main Page")
                                        time.sleep(1)
                                        main_menu()
                                else:
                                    print("\t\t Please Try Again, Card Credentials Does Not Match!")
                            else:
                                print("\t\t Error!\n\t\t Card Number Must Be 16 Digits!")

                    elif option == "2":
                        print("\n\t\t\t\t    Please Hold On\n\t\t\t   >>>Redirecting to TNG e-wallet>>>\n")
                        time.sleep(1)
                        with open("customer_order_records.txt", "a") as order_record_file:
                            order_record_file.write("TnG E-Wallet," + "\n")
                        while True:
                            password = str(input("\t\t Please Enter Pin Number: "))
                            if len(password) == 6:
                                password1 = str(input("\t\t Please Confirm Your Pin: "))
                                if password1 == password:
                                    amount_pay = str(input("\t\t Please Enter Amount Paid: "))
                                    balance = float(amount_pay) - float(str(total_cost))
                                    print("\n\t\t Change Due: RM {:.2f}".format(balance))
                                    print("\n\t\t\t >>>Your Payment Has Been Successfully Received!>>>"
                                          "\n\t\t    >>>Thank You For Using Spiderman Online Food Services>>>"
                                          "\n\t\t\t>>>Your Order will Be Delivered As Soon As Possible!>>>"
                                          "\n\t\t\t\t\t>>>Have A Nice Day>>>")
                                    time.sleep(5)
                                    break
                                else:
                                    print("\t\t Please Try Again, Pin Number Does Not Match!")
                            else:
                                print("\t\t Please Try Again, Pin Number Must Contains 6 Digits!")
                    else:
                        print("Order Has Been Cancelled\nRedirecting To Main Page...")
                        customer_main_page()
                else:
                    print("Invalid Input! Please Try Again")
        else:
            print("No Such Username! Please Try Again")
            customer_main_page()

def item_menu(category, item_list):
    print("\n" + category + "\tMenu")
    print("\t\tSelect From The Following Items, Display Cart Or Checkout: ")
    print("\n\t\t\t    No\t       Item Description\t\t   Price")
    print("\t\t\t   =====   ==========================\t ==========")
    for n in range(0, len(item_list)):
        print("\t\t\t    {0:>2s}   ~ {1:28s}   RM{2:6.2f}".format(str(n + 1), item_list[n][1],item_list[n][2]))
    print("\n\t\t\t     b   ~ Return To Category Menu")
    option = str(input("\n\nEnter Selection (1 to " + str(n + 1) + " or 'b'): ".format(str(len(item_list)))))
    return option

# Show types of food in each category by listing 1..2..3..
def number(item_list):
    choice_num = []
    for n in range(0, len(item_list)):
        choice_num.append(str(n + 1))
    return choice_num

# Display admin login page
def admin_login():
    print("--------------------------------- ADMIN LOGIN -------------------------------")
    with open("admin_list.txt", "r") as adm:
        admin_username_list = []
        admin_password_list = []
        for line in adm.readlines():
            data = line.split(';')
            username = data[0]
            password = data[1]
            admin_username_list.append(username)
            admin_password_list.append(password)
        admin_username = str(input("Please Enter Your Username: "))
        admin_password = str(input("Please Enter Your Password: "))
        if admin_username in admin_username_list and admin_password in admin_password_list:
            if admin_username_list.index(admin_username) == admin_password_list.index(admin_password):
                print("\nSuccessfully Logged In!")
                print("Welcome,", admin_username.upper(), "\n")
                def_admin_main()
            else:
                print("\n***Invalid Admin Username Or Password! Please Try Again ***")
                back = str(input("\nTry Again = 1 Exit = 2"))
                if back == "1":
                    admin_login()
                elif back == "2":
                    print("\nHave A Nice Day!")
                else:
                    print("\n*Invalid Answer* Existing...")
        else:
            print("\nAdmin Username Is Not Exist Or Invalid Password! Please Try Again")
            admin_login()

# Display admin main page
def def_admin_main():
    print("-------------------------------ADMIN MAIN PAGE-----------------------------")
    print("Choose an option:\n(1) Add Food Item\n(2) Modify Food Item\n(3) Display Records\n(4) Search Order or Payment\n(5) Logout\n")
    admin_input = str(input("\nEnter Option 1-5: "))
    if admin_input == "1":
        additem()
    elif admin_input == "2":
        modifyitem()
    elif admin_input == "3":
        display_records()
    elif admin_input == "4":
        search_order_payment()
    elif admin_input == "5":
        print("\n\t\t\t\t\t\t\t\t    Logging Out......\n\t\t\t\t\t\t>>>Thank You For Using The System!>>>\n\n")
        time.sleep(5)
        exit()
    else:
        print("Invalid Answer! Please Try Again")
        def_admin_main()

# Function of add item
def additem():
    print("\n*** ADD FOOD ITEM ***\n\n(1) ADD ROTI CANAI\n(2) ADD MURTABAK\n(3) ADD NASI GORENG\n(4) ADD MEE\n(5) ADD MINUMAN\n(6) Back")
    user_input = str(input("\nChoose Category 1-6: "))
    print('\n')
    if user_input == "1":
        with open("roticanai.txt","r") as file:
            for line in file:
                print(line, end="")
            add_roti_canai()
    elif user_input == "2":
        with open("murtabak.txt","r") as file:
            for line in file:
                print(line, end="")
            add_murtabak()
    elif user_input == "3":
        with open("nasigoreng.txt","r") as file:
            for line in file:
                print(line, end="")
            add_nasi_goreng()
    elif user_input == "4":
        with open("mee.txt","r") as file:
            for line in file:
                print(line, end="")
            add_mee()
    elif user_input == "5":
        with open("minuman.txt","r") as file:
            for line in file:
                print(line, end="")
            add_minuman()
    elif user_input == "6":
        def_admin_main()
    else:
        print("***Invalid Category! Please Try Again***")
        additem()

# Add roti canai into menu
def add_roti_canai():
    print("\n*- Adding Roti Canai Menu -*\n")
    with open("roticanai.txt", "r") as file:
        code_list = []
        name_list = []
        for line in file.readlines():
            data = line.split(",")
            f_code = data[0]
            f_name = data[1]
            code_list.append(f_code)
            name_list.append(f_name)
        while True:
            code = str(input("Add New Item Code: "))
            if code.upper() in code_list:
                print("Item Code Existed! Please Insert New Code ")
            else:
                name = str(input("Add New Item Name: "))
                if name.upper() in name_list:
                    print("Item Name Existed! Please Insert New Name ")
                else:
                    price = str(input("Add New Item Price: "))
                    with open("roticanai.txt", "a") as file:
                        file.write(code.upper() + "," + name.upper() + "," + price + "\n")
                        break
    print(code, name, price, "\n\nSuccessfully Added Into Menu!")
    while True:
        user_input = str(input("(c)Continue Add Item (b) Back Home: \n"))
        if user_input == "c" or user_input == "C":
            add_roti_canai()
        elif user_input == "b" or user_input == "B":
            additem()
        else:
            print("***Invalid Input! Please Try Again: ")

# Add murtabak in menu
def add_murtabak():
    print("\n*- Adding Murtabak Menu -*\n")
    with open("murtabak.txt", "r") as file:
        code_list = []
        name_list = []
        for line in file.readlines():
            data = line.split(",")
            f_code = data[0]
            f_name = data[1]
            code_list.append(f_code)
            name_list.append(f_name)
        while True:
            code = str(input("Add New Item Code: "))
            if code.upper() in code_list:
                print("Item Code Existed! Please Insert New Code ")
            else:
                name = str(input("Add New Item Name: "))
                if name.upper() in name_list:
                    print("Item Name Existed! Please Insert New Name ")
                else:
                    price = str(input("Add New Item Price: "))
                    with open("murtabak.txt", "a") as file:
                        file.write(code.upper() + "," + name.upper() + "," + price + "\n")
                        break
    print(code, name, price, "\n\nSuccessfully Added Into Menu!")
    while True:
        user_input = str(input("(c)Continue Add Item (b) Back Home: \n"))
        if user_input == "c" or user_input == "C":
            add_murtabak()
        elif user_input == "b" or user_input == "B":
            additem()
        else:
            print("***Invalid Input! Please Try Again: ")

# Add nasi goreng in menu
def add_nasi_goreng():
    print("\n*- Adding Nasi Goreng Menu -*\n")
    with open("nasigoreng.txt", "r") as file:
        code_list = []
        name_list = []
        for line in file.readlines():
            data = line.split(",")
            f_code = data[0]
            f_name = data[1]
            code_list.append(f_code)
            name_list.append(f_name)
        while True:
            code = str(input("Add New Item Code: "))
            if code.upper() in code_list:
                print("Item Code Existed! Please Insert New Code ")
            else:
                name = str(input("Add New Item Name: "))
                if name.upper() in name_list:
                    print("Item Name Existed! Please Insert New Name ")
                else:
                    price = str(input("Add New Item Price: "))
                    with open("nasigoreng.txt", "a") as file:
                        file.write(code.upper() + "," + name.upper() + "," + price + "\n")
                        break
    print(code, name, price, "\n\nSuccessfully Added Into Menu!")
    while True:
        user_input = str(input("(c)Continue Add Item (b) Back Home: \n"))
        if user_input == "c" or user_input == "C":
            add_nasi_goreng()
        elif user_input == "b" or user_input == "B":
            additem()
        else:
            print("***Invalid Input! Please Try Again: ")

# Add mee in menu
def add_mee():
    print("\n*- Adding Mee Menu -*\n")
    with open("mee.txt", "r") as file:
        code_list = []
        name_list = []
        for line in file.readlines():
            data = line.split(",")
            f_code = data[0]
            f_name = data[1]
            code_list.append(f_code)
            name_list.append(f_name)
        while True:
            code = str(input("Add New Item Code: "))
            if code.upper() in code_list:
                print("Item Code Existed! Please Insert New Code ")
            else:
                name = str(input("Add New Item Name: "))
                if name.upper() in name_list:
                    print("Item Name Existed! Please Insert New Name ")
                else:
                    price = str(input("Add New Item Price: "))
                    with open("mee.txt", "a") as file:
                        file.write(code.upper() + "," + name.upper() + "," + price + "\n")
                        break
    print(code, name, price, "\n\nSuccessfully Added Into Menu!")
    while True:
        user_input = str(input("(c)Continue Add Item (b) Back Home: \n"))
        if user_input == "c" or user_input == "C":
            add_minuman()
        elif user_input == "b" or user_input == "B":
            additem()
        else:
            print("***Invalid Input! Please Try Again: ")

# Add minuman in menu
def add_minuman():
    print("\n*- Adding Minuman Menu -*\n")
    with open("minuman.txt", "r") as file:
        code_list = []
        name_list = []
        for line in file.readlines():
            data = line.split(",")
            f_code = data[0]
            f_name = data[1]
            code_list.append(f_code)
            name_list.append(f_name)
        while True:
            code = str(input("Add New Item Code: "))
            if code.upper() in code_list:
                print("Item Code Existed! Please Insert New Code ")
            else:
                name = str(input("Add New Item Name: "))
                if name.upper() in name_list:
                    print("Item Name Existed! Please Insert New Name ")
                else:
                    price = str(input("Add New Item Price: "))
                    with open("minuman.txt", "a") as file:
                        file.write(code.upper() + "," + name.upper() + "," + price + "\n")
                        break
    print(code, name, price, "\n\nSuccessfully Added Into Menu!")
    while True:
        user_input = str(input("(c)Continue Add Item (b) Back Home: \n"))
        if user_input == "c" or user_input == "C":
            add_minuman()
        elif user_input == "b" or user_input == "B":
            additem()
        else:
            print("***Invalid Input! Please Try Again: ")

#Modify or remove item
def modifyitem():
    print("\n***** MODIFY FOOD ITEM *****\n\n(1) MODIFY ROTI CANAI\n(2) MODIFY MURTABAK\n(3) MODIFY NASI GORENG\n(4) MODIFY MEE\n(5) MODIFY MINUMAN\n(6) Back")
    user_input = str(input('\n\nChoose Category 1-6: \n'))
    if user_input == "1":
        option = str(input("(1) Modify Item   (2) Remove Item\nPlease choose a category to proceed: \n"))
        if option == "1":
            with open("roticanai.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_roti_canai()
        elif option == "2":
            with open("roticanai.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_remove_roti_canai()
        else:
            print("Invalid Option")
            modifyitem()
    elif user_input == "2":
        option = str(input("(1) Modify Item   (2) Remove Item \n Please choose a category to proceed: "))
        if option == "1":
            with open("murtabak.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_murtabak()
        elif option == "2":
            with open("murtabak.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_remove_murtabak()
        else:
            print("Invalid Option")
            modifyitem()
    elif user_input == "3":
        option = str(input("(1) Modify Item   (2) Remove Item \n Please choose a category to proceed: "))
        if option == "1":
            with open("nasigoreng.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_nasi_goreng()
        elif option == "2":
            with open("nasigoreng.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_remove_nasi_goreng()
        else:
            print("Invalid Option")
            modifyitem()
    elif user_input == "4":
        option = str(input("(1) Modify Item   (2) Remove Item \n Please choose a category to proceed: "))
        if option == "1":
            with open("mee.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_mee()
        elif option == "2":
            with open("mee.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_remove_mee()
        else:
            print("Invalid Option")
            modifyitem()
    elif user_input == "5":
        option = str(input("(1) Modify Item   (2) Remove Item \n Please choose a category to proceed: \n"))
        if option == "1":
            with open("minuman.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_minuman()
        elif option == "2":
            with open("minuman.txt","r") as file:
                for line in file:
                    print(line, end="")
                modify_remove_minuman()
        else:
            print("Invalid Option")
            modifyitem()
    elif user_input == "6":
        def_admin_main()
    else:
        print('Invalid Category, Please try again!')
        modifyitem()

def modify_roti_canai():
    print("\n*-- Modify Roti Canai Menu --*\n")
    with open("roticanai.txt","r") as file:
        old_code = str(input("Enter a Item Code for Modifying (e.g. RC01): ").upper())
        temp_list = []
        temp_name = []
        for line in file.readlines():
            data = line.split(",")
            code = data[0]
            name = data[1]
            temp_list.append(code)
            temp_name.append(name)
        if old_code in temp_list:
            file.close()
        else:
            print("Code Not Existed! Please try again")
            modify_roti_canai()

    new_code = str(input("New Food Item Code: ").upper())
    new_name = str(input("New Food Item Name: ").upper())
    new_price = str(input("New Food Item Price: "))

    new_data = []
    file = open("roticanai.txt", "r")
    for item in file:
        data = item.split(",")
        code = data[0]
        if code != old_code:
            new_data.append(item)
        else:
            f = open("temp_file.txt", "w")
            f.write(new_code + "," + new_name + "," + new_price + "," + "\n")
            f.close()
            r = open("temp_file.txt", "r")
            for line in r:
                new_data.append(line)
            r.close()
            print("\n", new_code, new_name, new_price, "Successfully modify in Menu!")
    file.close()

    roticanai = open("roticanai.txt","w")
    for item in new_data:
        roticanai.write(item)
    roticanai.close()
    while True:
        back = str(input("\n(b) Back: "))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print("Invalid Answer")


def modify_remove_roti_canai():
    print("*-- Modify Roti Canai Menu --*\n")
    old_code = str(input("Enter a Item Code for Removing (e.g. RC01): "))
    file = open("roticanai.txt", "r")
    temp_list = []
    for line in file.readlines():
        data = line.split(",")
        code = data[0]
        if old_code.upper() != code:
            temp_list.append(line)
    file.close()
    file = open("roticanai.txt", "w")
    for item in temp_list:
        file.write(item)
    print(old_code,"Is Removed From Menu\n")
    file.close()
    while True:
        back = input('(b) Back: ')
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print('**Invalid Answer**')

def modify_murtabak():
    print("\n*-- Modify Murtabak Menu --*\n")
    with open("murtabak.txt", "r") as file:
        old_code = str(input("Enter a Item Code for Modifying (e.g. M001): ").upper())
        temp_list = []
        temp_name = []
        for line in file.readlines():
            data = line.split(",")
            code = data[0]
            name = data[1]
            temp_list.append(code)
            temp_name.append(name)
        if old_code in temp_list:
            file.close()
        else:
            print("Code Not Existed! Please try again")
            modify_murtabak()

    new_code = str(input("New Food Item Code: ").upper())
    new_name = str(input("New Food Item Name: ").upper())
    new_price = str(input("New Food Item Price: "))

    new_data = []
    file = open("murtabak.txt", "r")
    for item in file:
        data = item.split(",")
        code = data[0]
        if code != old_code:
            new_data.append(item)
        else:
            f = open("temp_file.txt", "w")
            f.write(new_code + "," + new_name + "," + new_price + "," + "\n")
            f.close()
            r = open("temp_file.txt", "r")
            for line in r:
                new_data.append(line)
            r.close()
            print("\n", new_code, new_name, new_price, "Successfully modify in Menu!")
    file.close()

    murtabak = open("murtabak.txt","w")
    for item in new_data:
        murtabak.write(item)
    murtabak.close()
    while True:
        back = str(input("\n(b) Back: \n"))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print("Invalid Answer")


def modify_remove_murtabak():
    print("*-- Modify Murtabak Menu --*\n")
    old_code = str(input("Enter a Item Code for Removing (e.g. M001): ").upper())
    file = open("murtabak.txt", "r")
    temp_list = []
    for line in file.readlines():
        data = line.split(",")
        code = data[0]
        if old_code != code:
            temp_list.append(line)
    file.close()
    file = open("murtabak.txt", "w")
    for item in temp_list:
        file.write(item)
    print(old_code,"Is Removed From Menu\n")
    file.close()
    while True:
        back = str(input('(b) Back: '))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print('**Invalid Answer**')
            modify_remove_murtabak()
#op3
def modify_nasi_goreng():
    print("\n*-- Modify Nasi Goreng Menu --*\n")
    with open("nasigoreng.txt", "r") as file:
        old_code = str(input("Enter a Item Code for Modifying (e.g. N001): ").upper())
        temp_list = []
        temp_name = []
        for line in file.readlines():
            data = line.split(",")
            code = data[0]
            name = data[1]
            temp_list.append(code)
            temp_name.append(name)
        file.close()
        if old_code in temp_list:
            file.close()
        else:
            print("Code Not Existed! Please try again")
            modify_nasi_goreng()

    new_code = str(input("New Food Item Code: ").upper())
    new_name = str(input("New Food Item Name: ").upper())
    new_price = str(input("New Food Item Price: "))

    new_data = []
    file = open("nasigoreng.txt", "r")
    for item in file:
        data = item.split(",")
        code = data[0]
        if code != old_code:
            new_data.append(item)
        else:
            f = open("temp_file.txt", "w")
            f.write(new_code + "," + new_name + "," + new_price + "," + "\n")
            f.close()
            r = open("temp_file.txt", "r")
            for line in r:
                new_data.append(line)
            r.close()
            print("\n",new_code, new_name, new_price, "Successfully modify in Menu!")
    file.close()

    nasigoreng = open("nasigoreng.txt","w")
    for item in new_data:
        nasigoreng.write(item)
    nasigoreng.close()
    print(old_code, "Is Removed From Menu\n")
    while True:
        back = str(input("\n(b) Back: \n"))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print("Invalid Answer")

def modify_remove_nasi_goreng():
    print("*-- Modify Nasi Goreng Menu --*\n")
    old_code = str(input("Enter a Item Code for Removing (e.g. N001): ").upper())
    file = open("nasigoreng.txt", "r")
    temp_list = []
    for line in file.readlines():
        data = line.split(",")
        code = data[0]
        if old_code != code:
            temp_list.append(line)
    file.close()
    file = open("nasigoreng.txt", "w")
    for item in temp_list:
        file.write(item)
    print(old_code, "Is Removed From Menu\n")
    file.close()
    while True:
        back = str(input('(b) Back: '))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print('**Invalid Answer**')

#op4
def modify_mee():
    print("\n*-- Modify Mee Menu --*\n")
    with open("mee.txt", "r") as file:
        old_code = str(input("Enter a Item Code for Modifying (e.g. MG01): ").upper())
        temp_list = []
        temp_name = []
        for line in file.readlines():
            data = line.split(",")
            code = data[0]
            name = data[1]
            temp_list.append(code)
            temp_name.append(name)
        if old_code in temp_list:
            file.close()
        else:
            print("Code Not Existed! Please try again")
            modify_mee()

    new_code = str(input("New Food Item Code: ").upper())
    new_name = str(input("New Food Item Name: ").upper())
    new_price = str(input("New Food Item Price: "))

    new_data = []
    file = open("mee.txt", "r")
    for item in file:
        data = item.split(",")
        code = data[0]
        if code != old_code:
            new_data.append(item)
        else:
            f = open("temp_file.txt", "w")
            f.write(new_code + "," + new_name + "," + new_price + "," + "\n")
            f.close()
            r = open("temp_file.txt", "r")
            for line in r:
                new_data.append(line)
            r.close()
            print("\n", new_code, new_name, new_price, "Successfully modify in Menu!")
    file.close()

    mee = open("mee.txt","w")
    for item in new_data:
        mee.write(item)
    mee.close()
    while True:
        back = str(input("\n(b) Back: \n"))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print("Invalid Answer")

def modify_remove_mee():
    print("*-- Modify Mee Menu --*\n")
    old_code = str(input("Enter a Item Code for Removing (e.g. MG01): ").upper())
    file = open("mee.txt", "r")
    temp_list = []
    for line in file.readlines():
        data = line.split(",")
        code = data[0]
        if old_code != code:
            temp_list.append(line)
    file.close()
    file = open("mee.txt", "w")
    for item in temp_list:
        file.write(item)
    print(old_code, "Is Removed From Menu\n")
    file.close()
    while True:
        back = str(input('(b) Back: '))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print('**Invalid Answer**')

#op5
def modify_minuman():
    print("\n*-- Modify Minuman Menu --*\n")
    with open("minuman.txt", "r") as file:
        old_code = str(input("Enter a Item Code for Modifying (e.g. K001): ").upper())
        temp_list = []
        temp_name = []
        for line in file.readlines():
            data = line.split(",")
            code = data[0]
            name = data[1]
            temp_list.append(code)
            temp_name.append(name)
        if old_code in temp_list:
            file.close()
        else:
            print("Code Not Existed! Please try again")
            modify_minuman()

    new_code = str(input("New Food Item Code: ").upper())
    new_name = str(input("New Food Item Name: ").upper())
    new_price = str(input("New Food Item Price: "))

    new_data = []
    file = open("minuman.txt", "r")
    for item in file:
        data = item.split(",")
        code = data[0]
        if code != old_code:
            new_data.append(item)
        else:
            f = open("temp_file.txt", "w")
            f.write(new_code + "," + new_name + "," + new_price + "," + "\n")
            f.close()
            r = open("temp_file.txt", "r")
            for line in r:
                new_data.append(line)
            r.close()
            print("\n", new_code, new_name, new_price, "Successfully modify in Menu!")
    file.close()

    minuman = open("minuman.txt","w")
    for item in new_data:
        minuman.write(item)
    minuman.close()
    while True:
        back = str(input("\n(b) Back: \n"))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print("Invalid Answer")

def modify_remove_minuman():
    print("*-- Modify Minuman Menu --*\n")
    old_code = str(input("Enter a Item Code for Removing (e.g. K001): ").upper())
    file = open("minuman.txt", "r")
    temp_list = []
    for line in file.readlines():
        data = line.split(",")
        code = data[0]
        if old_code != code:
            temp_list.append(line)
    file.close()
    file = open("minuman.txt", "w")
    for item in temp_list:
        file.write(item)
    print(old_code, "Is Removed From Menu\n")
    file.close()
    while True:
        back = str(input('(b) Back: '))
        if back == 'b' or back == 'B':
            modifyitem()
        else:
            print('**Invalid Answer**')
            modify_remove_minuman()

# Display records for specific parts/fields
def display_records():
    print("\n", "*" * 8 + " DISPLAY RECORDS " + "*" * 8,
          "\n\n(1) Display All Food Category\n(2) Display All Food Items\n(3) Display All Customers Orders Records\n(4) Display All Customers Payment Records\n(5) Back")
    user_input = str(input("\n\nPlease Choose Category 1-5: "))
    print('\n')
    if user_input == "1":
        display_fcategory()
    elif user_input == "2":
        display_fitem()
    elif user_input == "3":
        display_cust_orders()
    elif user_input == "4":
        display_cpayment()
    elif user_input == "5":
        def_admin_main()
    else:
        print("***Invalid Category, Please Try Again!***")
        display_records()

# Display food category record
def display_fcategory():
    print("\n------------------------DISPLAY  FOOD  CATEGORY----------------------------")
    print("(1) ROTI CANAI\n(2) MURTABAK\n(3) NASI GORENG\n(4) MEE\n(5) MINUMAN\n\n(B) Back\n")
    while True:
        user_input = str(input("Press B to Back: "))
        if user_input == "b" or user_input == "B":
            display_records()
        else:
            print("**Invalid Answer**\nPress B For Back\n")

# Display food item record
def display_fitem():
    print("-------------------------- DISPLAY  ALL  FOOD  ITEM -------------------------")
    print("(1) ROTI CANAI\n(2) MURTABAK\n(3) NASI GORENG\n(4) MEE\n(5) MINUMAN\n\n(b) Back\n")
    selection = str(input("Enter An Option To Proceed: "))
    if selection == "1":
        print("\n*-*-*- Display Roti Canai Menu *-*-*")
        roti_canai_view = open("roticanai.txt")
        for line in roti_canai_view:
            print(line, end="")
        while True:
            back = str(input("\nPress B to back: "))
            if  back == "b" or back == "B":
                display_fitem()
            else:
                print("Invalid Input!!")
    elif selection == "2":
        print("\n*-*-*- Display Murtabak Menu *-*-*")
        murtabak_view = open("murtabak.txt")
        for line in murtabak_view:
            print(line, end="")
        while True:
            back = str(input("\nPress B to back: "))
            if back == "b" or back == "B":
                display_fitem()
            else:
                print("Invalid Input!!")
    elif selection == "3":
        print("\n*-*-*- Display Nasi Goreng Menu *-*-*")
        nasi_goreng_view = open("nasigoreng.txt")
        for line in nasi_goreng_view:
            print(line, end="")
        while True:
            back = str(input("\nPress B to back: "))
            if back == "b" or back == "B":
                display_fitem()
            else:
                print("Invalid Input!!")
    elif selection == "4":
        print("\n*-*-*- Display Mee Menu *-*-*")
        mee_view = open("mee.txt")
        for line in mee_view:
            print(line, end="")
        while True:
            back = str(input("\nPress B to back: "))
            if back == "b" or back == "B":
                display_fitem()
            else:
                print("Invalid Input!!")
    elif selection == "5":
        print("\n*-*-*- Display Minuman Menu *-*-*")
        minuman_view = open("minuman.txt")
        for line in minuman_view:
            print(line, end="")
        while True:
            back = str(input("\nPress B to back: "))
            if back == "b" or back == "B":
                display_fitem()
            else:
                print("Invalid Input!!")
    elif selection == "b" or selection == "B":
        display_records()
    else:
        print('**Invalid Answer**')
        display_fitem()

# Display customer order record
def display_cust_orders():
    with open("customer_order_records.txt", "r") as show_corders:
        for line in show_corders.readlines():
            data = line.split(',')
            order_id = data[0]
            username = data[1]
            date = data[2]
            order_item = data[3]
            quantity = data[4]
            total_amount = data[5]
            print("----- DISPLAY CUSTOMERS ORDERS RECORDS -----")
            print("OrderID: ",order_id, "\nUsername: ", username, "\nDate: ", date, "\nOrder Item: ", order_item, "\nQuantity:", quantity,
                  "\nTotal Amount: ", total_amount, "\n")
    while True:
        back = str(input("(b) Back: "))
        if back == "b" or back == "B":
            display_records()
        else:
            print("**Invalid Answer**")

# Display customer payment records
def display_cpayment():
    with open("customer_order_records.txt", "r") as records:
        for line in records.readlines():
            data = line.split(',')
            order_id = data[0]
            username = data[1]
            date = data[2]
            order_item = data[3]
            quantity = data[4]
            total_amount = data[5]
            payment_method = data[6]
            print("----- DISPLAY CUSTOMERS ORDERS AND PAYMENT RECORDS -----")
            print("OrderID: ",order_id, "Username: ", username, "\nDate: ", date, "\nOrder Item: ", order_item, "\nQuantity: ", quantity,"\nTotal Amount: ", total_amount, "\nPayment Method: ", payment_method, "\n")
    while True:
        back = str(input("(b) Back: "))
        if back == "b" or back == "B":
            display_records()
        else:
            print("**Invalid Answer**\nPress B To Back")

# Search specific customer order and payment
def search_order_payment():
    print("\n", "*" * 8 + " SEARCH ORDERS AND PAYMENT RECORDS " + "*" * 8, "\n\n(1) Search Orders Records\n(2) Search Payments Records\n(3) Back\n")
    user_input = input("\n\nPlease Choose Category 1-3: ")
    if user_input == "1":
        search_order()
    elif user_input == "2":
        search_payment()
    elif user_input == "3":
        def_admin_main()
    else:
        print("***Invalid Input! Please Try Again***")
        search_order_payment()

# Search specific customer order
def search_order():
    print("\nPlease Enter Customer Username For Searching.")
    search_cust_username = input("Customer Username: ").upper()
    show_search_order = open("customer_order_records.txt", "r")
    view_order = show_search_order.read()
    view_order_by_line = view_order.splitlines()
    show_search_order.close()
    for line in view_order_by_line:
        data = line.split(",")
        if search_cust_username in data[1]:
            print("\nSearching.....")
            time.sleep(1)
            print(
                "Done Searching!\n\n\n*----- " + search_cust_username + " CUSTOMERS ORDERS AND PAYMENT RECORDS -----*")
            print("*" * 55)
            print(" OrderID\t\t  : ",data[0], "\n Username\t\t  : ", data[1], "\n Date\t\t\t  : ", data[2], "\n Ordered\t\t  : ", data[3],
                  "\n Total Quantity\t\t  : ", data[4], "\n Total Amount\t\t  : ", data[5])
            print("*" * 55)
    while True:
        option = input("\nPlease Further (c) Continue (b) Back: ")
        if option == "b" or option == "B":
            search_order_payment()
        elif option == "c" or option == "C":
            search_order()
        else:
            print("\nInvalid Input! Please Try Again")

# Search specific customer payment
def search_payment():
    print("Please Enter Customer Username For Searching")
    search_username = input("Customer Username: ").upper()
    show_search_payment = open("customer_order_records.txt", "r")
    view_payment = show_search_payment.read()
    view_payment_by_line = view_payment.splitlines()
    show_search_payment.close()
    for line in view_payment_by_line:
        data = line.split(",")
        if search_username in data[1]:
            print("\nSearching.....")
            time.sleep(1)
            print(
                "Done Searching!\n\n\n*----- " + search_username + " CUSTOMERS ORDERS AND PAYMENT RECORDS -----*")
            print("*" * 55)
            print(" OrderID\t\t: ",data[0], "\n Username\t\t: ", data[1], "\n Date\t\t\t: ", data[2], "\n Ordered\t\t: ", data[3],
                  "\n Total Quantity\t\t: ", data[4], "\n Total Amount\t\t: ", data[5],"\n Payment Method\t\t: ", data[6])
            print("*" * 55)
    while True:
        option = input("\nPlease Further (c) Continue (b) Back: ")
        if option == "b" or option == "B":
            search_order_payment()
        elif option == "c" or option == "C":
            search_order()
        else:
            print("\nInvalid Input! Please Try Again")

main_menu()

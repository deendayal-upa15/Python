import re 
import json 

def main():
    """
    In this project,we take an json data to storing information of a person and 
    making an output json file
    """
    # Open the data file
    with open("info_dictionary.json", "r") as f:
        info_dictionary = json.load(f)
        #give choice to see contact, save contact or update contact
        while True:
            print("\n                    Information Diary\nYou can create, edit and view info of a person.\nEnter 'Exit' to exit")
            choice = input("Search(press s) or Create(press c): ")
            #save file and exit the program
            if choice == "exit" or choice == "Exit" :
                #save dictionary as json file
                with open("info_dictionary.json", "w") as f:
                    json.dump(info_dictionary, f, indent=4)
                break
            #initiating search function
            elif choice == "s":
                name = input("Search by name: ")
                search(name, info_dictionary)
            #initiating create function
            elif choice == "c":
                create(info_dictionary)
            #for wrong input
            else:
                print("Invalid option!! \nChoose again.") 

def create(dict):
    """
    Function will create a new contact and save it in contact dictionary
    """
    while True:
        #making a Dictionary to save info of name key
        info = {}
        print("\nMaking a new Entry.")
        name = input("Enter Name(press enter to go back): ")
        #exit loop when saving is done
        if name == "":
            break
        #if name already exist
        elif name in dict:
            #show exiting information and ask to edit or exit
            print("Name already exist.\n")
            search(name, dict)
            ask = input("\nWant to edit(press e) or exit(press any other key)? ")
            if ask == "e":
                info["Name"] = name
                add_number(name, info)
                break
            else:
                break
        else:
            info["Name"] = name
            add_number(info)
            #add more information to contact
            all_info = additional_info(info)
            dict[name]= all_info
    return dict

def add_number(list):
    """
    This function will varify and add number to corresponding key name
    """
    while True:
        number = input("Contact Number: ")
        #varifying number is correct or not. (for indian numbers)
        pattern = re.compile("(0|91)?[6-9][0-9]{9}")
        if (pattern.match(number)):
            list["Contact Number"] = number
            break
        else:
            #asking for save if number is invalid
            ask = input("Invalid Number!!! \nWant to save(press s) or re-enter number(press enter)? ")
            if ask == "s":
                list["Contact Number"] = number
            else:
                add_number(list)
            break

def additional_info(list):
    """
    This function will save other details like Email and address.
    """
    while True:
        email = input("Email Address(Leave blank to skip): ")
        #checking for validation of mail address
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, email)):
            #if mail is valid
            break
        else:
            print("Invalid Email")
    list["Email Address"] = email
    address = input("Address(Leave blank to skip): ")
    list["Address"] = address
    return list

def search(name, dict):
    """
    This function will search name in info directory and show corresponding information.
    """
    #print info corresponding to the values
    if name in dict:
        info = dict.get(name)
        print("Name: "+ info["Name"])
        print("Phone Number: "+ info["Contact Number"])
        print("Email Address: "+ info["Email Address"])
        print("Address: "+ info["Address"])
    else:
        print("No Information Found!!!")
        ask = input("Want to add Person?(Y/N) ")
        if ask == "Y" or ask == "y":
            create(dict)
    
if __name__ == '__main__':
    main()

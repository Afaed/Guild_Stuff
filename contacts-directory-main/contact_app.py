

def view():

    with open("contacts.csv") as file:

        contact_dictionary = {}
        contact_lst = []
        for person in file.readlines():
            contact = person.strip().split(",")
            contact_dictionary = {
                "name": contact[0], #First Key
                "phone": contact[1] # Second Key
            }
            contact_lst.append(contact_dictionary)
        print(f"{'Name':<{35}} | Phone Numbers")
        print("-" * (56))
        
        for i in range (1, len(contact_lst)):
            print(f"{contact_lst[i].get('name'):<35} | {contact_lst[i].get('phone')}")
    

def find(name: str):
    result = ""
    file = open("contacts.csv", "r")
  
    for contact in file.readlines():
      person = contact.strip().split(",")
      if person[0] == name:
          result = contact
          break
    if result == "":
      return "Person not found"
    file.close()
    return result
  
def add(person: str):
    file = open("contacts.csv", "a")
    file.write(person)
    file.close()

def main():
    start = True
    while start:
        print('''
            1. View Contacts
            2. Find Contacts 
            3. Add Contacts
            4. Exit''')
        
        try:
            intro_input = input("Enter a number: ")
            intro_input = int(intro_input)
            if intro_input > 4 or intro_input < 1:
                raise Exception("The number is not in the range")
            
            if intro_input == 1:
                view()
            
            elif intro_input == 2 :
                try:
                    name = input("Enter the contacts full name: ")
                    if name == "":
                        raise Exception()
                    print(find(name).strip())
                except:
                    print("Name must be filled in!")
            
            elif intro_input == 3 :
                try:
                    add_name = input("Enter a name to be added: ")
                    add_phone = input("Enter their phone number: ")
                    if add_name == "" or add_phone == "":
                        raise Exception()   
                    add(f"\n{add_name},{add_phone}")
                except:
                    print("Name or phone number is missing")
                    continue
            elif intro_input == 4 :
                start = False
                print("Thank you for using the contact book app.")
            
        except ValueError:
            print("Invalid-input must be a number between 1 and 4")
            continue
        except Exception:
            print("Error: number not in range")
            continue
      
main()
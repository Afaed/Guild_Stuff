def populate():
    with open("contacts.csv") as file:

        contact_dictionary = {}
        contact_lst = []
        for person in file.readlines():
            contact = person.strip().split(",")
            contact_dictionary = {
                "name": contact[0],
                "phone": contact[1]
            }
            contact_lst.append(contact_dictionary)
        print(contact_lst)

populate()
import random
import json

def first_name() -> str:
    """Return a randomly generated first name.

    :return: 
    """
    with open("./data/first_names.txt") as file:
        
        name_lst = list(file.readlines())
        name = random.choice(name_lst)
        return name

def last_name() -> str:
    """Return a randomly generated surname.

    :return: 
    """
    with open("./data/last_names.txt") as file:
        last_name_lst = list(file.readlines())
        last_name = random.choice(last_name_lst)
        return last_name
    

def full_name() -> str:
    """Returns a randomly generated first and last name.
    
    :return:
    """
    return f" {first_name().strip()} {last_name().strip()}"

def phone_number() -> str:
    """Return a randomly generated phone number.

    :return: 
    """
    number = ""
    for i in range(11):
        random_int = str(random.randrange(0,9))
        number+=random_int
    return "{}{}{}-{}{}{}-{}{}{}{}".format(*number)

def address(secondary: str=None) -> str:
    """Return a randomly generated street address.

    :param secondary: additional address info (apt., suite, etc)
    :return:
    123 Main Street, apt no. 3 
    """
    
    with open("data.json") as file:
        street_names = ["Lunada", "Danville", "Oyster", "Maple", "Main"]
        new_file = open("data.json")
        address_lst = json.load(file).get("address_types")
        street_lst = json.load(new_file).get("street_types")

        number = random.randint(0, 5000)
        smaller_number = random.randint(1, 25)

        address_type = random.choice(address_lst)
        street_type = random.choice(street_lst)
        address = f"{number} {random.choice(street_names)} {street_type}, {address_type} {smaller_number}"
        new_file.close()

        return address


def town() -> str:
    """Return a randomly generated town.

    :return: 
    """
    with open("data.json") as file:
        
        return random.choice(json.load(file).get("cities"))

def full_address() -> str:
    """Return a street, city and state.

    :return:
    """
    with open("data.json") as file:
        states = json.load(file).get('states') 

        state_lst = list(states.values())
        return f"{address()}, {town()}, {random.choice(state_lst)}"

def company_name() -> str:
    """Return a randomly generated company name.

    :return: 
    """
    with open("data.json") as company_file:
        with open("./data/first_names.txt") as file:
            companies = list(json.load(company_file).get('company_types'))
            name = list(file.readlines())

            return f"{random.choice(name).strip()} {random.choice(companies)}"


def price_str(max_value: int=100, acc=2, curr='usd') -> str:
    """Returns random price.

    :params max_value: highest price
    :params acc: number of digits after the decimal
    """

    return f"{round(max_value *random.random(), acc)} {curr}"

def price(max_value: int=100, acc=2) -> float:
    """Returns random price.

    :params max_value: highest price
    :params acc: number of digits after the decimal
    """
    return float(round(max_value * random.random(), acc))

def email(company: str='example', tld: str='.com') -> str:
    """Return a randomly generated email address.

    :param company:
    :param tld: top level domain (.com, .net, .org, etc)
    :return: 
    """
    return f"{first_name().strip()[0]}{last_name().strip()}{random.randint(0,1000)}@{company}{tld}"



def text(sentences: int=1) -> str:
    """Return randomly generated text.

    :param sentences: the number of sentences
    :return: 
    """
    with open("./data/words.txt") as file:
        paragraph = []
        
        trigger = 0
        period_trigger = 0
        end = random.randrange(0, 9)

        words = list(file.readlines())

        for i in range(sentences):
            word = random.choices(words, k=5)
            paragraph.append(word)
        answer = ".".join(paragraph) + "."
        return answer
        # while trigger != sentences:  
        #     print(f"Period trigger: {period_trigger}")
        #     print(f"End: {end}")
            
        #     to_be_added = random.choices(words, k=1)
        #     paragraph+=".".join(to_be_aded)
        #     period_trigger+=1
        #     if period_trigger == end:
                
        #         trigger+=1
        #     else:
        #         paragraph+= " "

text()
if __name__ == '__main__':
    import sys

    args = sys.argv[1:]

    print('Phoney options: name, phone')

import requests
# Process Json

# Identifies data
# Display data
# Ask user for index, key
# stores that in history
# go back to step 1


user_url = None


def proccessing_url(link):
    url = link
    response = requests.get(url)
    if response.status_code != 200:
        print("Invalid url")
        return False
    else:
        return response.json()


def identifier(parameter):
    match parameter:
        case dict():
            return dict
        case list():
            return list
        case None:
            return None

        
def display_dictionary(parameter):
    for key, value in parameter.items():
        print(f"{key} : {value}")


def display_list(parameter):
    index = 0
    for item in parameter:
        print(f"{index} : {item}")
        index += 1


def processed_data(*data_with_key):
    pass


def history(data, history, key = False, index = False):
    if key == False: 
        history.append(index)
    if index == False:
        history.append(key)

    return [data,history]


def main(parameter):
    # Processed json
    while True:
        json_file = proccessing_url(parameter)
        if not json_file:
            print("Incorrect url or unstable internet")
            break

    history = []
    if len(history) == 0:
        data = json_file
    elif len(history) > 0:
        data = new_data

    while True:
        # Dictionary
        if identifier(data) == dict:        

            # Display 
            display_dictionary(data)

            # Ask user for key and stores it
            while True:
                try:
                    key = input("Type the key of where you want to go into")
                    data_with_key = history(data = data, history = history, key = key)
                    new_data = processed_data(*data_with_key)
                except KeyError:
                    print("Incorrect key")
                    continue

            # go back to step 1

        # List
        if identifier(data) == list:        

            # Display 
            display_list(data)

            # Ask user for key and stores it
            while True:
                try:
                    index = input("Type the index of where you want to go into")
                    data_with_key = history(data = data, history = history, index = index)
                    new_data = processed_data(data_with_key)
                    history(index = index)
                except IndexError:
                    print("Incorrect index")
                    continue

            # go back to step 1

        # Else
        else:
            print("You hit the end of the array")

main(user_url)
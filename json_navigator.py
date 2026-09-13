import requests

history = []


def processing_url(link):
    response = requests.get(link)

    if response.status_code != 200:
        print("Invalid url")
        return False
    else:
        return response.json()


def display_dictionary(parameter):
    print(f"\n{parameter.keys()}")

def display_list(parameter):
    index = 0
    print("\n")
    for item in parameter:
        print(f"{index} : {item}")
        index += 1


def processed_data(data, history):
    current_data = data

    for key_index in history:
        current_data = current_data[key_index]

    return current_data


def main():

    # Processing json
    while True:
        user_link = input("Put the website link: ").replace(" ", "")
        json_file = processing_url(user_link)

        if json_file is False:
            print("Wrong link or unstable connection")
            continue

        break

    while True:
        data = processed_data(json_file, history)

        # 1. Dictionary
        if type(data) == dict:

            while True:
                try:
                    # Display
                    display_dictionary(data)
                    print(f"Your current history : {history}")

                    # Ask user for key or to go back
                    user_input = input("\nType the keyname or type back: ")

                    if user_input.lower() == "back":
                        break

                    key = user_input
                    data[key]
                    break

                except (KeyError, ValueError):
                    print("Incorrect input")
                    continue

            # Remove or back
            if user_input.lower() == "back":

                if len(history) != 0:
                    history.pop()
                else:
                    print("You're at the top already")

            else:
                # Adds history
                history.append(key)

            continue

        # 2. List
        if type(data) == list:


            while True:
                try:
                    # Display
                    display_list(data)
                    print(f"Your current history : {history}")

                    # Ask user for index
                    user_input = input("\nType the index number or type back: ")

                    if user_input.lower() == "back":
                        break

                    index = int(user_input)
                    data[index]
                    break

                except (IndexError, ValueError):
                    print("Incorrect input")
                    continue

            # Remove or back
            if user_input.lower() == "back":

                if len(history) != 0:
                    history.pop()
                else:
                    print("You're at the top already")

            else:
                history.append(index)

            continue

        # 3. Else
        else:
            print(f"{history[-1]}: {data}")

            user_input = input("Type back to return: ")

            if user_input.lower() == "back":
                if len(history) != 0:
                    history.pop()
                else:
                    print("You're already at the top.")

main()

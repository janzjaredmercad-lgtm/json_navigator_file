import requests


class JSON_Navigator:
    def __init__(self, data):
        self.data = data
        self.history = []


    def get_current_data(self):
        current_data = self.data

        for key_index in self.history:
            current_data = current_data[key_index]

        return current_data


    def display_dictionary(self, data):
        print("\nKeys:")
        print(", ".join(data))
        print()


    def display_list(self, data):
        print("\nIndexes:")
        for i in range(len(data)):
            if i < len(data) - 1:
                print (f"{i}, ",end="")
            else:
                print(i,end="")
        print()


    def navigate(self):
        while True:
            current_data = self.get_current_data()

            # Dictionary
            if type(current_data) is dict:
                self.navigate_dictionary(current_data)

            # List
            elif type(current_data) is list:
                self.navigate_list(current_data)

            # Final value
            else:
                while True:
                    print(f"\nYour current history : {self.history}")
                    print(f"\nValue: {current_data}")

                    user_input = input("Type back to return: ")

                    if user_input.lower() == "back":
                        if len(self.history) != 0:
                            self.history.pop()
                        else:
                            print("You're already at the top.")
                        break
                    else:
                        print("Type back to continue")


    def navigate_dictionary(self, data):
        while True:
            try:
                # Display
                self.display_dictionary(data)
                print(f"Your current history : {self.history}")

                # Ask user for valid key or to go back
                user_input = input("\nType the keyname or type back: ")

                if user_input.lower() == "back":
                    break

                key = user_input
                data[key]
                break

            except (KeyError, ValueError):
                print("Incorrect input")
                continue

        # Either remove and back
        if user_input.lower() == "back":

            if len(self.history) != 0:
                self.history.pop()
            else:
                print("You're at the top already")

        # Or add history
        else:
            self.history.append(key)


    def navigate_list(self, data):
        while True:
            try:
                # Display
                self.display_list(data)
                print(f"Your current history : {self.history}")

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

        # Either remove and back
        if user_input.lower() == "back":

            if len(self.history) != 0:
                self.history.pop()
            else:
                print("You're at the top already")

        # Or add history
        else:
            self.history.append(index)


def processing_url(link):
    try:
        response = requests.get(link)

        if response.status_code != 200:
            return False

        return response.json()

    except (requests.exceptions.RequestException, ValueError):
        return False


def inspect_json(data):
    navigator = JSON_Navigator(data)
    navigator.navigate()


def main():

    # Processing json
    while True:
        user_link = input("Put the website link: ").replace(" ", "")
        json_file = processing_url(user_link)

        if json_file is False:
            print("Wrong link or unstable connection")
            continue

        break

    inspect_json(json_file)


if __name__ == "__main__":
    main()
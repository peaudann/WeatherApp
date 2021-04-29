import requests

API = "926c8adc05d91ce7a01de33400249e5a"
URL = "https://api.openweathermap.org/data/2.5/weather?zip="


def retrieve_zip():

    zip_code = input("Enter your zip code(or 'q' to quit: \n")
    if zip_code == 'q':
        print("Goodbye")
        quit()
    elif len(zip_code) !=5:
        print("Enter a valid 5 didgit zip code.")
    elif not zip_code.isdigit():
        print("Zip codes should only contain numbers.")
    else:
        return zip_code


def connect(url, zip_code):

    try:
        res = requests.get(url + zip_code + "&units=imperial&appid=" + API)
        res.raise_for_status()
        print(f'Connection successful: status {str(res.status_code)}')
        return res.json()
    except TypeError as err:
        print("Invalid input.\n")
        if __name__ == "__main__":
            main()
    except requests.exceptions.HTTPError as err:
        print(f'Error {str(err)}')
        print("Incorrect zip code used, please try again.\n")
        if __name__ == "__main__":
            main()


def main():

    print("Welcome to the Weather App")
    input("To start hit enter")

    while True:

        data = connect(URL, retrieve_zip())

        city = data["name"]
        weather_descrip = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]

        print(
            f'\nCity: {city}\n'
            f'Weather Description:     {weather_descrip.title()}\n'
            f'Temperature: {temp}\n'
            f'Daily Low: {temp_min}\n'
            f'Daily High: {temp_max}\n'
            f'Humidity: {humidity}%\n'
        )


if __name__ == "__main__":
    main()

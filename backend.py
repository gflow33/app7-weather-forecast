import requests

API_KEY = "65278883de84174a5cc954217835d623"
# city_name = "lagos"


def get_data(place, forecastdays):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecastdays
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Lagos", forecastdays=3))
import requests

iss_url = "http://api.open-notify.org/iss-now.json"

def get_iss_data():
    response = requests.get(iss_url)
    data = response.json()

    return data

def display_iss_data(data):
    iss_message = data["message"]
    position_lat = data["iss_position"]["latitude"]
    position_long = data["iss_position"]["longitude"]
    time_stamp = data["timestamp"]

    print("*" * 30)
    print(iss_message)
    print(position_lat)
    print(position_long)
    print(time_stamp)
    print("*" * 30)
    

def main():
    print("***Starting ISS Tracker*** \n")

    iss_data = get_iss_data()
    display_iss_data(iss_data)

if __name__ == "__main__":
    main()
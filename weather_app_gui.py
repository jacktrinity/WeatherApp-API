from tkinter import *
import json
import urllib.request
import time

# Our Window
root = Tk()
root.title("Weather Application")


def city_output(event):
    city_name = city_input.get();
    get_api(city_name)


def get_api(city):
    url_first_half = "http://api.openweathermap.org/data/2.5/weather?q="
    url_second_half = ",us&appid=8da995db2c96601bd55534c67e8856db"
    full_url = url_first_half + city + url_second_half

    response = urllib.request.urlopen(full_url)
    result = json.loads(response.read())

    weather_forecast(result)

def weather_forecast(weather_result):
    #city_name = weather_result["name"]  # City Name
    #weather_description = weather_result["weather"][0]["main"]  # Description of the weather

    my_time = weather_result["dt"]

    intro_time = Label(root, text=str(time.ctime(my_time)))
    intro_time.grid(row=1, column=1, sticky=W)


    current_temperature = weather_result["main"]["temp"]  # Current temperature
    min_temperature = weather_result["main"]["temp_min"]  # Min temperature
    max_temperature = weather_result["main"]["temp_max"]  # Max temperature

    current_temperature = round(temp_k_to_f(current_temperature), 2)
    min_temperature = round(temp_k_to_f(min_temperature), 2)
    max_temperature = round(temp_k_to_f(max_temperature), 2)

    current_temp_display = Label(root, text=str(current_temperature) + " F")
    current_temp_display.grid(row=2, column=1, sticky=W)

    low_temp_display = Label(root, text=str(min_temperature) + " F")
    low_temp_display.grid(row=3, column=1, sticky=W)

    high_temp_display = Label(root, text=str(max_temperature) + " F")
    high_temp_display.grid(row=4, column=1, sticky=W)


def temp_k_to_f(kevin):
    fahrenheit = (kevin - 273.15) * (9 / 5) + 32

    return fahrenheit


city_label = Label(root, text="Please enter a city: ")
city_label.grid(row=0, column=0, sticky=W)

city_input = Entry(root)
city_input.bind("<Return>", city_output)
city_input.grid(row=0, column=1)


button_enter = Button(root, text="Enter", fg="blue")
button_enter.bind("<Button-1>", city_output)
button_enter.grid(row=0, column=2)

intro_label = Label(root, text="Date and Time: ")
intro_label.grid(row=1, column=0, sticky=W)

intro_time = Label(root, text="Current Weather Report")
intro_time.grid(row=1, column=1, sticky=W)



# Temperature Display
current_temp = 0
low_temp = 0
high_temp = 0

current_temp_label = Label(root, text="Current Temperature: ")
current_temp_label.grid(row=2, column=0, sticky=W)
current_temp_display = Label(root, text=str(current_temp) + " F")
current_temp_display.grid(row=2, column=1, sticky=W)

low_temp_label = Label(root, text="Low Temperature Today: ")
low_temp_label.grid(row=3, column=0, sticky=W)
low_temp_display = Label(root, text=str(low_temp) + " F")
low_temp_display.grid(row=3, column=1, sticky=W)

high_temp_label = Label(root, text="High Temperature Today: ")
high_temp_label.grid(row=4, column=0, sticky=W)
high_temp_display = Label(root, text=str(high_temp) + " F")
high_temp_display.grid(row=4, column=1, sticky=W)


# Display Window
root.mainloop()
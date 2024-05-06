import requests
import tkinter as tk
from tkinter import messagebox

# UI
weather_window = tk.Tk()
weather_window.title("You may need an umbrella today")
weather_window.geometry('600x600')
weather_window.config(padx=20, pady=20)


canvas = tk.Canvas(height=370, width=370)
logo = tk.PhotoImage(file='open_weather_image.png')
canvas.create_image(200, 200, image=logo)
canvas.pack()

FONT = ("Calibri", 16, 'normal')

# City Label
city_label = tk.Label(text="Enter the city name", font=FONT)
city_label.config(padx=5, pady=5)
city_label.pack()

# City Entry
city_entry = tk.Entry(width=20)
city_entry.config(width=30)

city_entry.pack()
city_entry.focus()



# Fetch Weather Button
def fetch_weather():
    city = city_entry.get()
    api_key = 'ENTER_YOUR_API'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch data")
    finally:
        city_entry.delete(0, tk.END)

fetch_button = tk.Button(weather_window, text='See Current Weather', font=('Calibri', 12, 'italic'), command=fetch_weather)
fetch_button.config(padx=10, pady=10)
fetch_button.pack()

# Label for Weather message
weather_label = tk.Label(text="", font=('Calibri', 16, 'italic'))
weather_label.pack()

weather_window.mainloop()
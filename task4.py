direction = input("Convert from Celsius (C) or Fahrenheit (F)? ").upper()
temperature = float(input("Temperature: "))

if direction == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C = {fahrenheit}°F")
elif direction == "F":
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {celsius}°C")
    
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

highest_temperature = max(antarctic_temperatures)
lowest_temperature = min(antarctic_temperatures)

print("Highest Temperature", highest_temperature, "°C")
print("Lowest Temperature", lowest_temperature, "°C")

average_temperature = round(sum(antarctic_temperatures) / len(antarctic_temperatures) , 1)
print("Average Temperature", average_temperature, "°C")

coldest_temperature_abs = abs(min(antarctic_temperatures))
print("The coldest temperature was", coldest_temperature_abs, "°C below freezing.") 
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

city_name = "Tampa"

def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')
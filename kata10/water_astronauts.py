def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument/10 #not-int catcher
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

def alert_navigation_system(err):
    print("ALERT! THINGS ARE GOING BAD, START PANICKING")

def main():
    #"Probemos con cinco astronautas, 100 litros de agua sobrante y dos días"
    #water_left(5, 100, 2)

    #Modificamos ahora la aproximación para llamar al método
    try:
        #water_left(5, 100, 2)
        water_left("3", "200", None)
    except RuntimeError as err:
        alert_navigation_system(err)

if __name__ == '__main__':
    main()
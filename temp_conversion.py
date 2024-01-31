# Todo: Code is a bit unclear

def convert_fahr_to_celcius(fahr):
    """
    Given a temprature in fahr, converts to celcius
    
    :param fahr: Tempratyre in fahrenheit
    :raises ValuError: If temp below absolute zero
    :retyrn: the temprature in celcius
    Arguments:
    fahr: temprature in fahrenheit
    """
    celcius = (fahr - 32) * (5 / 9)
    if celcius < -273.15:
        # if temprature is below zero, throw an error
        raise ValueError(
            f"trying to convert impossible temprature: {fahr}"
        )
    return celcius

def convert_fahr_to_kelvin(fahr):
    celcius = convert_fahr_to_celcius(fahr)
    kelvin = celcius + 273.15
    return kelvin

def convert_centigrade_to_fahrenheit(celsius:float) -> float:
    """Convert a temperature from Centigrade to Fahrenheit.

    Args:
        celsius (float): Temperature in Centigrade.

    Returns:
        float: Temperature in Fahrenheit.
    """
    F = celsius * (9/5) + 32
    return F

def convert_fahrenheit_to_centigrade(fahrenheit:float) -> float:
    """Convert a temperature from Fahrenheit to Centigrade.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Centigrade.
    """
    C = (fahrenheit - 32) * (5/9)
    return C

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Centigrade: "))
    fahrenheit = convert_centigrade_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_centigrade(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
def temperature_check(temperature, unit="C", threshold=30):
    if unit.upper() == "F":
        converted = (temperature - 32) * 5 / 9
    elif unit.upper() == "C":
        converted = (temperature * 9 / 5) + 32      
    else:
        return "Invalid Input! Unit must be either 'C' or 'F'"
        
    if converted < threshold:
        return "Cold Advisory"
    else:
        return "Heat Alert"
        

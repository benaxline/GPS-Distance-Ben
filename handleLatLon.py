

def parse_value(value):
    if value is None:
        return None
    
    value = value.replace("°", "").strip()
    value = value.replace("degrees", "").strip()

    sign = 1
    ending_character = value[-1].upper()
    if ending_character == 'S' or ending_character == 'W':
        sign = -1
        value = value[:-1].strip()
    elif ending_character == 'N' or ending_character == 'E':
        value = value[:-1].strip()

    if not value:
        return None
    
    try:
        val = float(value)

    except ValueError:
        return None
    
    return sign * val

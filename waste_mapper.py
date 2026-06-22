def map_to_waste_category(object_name):

    object_name = object_name.lower()

    # Plastic
    if any(word in object_name for word in [
        "bottle",
        "water_bottle",
        "plastic_bag"
    ]):
        return "Plastic"

    # Metal
    elif any(word in object_name for word in [
        "can",
        "tin",
        "metal"
    ]):
        return "Metal"

    # Paper
    elif any(word in object_name for word in [
        "book",
        "newspaper",
        "envelope"
    ]):
        return "Paper"

    # Glass
    elif any(word in object_name for word in [
        "wine_bottle",
        "glass"
    ]):
        return "Glass"

    # E-Waste
    elif any(word in object_name for word in [
        "cellular_telephone",
        "laptop",
        "keyboard",
        "computer"
    ]):
        return "E-Waste"

    # Organic
    else:
        return "Organic"
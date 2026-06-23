def map_to_waste_category(object_name):

    object_name = object_name.lower()

    # Plastic
    if any(word in object_name for word in [
        "plastic",
        "plastic_bag",
        "bottle",
        "water_bottle"
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
        "envelope",
        "paper"
    ]):
        return "Paper"

    # Glass
    elif any(word in object_name for word in [
        "glass",
        "wine_bottle"
    ]):
        return "Glass"

    # E-Waste
    elif any(word in object_name for word in [
        "cellular_telephone",
        "keyboard",
        "computer",
        "laptop",
        "monitor"
    ]):
        return "E-Waste"

    else:
        return "Organic"
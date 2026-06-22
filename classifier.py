def classify_waste(filename):
    filename = filename.lower()

    if "plastic" in filename or "bottle" in filename:
        return "Plastic"

    elif "paper" in filename or "newspaper" in filename:
        return "Paper"

    elif "glass" in filename:
        return "Glass"

    elif "can" in filename or "metal" in filename:
        return "Metal"

    else:
        return "Organic"
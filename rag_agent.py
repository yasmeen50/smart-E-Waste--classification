INFO_FILE = "knowledge_base/ewaste_info.txt"


def get_information(category):
    with open(INFO_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    categories = [
        "LAPTOP",
        "MOBILE",
        "BATTERY",
        "CHARGER",
        "KEYBOARD",
        "PRINTER"
    ]

    category = category.upper()

    start = text.find(category)

    if start == -1:
        return "No information found for this category."

    end = len(text)

    for next_category in categories:
        if next_category != category:
            position = text.find(next_category, start + len(category))
            if position != -1 and position < end:
                end = position

    return text[start:end].strip()
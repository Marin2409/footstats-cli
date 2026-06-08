# Parse name for URL formatting
# Ex. Cristiano Ronaldo -> cristiano-ronaldo
def parse_name(name):
        parsed_name = '-'.join(name.lower().split())
        return parsed_name

def parse_citizenship(citizenship_tag) -> str | None:
    if not citizenship_tag:
        return None

    countries = [
        img.get("title")
        for img in citizenship_tag.find_all("img")
        if img.get("title")
    ]

    return ", ".join(countries) if countries else None

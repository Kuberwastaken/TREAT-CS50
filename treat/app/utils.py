def identify_triggers(outputs):
    # Initialize a set to store identified triggers
    identified_triggers = set()

    # Iterate over the model outputs
    for response_text in outputs:
        # Check if the response contains a positive indication of the category
        if "yes" in response_text.lower():
            # Extract the category from the response_text
            category = extract_category(response_text)
            if category:
                identified_triggers.add(category)
    
    return list(identified_triggers)

def extract_category(response_text):
    # Define trigger categories
    trigger_categories = [
        "Violence",
        "Death",
        "Substance Use",
        "Gore",
        "Vomit",
        "Sexual Content",
        "Self-Harm",
        "Gun Use"
        "Animal Cruelty",
        "Mental Health Issues"
    ]
    
    # Check if any category is present in the response_text
    for category in trigger_categories:
        if category.lower() in response_text.lower():
            return category
    return None

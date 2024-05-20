def get_word(word_type):
    return input(f"Please enter a {word_type}: ")

def create_story(words):
    story = f"""
    Once upon a time in a {words['adjective1']} land, there was a {words['noun1']} who loved to {words['verb1']}.
    Every day, the {words['noun1']} would go to the {words['noun2']} and {words['verb2']} with a {words['adjective2']} {words['noun3']}.
    One day, a {words['adjective3']} {words['noun4']} appeared and asked, "Would you like to {words['verb3']} with me?"
    The {words['noun1']} was so {words['adjective4']} and said yes! They {words['verb4']} happily ever after.
    """
    return story

def main():
    words = {
        "adjective1": get_word("adjective"),
        "noun1": get_word("noun"),
        "verb1": get_word("verb"),
        "noun2": get_word("noun"),
        "verb2": get_word("verb"),
        "adjective2": get_word("adjective"),
        "noun3": get_word("noun"),
        "adjective3": get_word("adjective"),
        "noun4": get_word("noun"),
        "verb3": get_word("verb"),
        "adjective4": get_word("adjective"),
        "verb4": get_word("verb"),
    }

    story = create_story(words)
    print(story)

if __name__ == "__main__":
    main()

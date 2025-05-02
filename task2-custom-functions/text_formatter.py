"""
    text_formatter.py
    Asimple script that formats text in different ways.

    """
def format_text(text,uppercase=False,lowercase=False,capitalized=False,strip=True,replace_newlines=True):
    """
    parameters:
    formats the input based on what provided
    text(str):the text to be formated
    uppercase(bool
    lowercase(bool)
    capitalized(bool)
    strip(bool)
    replace_newlines(bool)
    returns:
    sttr:the formated text
    raises:
    TypeError:if input is not a string 
    """
    if not isinstance(text,str):
     raise TypeError("the input must be a string")
    if replace_newlines:
      text=text.replace('\n',' ')
    if strip:
     text=text.strip()
    if lowercase:
     text=text.lower()
    if uppercase:
     text=text.upper()
    if capitalized:
     text=text.capitalize()
    return text 
if __name__ == "__main__":
    examples = [
        "   Hello World!   ",
        "hello\nworld",
        123,  # Should trigger TypeError
        "python"
    ]

    for item in examples:
        print(f"Original: {item}")
        try:
            result = format_text(item, capitalize=True)
            print("Formatted:", result)
        except Exception as e:
            print("Error:", e)
        print("-" * 20)

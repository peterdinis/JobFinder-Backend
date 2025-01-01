import os

def validate_file_extension(value):
    isValid = True

    ext = os.path.splitext(value[1])
    valid_extensions = [".pdf"]

    if not ext.lower() in valid_extensions:
        isValid = False

    return isValid
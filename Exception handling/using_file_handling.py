def read_file(filename):
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError as e:
        raise RuntimeError("Failed to read file") from e


try:
    read_file("data.txt")
except RuntimeError as e:
    print(e)

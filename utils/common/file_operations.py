def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    with open(filename,"r") as file:
        return file.read()

print(__name__)
print("Prueba de ruta relativa file_operations.py")

import os

def print_directory_structure(root_dir, indent=0):
    """Imprime la estructura de directorios de manera recursiva.

    Args:
        root_dir (str): El directorio raíz desde el cual comenzar.
        indent (int): La cantidad de espacios para la indentación (para mostrar la jerarquía).
    """
    try:
        # Imprimir el nombre del directorio actual con la indentación adecuada
        print(' ' * indent + os.path.basename(root_dir) + '/')
        
        # Iterar sobre los elementos en el directorio
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            
            if os.path.isdir(item_path):
                # Si el elemento es un directorio, hacer una llamada recursiva
                print_directory_structure(item_path, indent + 4)
            else:
                # Si el elemento es un archivo, imprimir su nombre con la indentación adecuada
                print(' ' * (indent + 4) + item)
    except PermissionError:
        # Manejar el caso en el que el script no tiene permisos para acceder a algunos directorios
        print(' ' * indent + '[Permiso Denegado]')

if __name__ == "__main__":
    # Cambia la ruta a la ubicación de tu proyecto
    project_root = 'C:/Users/ruben/Desktop/MultimodalAI/Multimodal-AI-Application-with-LangChain-the-OpenAI-API/app'
    print_directory_structure(project_root)

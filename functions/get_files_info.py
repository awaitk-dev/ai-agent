import os
from google import genai
from google.genai import types


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = ""
    try:
        full_path = os.path.join(working_directory, directory)
        abs_full_path = os.path.abspath(full_path)
        abs_work_path = os.path.abspath(working_directory)
        if not abs_full_path.startswith(abs_work_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        check_is_dir = os.path.isdir(abs_full_path)
        if not check_is_dir:
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(abs_full_path)
        file_sizes = []
        for item in contents:
            item_path = os.path.join(abs_full_path, item)
            file_sizes.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
        return "\n".join(file_sizes)


    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
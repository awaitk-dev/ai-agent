import os
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_path = os.path.abspath(working_directory)
    if not abs_full_path.startswith(abs_work_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        CHAR_LIMIT = 10000
        with open(abs_full_path, "r") as f:
            content = f.read(CHAR_LIMIT)
            if os.path.getsize(abs_full_path) > CHAR_LIMIT:
                content += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )
        return content
    except Exception as e:
        return f"Error reading from file: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a specified file within the working directory, up to 10,000 characters. Prevents access to files outside the working directory and handles errors for missing or invalid files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to retrieve the content of.",
            ),
        },
    ),
)
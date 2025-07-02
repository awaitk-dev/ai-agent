import os

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
import os

def write_file(working_directory, file_path, content):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_path = os.path.abspath(working_directory)
    if not abs_full_path.startswith(abs_work_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_full_path):
            os.makedirs(os.path.dirname(abs_full_path), exist_ok=True)
        with open(abs_full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error writing to file: {e}")
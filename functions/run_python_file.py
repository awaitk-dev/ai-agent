import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_path = os.path.abspath(working_directory)
    if not abs_full_path.startswith(abs_work_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        compProcess = subprocess.run(["python", file_path], capture_output=True, timeout=30, cwd=abs_work_path)
        output = []
        if compProcess.stdout:
            output.append(f'STDOUT: {compProcess.stdout.decode()}')
        if compProcess.stderr:
            output.append(f'STDERR: {compProcess.stderr.decode()}')
        if compProcess.returncode != 0:
            output.append(f'Process exited with code {compProcess.returncode}')
        if not output:
            return 'No output produced.'
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
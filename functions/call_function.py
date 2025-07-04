import os
from google import genai
from google.genai import types

from .get_file_content import get_file_content, schema_get_file_content
from .get_files_info import get_files_info, schema_get_files_info
from .run_python_file import run_python_file, schema_run_python_file
from .write_file import write_file, schema_write_file
from config import WORKING_DIR



# List of available functions to give ai agent
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    call_args = function_call_part.args
    call_args["working_directory"] = WORKING_DIR

    if verbose:
        print(f"Calling function: {function_name}({call_args})")
    else:
        print(f" - Calling function: {function_name}")

    func_dict = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    if function_name in func_dict:
        function_result = func_dict[function_name](**call_args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    
    # If function name is invalid, return types.Content that explains the error
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )


from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    # result = get_files_info("calculator", ".")
    # print('Result for current directory:')
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "/bin")
    # print("Result for '\\bin' directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)

    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py':")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py' directory:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat' directory:")
    # print(result)

    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for writing to 'lorem.txt':")
    # print(result)
    # print("")

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for writing to 'pkg/morelorem.txt':")
    # print(result)
    # print("")

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for writing to '/tmp/temp.txt':")
    # print(result)
    # print("")

    result = run_python_file("calculator", "main.py")
    print("Result for running 'main.py':")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for running 'tests.py':")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for running '../main.py':")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running 'nonexistent.py':")
    print(result)
    print("")

if __name__ == "__main__":
    test()
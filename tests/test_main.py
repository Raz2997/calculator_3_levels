import subprocess

def run_command(args):
    result = subprocess.run(["python", "main.py"] + args, capture_output=True, text=True)
    return result.stdout.strip()

def test_cli_add():
    assert "The result of 5.0 add 3.0 is equal to 8.0" in run_command(["5", "3", "add"])

def test_cli_subtract():
    assert "The result of 10.0 subtract 2.0 is equal to 8.0" in run_command(["10", "2", "subtract"])

def test_cli_multiply():
    assert "The result of 4.0 multiply 5.0 is equal to 20.0" in run_command(["4", "5", "multiply"])

def test_cli_divide():
    assert "The result of 20.0 divide 4.0 is equal to 5.0" in run_command(["20", "4", "divide"])

def test_cli_divide_by_zero():
    assert "An error occurred: Cannot divide by zero." in run_command(["1", "0", "divide"])

def test_cli_invalid_operation():
    assert "Unknown operation: unknown" in run_command(["9", "3", "unknown"])

def test_cli_invalid_input():
    assert "Invalid number input: a or 3 is not a valid number." in run_command(["a", "3", "add"])

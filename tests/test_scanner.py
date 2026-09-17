from scanner.scanner import scan_code


def test_hardcoded_secret():
    result = scan_code('password = "demo123"')
    assert result[0]["severity"] == "HIGH"


def test_eval():
    result = scan_code("eval(user_input)")
    assert result[0]["issue"] == "Dangerous eval()"


def test_clean_code():
    assert scan_code("print('Hello')") == []


def test_debug_mode():
    result = scan_code("debug = True")
    assert result[0]["severity"] == "MEDIUM"
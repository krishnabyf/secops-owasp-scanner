def fix_sql_injection(code):
    if "SELECT" in code:
        return code.replace("f\"", "\"").replace("+", ",")
    return code

def apply_fixes(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    fixed_code = fix_sql_injection(code)

    with open(file_path, "w") as f:
        f.write(fixed_code)

    print(f"[+] Fixed: {file_path}")
line=input()
if "import" in line:
    print("Hacker")
    exit(1)
exec(line)
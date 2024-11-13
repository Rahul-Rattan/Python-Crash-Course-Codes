from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text().splitlines()
print(contents)

cath=Path("programming.txt")
cath.write_text("Hello World!")

wath=Path("Alice_in_wonderland.txt")
try:
    fonents=wath.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"File {wath} not found")
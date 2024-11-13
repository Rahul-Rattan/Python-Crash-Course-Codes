from pathlib import Path

path=Path("pi_digits.txt")
contents=path.read_text()
lines=contents.splitlines()
pi=''
for content in lines:
    pi+=content
print(pi)
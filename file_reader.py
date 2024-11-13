from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text().splitlines()
print(contents)
pi=''
for content in contents:
    print(content)
    pi+=content.lstrip()
print(pi)



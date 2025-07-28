from pathlib import Path

for arquivo in Path("dados/entrada").glob("*.txt"):
    print(arquivo.stem)
from pathlib import Path
import shutil

shutil.unpack_archive("arquivos_secretos.zip", "extraidos")

extraidos = Path("extraidos")
for arquivo in extraidos.iterdir():
    print(arquivo.stem)
    
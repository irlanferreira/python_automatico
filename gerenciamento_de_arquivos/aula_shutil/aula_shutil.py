import shutil
from pathlib import Path

# shutil.copy2("arquivinho.txt", "backup/arquivinho_backup.txt")
# shutil.copytree("meus_arquivos", "meus_arquivos_backup", dirs_exist_ok=True)

# shutil.move("meus_arquivos/arquivo_teste.txt", "meus_arquivos/arquivo.txt")

# shutil.rmtree("meus_arquivos_backup")

# shutil.make_archive("meus_arquivos", "zip", "meus_arquivos")

# shutil.unpack_archive("meus_arquivos.zip", "arquivos")

arquivos = Path("arquivos")
arquivos_backup = Path("arquivos_backup")

shutil.copytree(arquivos, arquivos_backup)
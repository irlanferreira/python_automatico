from pathlib import Path
import shutil

imagens = Path("imagens")
backup = Path("backup")

shutil.copytree(imagens, backup)
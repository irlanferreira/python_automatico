from pathlib import Path
import shutil

relatorio = Path("relatorio.txt")
relatorios_antigos = Path("relatorios_antigos")

shutil.move(relatorio, relatorios_antigos/"relatorio_backup.txt")
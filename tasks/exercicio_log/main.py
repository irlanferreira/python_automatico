import pathlib
from datetime import datetime

log_path = pathlib.Path('boot_log.txt')
data = datetime.now()
with open(log_path, 'a', encoding='utf-8') as arquivo:
    log_texto = f"[BOOT] {data.strftime('%d/%m/%Y às %H:%M:%S')}\n"
    arquivo.write(log_texto)
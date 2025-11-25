from pathlib import Path

log_path = Path('log.txt')

try:
    with open(log_path, 'a', encoding='utf-8') as arquivo:
        arquivo.write("Registro Concluído!\n")
except Exception as erro:
    print(erro)
    input()
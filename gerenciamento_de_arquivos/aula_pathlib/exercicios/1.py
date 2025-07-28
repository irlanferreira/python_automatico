from pathlib import Path

entrada = Path("dados/entrada")
saida = Path("dados/saida")
relatorios = Path("relatorios")

entrada.mkdir(parents=True, exist_ok=True)
saida.mkdir(parents=True, exist_ok=True)
relatorios.mkdir(parents=True, exist_ok=True)
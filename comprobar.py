import pathlib
import re
import sys

raiz = pathlib.Path(__file__).parent
fallos = []
for pagina in raiz.glob("*.html"):
    texto = pagina.read_text(encoding="utf-8")
    if "{{" in texto:
        fallos.append(f"{pagina.name}: quedan huecos por rellenar")
    for ruta in re.findall(r'(?:src|href)="(assets/[^"]+)"', texto):
        if not (raiz / ruta).exists():
            fallos.append(f"{pagina.name}: falta {ruta}")
print("\n".join(fallos) or "bien")
sys.exit(1 if fallos else 0)

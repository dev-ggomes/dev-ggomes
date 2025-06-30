#!/usr/bin/env python3
# update_readme.py
import random 
import re
import sys
from pathlib import Path

# Lista de frases 
PHRASES = Path("quotes.txt").read_text(encoding="utf-8").splitlines()

def main():
  readme = Path("README.md")
  if not readme.exists():
    print("README.md não encontrado.", file=sys.stderr)
    sys.exit(1)

  text = readme.read_text(encoding="utf-8")
  new_quote = random.choice(PHRASES)

  # Substitui apenas o conteúdo entre os marcadores
  pattern = re.compile(
    r"(<!-- phrase-start -->\s*)(.*?)(\s*<!-- phrase-end -->)",
    flags=re.DOTALL
  )
  new_text, count = pattern.subn(
    rf"\1{new_quote}\3", text, count=1
  )
  if count == 0:
    print("Marcadores não encontrados no README.md.", file=sys.stderr)
    sys.exit(1)

  readme.write_text(new_text, encoding="utf-8")
  print(f"✔️ Atualizado para: “{new_quote}”")

if __name__ == "__main__":
  main()

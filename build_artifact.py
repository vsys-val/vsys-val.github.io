#!/usr/bin/env python3
"""Gera uma versão self-contained de index.html (imagens em data: URI).

Uso: python3 build_artifact.py
Saída: ../artifact.html  — página sem <html>/<head>/<body>, para publicar como Artifact.
O site do GitHub Pages usa index.html normal; este arquivo é só a cópia embutida.
"""
import base64
import mimetypes
import pathlib
import re

HERE = pathlib.Path(__file__).parent
src = (HERE / "index.html").read_text(encoding="utf-8")


def inline_assets(html: str) -> str:
    def repl(m):
        path = m.group(2)
        f = HERE / path
        if not f.exists():
            return m.group(0)
        mime = mimetypes.guess_type(str(f))[0] or "application/octet-stream"
        b64 = base64.b64encode(f.read_bytes()).decode("ascii")
        return f'{m.group(1)}="data:{mime};base64,{b64}"'
    return re.sub(r'(src|href)="(assets/[^"]+)"', repl, html)


src = inline_assets(src)

head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", src, re.S).group(1)

# o wrapper do Artifact já fornece charset e viewport
head = re.sub(r'\s*<meta charset="UTF-8">', "", head)
head = re.sub(r'\s*<meta name="viewport"[^>]*>', "", head)

out = head.strip() + "\n\n" + body.strip() + "\n"
target = HERE.parent / "artifact.html"
target.write_text(out, encoding="utf-8")
print(f"escrito {target} — {len(out)/1024:.0f} KB")

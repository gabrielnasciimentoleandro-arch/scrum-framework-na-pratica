#!/usr/bin/env python3
"""Valida estrutura, conteúdo, links e artefatos do projeto."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "index.html",
    "LICENSE",
    "CONTRIBUTING.md",
    "ENTREGA_DIO.md",
    "Makefile",
    "requirements.txt",
    "docs/GUIA_COMPLETO.md",
    "docs/CLASSIFICACAO_DOS_CARDS.md",
    "docs/PILARES_E_VALORES.md",
    "docs/APLICACAO_PRATICA.md",
    "docs/ANTI_PADROES.md",
    "docs/QUIZ.md",
    "docs/REFERENCIAS.md",
    "assets/capa.svg",
    "assets/capa-documento.png",
    "assets/mapa-framework.svg",
    "assets/pilares-valores.svg",
    "assets/ciclo-sprint.svg",
    "entrega/Guia_Framework_Scrum.docx",
    "entrega/Guia_Framework_Scrum.pdf",
    "scripts/generate_deliverables.py",
    "scripts/validate_project.py",
    "tests/test_project.py",
]

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDERS = [
    r"\bTODO:",
    r"\bFIXME:",
    r"SEU[_ ]NOME",
    r"COLE[_ ]AQUI",
    r"Lorem ipsum",
]


class ProjectHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.external_scripts: list[str] = []
        self.external_styles: list[str] = []
        self.title_depth = 0
        self.title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if element_id := values.get("id"):
            self.ids.add(element_id)
        for attribute in ("href", "src"):
            if target := values.get(attribute):
                self.references.append((attribute, target))
        if tag == "script" and values.get("src"):
            self.external_scripts.append(values["src"] or "")
        if tag == "link" and values.get("rel") == "stylesheet":
            self.external_styles.append(values.get("href") or "")
        if tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"arquivo vazio: {relative}")


def validate_markdown_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = unquote(target.split("#", 1)[0])
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"link sai do repositório em {path.relative_to(ROOT)}: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"link local quebrado em {path.relative_to(ROOT)}: {target}"
                )


def validate_html(errors: list[str]) -> None:
    path = ROOT / "index.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    parser = ProjectHTMLParser()
    parser.feed(text)

    if "Framework Scrum na Prática" not in "".join(parser.title_text):
        errors.append("título HTML inesperado")
    if parser.external_scripts or parser.external_styles:
        errors.append("HTML depende de script ou folha de estilo externa")
    for expected_id in (
        "inicio",
        "fundamentos",
        "framework",
        "pratica",
        "classificacao",
        "quiz",
        "fontes",
    ):
        if expected_id not in parser.ids:
            errors.append(f"seção HTML ausente: #{expected_id}")
    for attribute, target in parser.references:
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            if target[1:] and target[1:] not in parser.ids:
                errors.append(f"âncora HTML inexistente: {target}")
            continue
        clean = unquote(target.split("#", 1)[0])
        if clean and not (ROOT / clean).exists():
            errors.append(f"recurso HTML local ausente ({attribute}): {target}")
    if len(re.findall(r"\{ q: ", text)) != 8:
        errors.append("quiz interativo não contém exatamente 8 perguntas")
    if "localhost" in text and "http://localhost:8000" not in text:
        errors.append("referência inesperada a localhost no HTML")


def validate_content(errors: list[str]) -> None:
    combined = "\n".join(path.read_text(encoding="utf-8") for path in markdown_files())
    for pattern in PLACEHOLDERS:
        if re.search(pattern, combined):
            errors.append(f"placeholder encontrado: {pattern}")

    guide = (ROOT / "docs/GUIA_COMPLETO.md").read_text(encoding="utf-8")
    required_terms = [
        "Transparência",
        "Inspeção",
        "Adaptação",
        "Compromisso",
        "Foco",
        "Abertura",
        "Respeito",
        "Coragem",
        "Product Owner",
        "Scrum Master",
        "Developers",
        "Sprint Planning",
        "Daily Scrum",
        "Sprint Review",
        "Sprint Retrospective",
        "Product Backlog",
        "Sprint Backlog",
        "Incremento",
        "Meta do Produto",
        "Meta da Sprint",
        "Definition of Done",
    ]
    for term in required_terms:
        if term not in guide:
            errors.append(f"conceito essencial ausente do guia: {term}")
    if len(guide.split()) < 2500:
        errors.append("guia principal parece curto demais")
    if "Não reproduz os slides" not in guide:
        errors.append("declaração de originalidade ausente no guia")
    if "2020-Scrum-Guide-PortugueseBR-3.0.pdf" not in guide:
        errors.append("referência brasileira oficial ausente")


def validate_svg_and_png(errors: list[str]) -> None:
    for path in sorted((ROOT / "assets").glob("*.svg")):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"SVG inválido em {path.relative_to(ROOT)}: {exc}")
            continue
        if not root.tag.endswith("svg"):
            errors.append(f"raiz inesperada no SVG: {path.relative_to(ROOT)}")
        if root.find("{http://www.w3.org/2000/svg}title") is None:
            errors.append(f"SVG sem título acessível: {path.relative_to(ROOT)}")
    png = ROOT / "assets/capa-documento.png"
    if png.exists() and not png.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append("capa PNG inválida")


def validate_docx(errors: list[str]) -> None:
    path = ROOT / "entrega/Guia_Framework_Scrum.docx"
    if not path.exists():
        return
    try:
        with zipfile.ZipFile(path) as archive:
            if bad := archive.testzip():
                errors.append(f"DOCX corrompido em: {bad}")
            names = set(archive.namelist())
            for expected in (
                "[Content_Types].xml",
                "word/document.xml",
                "docProps/core.xml",
            ):
                if expected not in names:
                    errors.append(f"DOCX sem componente: {expected}")
            xml = archive.read("word/document.xml").decode("utf-8")
            for phrase in (
                "Framework Scrum",
                "EcoCiclo",
                "Definition of Done",
                "Referências",
            ):
                if phrase.casefold() not in xml.casefold():
                    errors.append(f"DOCX não contém: {phrase}")
    except (zipfile.BadZipFile, KeyError) as exc:
        errors.append(f"DOCX inválido: {exc}")


def validate_pdf(errors: list[str]) -> None:
    path = ROOT / "entrega/Guia_Framework_Scrum.pdf"
    if not path.exists():
        return
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        errors.append("PDF sem cabeçalho válido")
    if b"%%EOF" not in data[-2048:]:
        errors.append("PDF sem marcador final")
    pages = len(re.findall(rb"/Type\s*/Page(?!s)", data))
    if pages < 7:
        errors.append(f"PDF possui poucas páginas ({pages})")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_markdown_links(errors)
    validate_html(errors)
    validate_content(errors)
    validate_svg_and_png(errors)
    validate_docx(errors)
    validate_pdf(errors)
    if errors:
        print("VALIDAÇÃO: FALHOU")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    print("VALIDAÇÃO: OK")
    print(f"  ✓ {len(REQUIRED)} arquivos obrigatórios")
    print(f"  ✓ {len(markdown_files())} documentos Markdown")
    print("  ✓ HTML, links locais, conceitos, SVG, PNG, DOCX e PDF")
    return 0


if __name__ == "__main__":
    sys.exit(main())

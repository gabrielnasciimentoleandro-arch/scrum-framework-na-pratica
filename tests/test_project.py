import subprocess
import sys
import unittest
from pathlib import Path

from scripts.generate_deliverables import SOURCE, find_font, iter_inline, parse_markdown

ROOT = Path(__file__).resolve().parents[1]


class ScrumFrameworkProjectTest(unittest.TestCase):
    def test_repository_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_project.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_guide_parser_supports_tables_and_quotes(self):
        blocks = parse_markdown(SOURCE)
        headings = [block.text for block in blocks if block.kind == "heading"]
        tables = [block for block in blocks if block.kind == "table"]
        quotes = [block for block in blocks if block.kind == "quote"]

        self.assertEqual(blocks[0].text, "Resumo")
        self.assertIn("4. Scrum Team e responsabilidades formais", headings)
        self.assertIn("10. Síntese", headings)
        self.assertGreaterEqual(len(tables), 3)
        self.assertGreaterEqual(len(quotes), 1)

    def test_inline_parser_formats_link_bold_and_code(self):
        tokens = list(
            iter_inline("**Scrum** usa `Sprint` e [guia](https://scrumguides.org/).")
        )
        kinds = [kind for kind, _, _ in tokens]
        self.assertIn("bold", kinds)
        self.assertIn("code", kinds)
        self.assertIn("link", kinds)

    def test_portable_fonts_are_available(self):
        self.assertTrue(find_font("Vera.ttf").is_file())
        self.assertTrue(find_font("VeraBd.ttf").is_file())

    def test_interactive_quiz_has_eight_questions(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertEqual(html.count("{ q: "), 8)
        self.assertIn('id="quizForm"', html)
        self.assertIn("addEventListener", html)

    def test_final_files_have_expected_signatures(self):
        pdf = ROOT / "entrega" / "Guia_Framework_Scrum.pdf"
        docx = ROOT / "entrega" / "Guia_Framework_Scrum.docx"
        self.assertTrue(pdf.read_bytes().startswith(b"%PDF-"))
        self.assertTrue(docx.read_bytes().startswith(b"PK"))


if __name__ == "__main__":
    unittest.main()

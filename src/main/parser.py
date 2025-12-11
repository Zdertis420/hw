from pathlib import Path
import re


class Parser:
    def __init__(self, path: str):
        self.path = Path(path)
        self.SINGLE_LINE_RE = re.compile(r"--.*?$", re.MULTILINE)
        self.MULTI_LINE_RE = re.compile(r"/\+.*?\+/", re.DOTALL)

    def read(self):
        if not self.path.exists():
            raise FileNotFoundError(f"File not found: {self.path}")

        return self.path.read_text(encoding="utf-8")

    def remove_comments(self, text: str) -> str:
        no_multi = re.sub(self.MULTI_LINE_RE, "", text)

        no_single = re.sub(self.SINGLE_LINE_RE, "", no_multi)

        return no_single

    def load_clean(self) -> str:
        raw = self.read()
        cleaned = self.remove_comments(raw)
        return cleaned.strip()

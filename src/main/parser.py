from pathlib import Path


class Parser:
    def __init__(self, path: str):
        self.path = Path(path)

    def read(self):
        if not self.path.exists():
            raise FileNotFoundError(f"File not found: {self.path}")

        return self.path.read_text(encoding="utf-8")

import csv
import os
from typing import Dict, List


class TranslationManager:
    """Manages loading and retrieving translations from a CSV file.

    The CSV should have a header where the first column is the translation key
    and the subsequent columns are language codes (e.g., 'en', 'es').
    """

    def __init__(self, csv_path: str = None, default_lang: str = "en") -> None:
        if csv_path is None:
            # Default to translations.csv in the same directory as this file
            csv_path = os.path.join(os.path.dirname(__file__), "translations.csv")
            # If not found, try the test path for backward compatibility/demo
            if not os.path.isfile(csv_path):
                test_path = os.path.join(os.path.dirname(__file__), "test", "test.csv")
                if os.path.isfile(test_path):
                    csv_path = test_path

        self.csv_path = csv_path
        self.default_lang = default_lang
        self.active_lang = default_lang
        self.translations: Dict[str, Dict[str, str]] = {}
        self.available_languages: List[str] = []
        self._load_csv()

    def _load_csv(self) -> None:
        if not os.path.isfile(self.csv_path):
            return

        with open(self.csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames:
                # First column is 'key', rest are languages
                self.available_languages = reader.fieldnames[1:]
                key_field = reader.fieldnames[0]
                for row in reader:
                    key = row.pop(key_field)
                    if key:
                        # Remove empty columns
                        self.translations[key] = {
                            lang: txt for lang, txt in row.items() if txt
                        }

    def set_language(self, lang: str) -> None:
        """Change the active language."""
        self.active_lang = lang

    def get_available_languages(self) -> List[str]:
        """Return a list of language codes available in the CSV."""
        return self.available_languages

    def translate(self, key: str) -> str:
        """Return the translation for key in the active language.
        Falls back to default language then the key itself.
        """
        entry = self.translations.get(key, {})
        return entry.get(self.active_lang) or entry.get(self.default_lang) or key


# Singleton instances for convenience
translator = TranslationManager()


def t(key: str) -> str:
    """Shortcut for translator.translate(key)."""
    return translator.translate(key)


def set_language(lang: str) -> None:
    """Set the active language globally."""
    translator.set_language(lang)


def get_available_languages() -> List[str]:
    """Get all available language codes."""
    return translator.get_available_languages()

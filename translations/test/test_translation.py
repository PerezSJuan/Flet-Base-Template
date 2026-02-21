import unittest

from translations.translations import (
    set_language,
    t,
    get_available_languages,
)


class TestTranslationManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure the CSV path is correct (already set in module)
        pass

    def test_default_language(self):
        # Assuming CSV contains key 'greeting' with English and Spanish values
        self.assertEqual(t("greeting"), "Hello")

    def test_set_language(self):
        set_language("es")
        self.assertEqual(t("greeting"), "Hola")
        # Reset to default for other tests
        set_language("en")

    def test_missing_key_fallback(self):
        # If key not present, should return the key itself
        self.assertEqual(t("nonexistent_key"), "nonexistent_key")

    def test_get_available_languages(self):
        langs = get_available_languages()
        self.assertIn("en", langs)
        self.assertIn("es", langs)
        self.assertEqual(len(langs), 2)


if __name__ == "__main__":
    unittest.main()

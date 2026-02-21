# Mapping of language codes to their full names
LANGUAGE_NAMES = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
    "ru": "Русский",
    "zh": "中文",
    "ja": "日本語",
    "ko": "한국어",
    "ar": "العربية",
    "nl": "Nederlands",
    "pl": "Polski",
    "tr": "Türkçe",
    "sv": "Svenska",
    "no": "Norsk",
    "da": "Dansk",
    "fi": "Suomi",
    "cs": "Čeština",
    "hu": "Magyar",
    "ro": "Română",
    "th": "ไทย",
    "vi": "Tiếng Việt",
    "id": "Bahasa Indonesia",
    "el": "Ελληνικά",
    "he": "עברית",
    "hi": "हिन्दी",
}


def get_language_name(code: str) -> str:
    """Returns the full name of a language given its code.
    Falls back to the code itself if not found.
    """
    return LANGUAGE_NAMES.get(code.lower(), code)


def get_language_code(name: str) -> str:
    """Returns the code of a language given its name.
    Falls back to the name itself if not found.
    """
    # Buscamos en los valores del diccionario ignorando mayúsculas/minúsculas
    name_lower = name.lower().strip()
    for code, lang_name in LANGUAGE_NAMES.items():
        if lang_name.lower() == name_lower:
            return code
    return name

from . import zh, en

LANG_MAP = {
    "zh": zh.TEXT,
    "en": en.TEXT
}

def t(lang: str, key: str, **kwargs):
    template = LANG_MAP.get(lang, en.TEXT).get(key, key)
    return template.format(**kwargs)
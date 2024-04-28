NUM_LAYERS = 12
NUM_HEAD = 16
N_DIM = 1024
PREFIX_MODE = 1
NUM_QUANTIZERS = 8
SAMPLE_RATE = 24000

lang2token = {
    'zh': "[ZH]",
    'ja': "[JA]",
    "en": "[EN]",
    'mix': "",
    'ru': "[RU]"
}

lang2code = {
    'zh': 0,
    'ja': 1,
    "en": 2,
    "ru": 3
}

token2lang = {
    '[ZH]': "zh",
    '[JA]': "ja",
    "[EN]": "en",
    "": "mix",
    '[RU]': "ru"
}

code2lang = {
    0: 'zh',
    1: 'ja',
    2: "en",
    3: "ru"
}

langdropdown2token = {
    'English': "[EN]",
    '中文': "[ZH]",
    '日本語': "[JA]",
    'Mix': "",
    'Russian': "[RU]"
}
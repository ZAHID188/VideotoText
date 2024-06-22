import argostranslate.package
import argostranslate.translate


def jap_to_en(jap):
    from_code = "ja"
    to_code = "en"
    translatedText = argostranslate.translate.translate(jap, from_code, to_code)
    return translatedText
def jap_to_zh(jap):
    from_code = "ja"
    to_code = "zh"
    translatedText = argostranslate.translate.translate(jap, from_code, to_code)
    return translatedText
def translation(jap):
    en=jap_to_en(jap)
    zh=jap_to_zh(jap)
    return en,zh
# x=translation()
# print(x[0])
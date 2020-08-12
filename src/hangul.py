#! .venv/bin/python3
# coding: utf-8

def __make_translit_dicts():
    YALE_CHOSEONG = "k kk n t tt l m p pp s ss . c cc ch kh th ph h"
    YALE_JUNGSEONG = "a ay ya yay e ey ye yey o wa way oy yo wu we wey wi yu u uy i"
    YALE_JONGSEONG = ". k kk ks n nc nh t l lk lm lp ls lth lph lh m p ps s ss ng c ch kh th ph h"
    IPA_CHOSEONG = "k k͈ n t t͈ l m p p͈ s s͈ . tɕ tɕ͈ tɕʰ kʰ tʰ pʰ h"
    IPA_JUNGSEONG = "a æ ja jæ ʌ ɛ jʌ jɛ o wa wæ wø jo u wʌ wɛ wʏ ju ɯ ɰi i"
    IPA_JONGSEONG = ". k k͈ ks n ntɕ nh t l lk lm lp ls ltʰ lpʰ lh m p ps s s͈ ŋ tɕ tɕʰ kʰ tʰ pʰ h"
    HAN_JAMO = "ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ"
    YALE_JAMO = YALE_CHOSEONG + " " + YALE_JUNGSEONG
    IPA_JAMO = IPA_CHOSEONG + " " + IPA_JUNGSEONG

    def make_syllables(chos, jungs, jongs):
        return [
            f"{cho}{jung}{jong}".replace('.', '')
            for cho in chos.split()
            for jung in jungs.split()
            for jong in jongs.split()
        ]

    HAN_SYLLABLES = [
        *map(chr, range(ord('가'), ord('힣') + 1))] + HAN_JAMO.split()
    YALE_SYLLABLES = make_syllables(
        YALE_CHOSEONG, YALE_JUNGSEONG, YALE_JONGSEONG) + YALE_JAMO.split()
    IPA_SYLLABLES = make_syllables(IPA_CHOSEONG, IPA_JUNGSEONG, IPA_JONGSEONG) + IPA_JAMO.split()

    return (
        dict(zip(HAN_SYLLABLES, YALE_SYLLABLES)),
        dict(zip(HAN_SYLLABLES, IPA_SYLLABLES)),
    )


LOMACA, PHONOLOGY = __make_translit_dicts()


def __transliterate(hangul_word, translit_dict):
    return ".".join(translit_dict.get(char, char) for char in hangul_word)


def yale(hangul_word):
    return __transliterate(hangul_word, LOMACA)


def ipa(hangul_word):
    return __transliterate(hangul_word, PHONOLOGY)

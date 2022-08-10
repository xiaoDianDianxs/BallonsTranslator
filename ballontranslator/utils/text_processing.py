from typing import List, Tuple

CHSEG = None

def seg_to_chars(text: str) -> List[str]:
    text = text.replace('\n', '')
    return [c for c in text]

def seg_ch(text: str) -> List[str]:
    text = text.replace('\n', '')
    global CHSEG
    if CHSEG is None:
        import pkuseg
        CHSEG = pkuseg.pkuseg()

    return CHSEG.cut(text)

def seg_eng(text: str) -> List[str]:
    text = text.replace('  ', ' ').replace(' .', '.').replace('\n', ' ')
    processed_text = ''

    # dumb way to insure spaces between words
    text_len = len(text)
    for ii, c in enumerate(text):
        if c in ['.', '?', '!'] and ii < text_len - 1:
            next_c = text[ii + 1]
            if next_c.isalpha() or next_c.isnumeric():
                processed_text += c + ' '
            else:
                processed_text += c
        else:
            processed_text += c

    return processed_text.split(' ')

def seg_text(text: str, lang: str) -> Tuple[List, str]:
    delimiter = ''
    if lang in ['简体中文', '繁体中文']:
        words = seg_ch(text)    
    elif lang in ['日本語', '한국어']:
        words = seg_to_chars(text)
    else:
        words = seg_eng(text)
        delimiter = ' '
    return words, delimiter

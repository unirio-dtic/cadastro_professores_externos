from unicodedata import normalize


def remover_acentos(txt, codif='utf-8'):
    if isinstance(txt, unicode):
        txt = txt.encode('utf-8')
    return normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore')
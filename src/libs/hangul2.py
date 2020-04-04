HANGUL_BASE = ord('가')


def char_range(fst, lst, by=1):
    return [chr(x) for x in range(ord(fst), ord(lst) + 1, by)]


def han_position(c):
    return ord(c) - HANGUL_BASE


def get_pos_chojungjong(h):
    cho, jungjong = divmod(han_position(h), 588)
    jung, jong = divmod(jungjong, 28)
    return (cho, jung, jong)


def mk_dict(s):
    return dict(enumerate(s.replace('.', '').split(' ')))


YALE_CHO = mk_dict(
    "k, kk, n, t, tt, l, m, p, pp, s, ss, ., c, cc, ch, kh, th, ph, h")
YALE_JUNG = mk_dict(
    "a, ay, ya, yay, e, ey, ye, yey, o, wa, way, oy, yo, wu, we, wey, wi, yu, u, uy, i")
YALE_JONG = mk_dict(
    "., k, kk, ks, n, nc, nh, t, l, lk, lm, lp, ls, lth, lph, lh, m, p, ps, s, ss, ng, c, ch, kh, th, ph, h")


def get_yale_chojungjong(h):
    cho, jung, jong = get_pos_chojungjong(h)
    return YALE_CHO[cho], YALE_JUNG[jung], YALE_JONG[jong]

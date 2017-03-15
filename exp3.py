def cohensutherland(left, top, right, bottom, x1, y1, x2, y2):
    LEFT, RIGHT, LOWER, UPPER = 1, 2, 4, 8

    def _getclip(xa, ya):
        p = 0
        if xa < left:
            p = LEFT
        elif xa > right:
            p = RIGHT
        if ya < top:
            p |= LOWER
        elif ya > bottom:
            p |= UPPER
        return p

    k1 = _getclip(x1, y1)
    k2 = _getclip(x2, y2)
    while (k1 | k2) != 0:
        if (k1 & k2) != 0:
            return None, None, None, None
        opt = k1 or k2
        if opt & UPPER:
            x = x1 + (x2 - x1) * (1.0 * (bottom - y1)) / (y2 - y1)
            y = bottom
        elif opt & LOWER:
            x = x1 + (x2 - x1) * (1.0 * (top - y1)) / (y2 - y1)
            y = top
        elif opt & RIGHT:
            y = y1 + (y2 - y1) * (1.0 * (right - x1)) / (x2 - x1)
            x = right
        elif opt & LEFT:
            y = y1 + (y2 - y1) * (1.0 * (left - x1)) / (x2 - x1)
            x = left
        else:
            raise RuntimeError("invalid clipping state")

        if opt == k1:
            x1, y1 = x, y
            k1 = _getclip(x1, y1)
        else:
            x2, y2 = x, y
            k2 = _getclip(x2, y2)
    return x1, y1, x2, y2


def liangbarsky(left, top, right, bottom, x1, y1, x2, y2):
    dx = x2 - x1 * 1.0
    dy = y2 - y1 * 1.0
    dt0, dt1 = 0.0, 1.0
    xx1 = x1
    yy1 = y1

    checks = ((-dx, x1 - left),
              (dx, right - x1),
              (-dy, y1 - top),
              (dy, bottom - y1))

    for p, q in checks:
        if p == 0 and q < 0:
            return None, None, None, None
        if p != 0:
            dt = q / (p * 1.0)
            if p < 0:
                if dt > dt1:
                    return None, None, None, None
                dt0 = max(dt0, dt)
            else:
                if dt < dt0:
                    return None, None, None, None
                dt1 = min(dt1, dt)
    if dt0 > 0:
        x1 += dt0 * dx
        y1 += dt0 * dy
    if dt1 < 1:
        x2 = xx1 + dt1 * dx
        y2 = yy1 + dt1 * dy
    return x1, y1, x2, y2


clipline = lambda l, t, r, b, x1, y1, x2, y2, method = liangbarsky: \
    method(l, t, r, b, x1, y1, x2, y2)
Contact GitHub 

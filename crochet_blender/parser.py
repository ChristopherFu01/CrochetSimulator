def parse_pattern(text):
    tokens = [t.strip() for t in text.split(",")]
    pattern = []
    for tok in tokens:
        if "*" in tok:
            n, stitch = tok.split("*")
            pattern.extend([stitch] * int(n))
        else:
            pattern.append(tok)
    return pattern
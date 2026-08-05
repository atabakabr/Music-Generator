def generate_progression(grammar, start_symbol='S', length=8):
    seq = [start_symbol]
    
    while any(grammar.is_non_terminal(sym) for sym in seq):
        new_seq = []
        for sym in seq:
            if grammar.is_non_terminal(sym):
                chosen = grammar.choose_rule(sym)
                new_seq.extend(chosen)
            else:
                new_seq.append(sym)
        seq = new_seq
        if len(seq) >= length * 5:
            break

    while len(seq) < length:
        extra = generate_progression(grammar, start_symbol, length - len(seq))
        seq.extend(extra)
    
    return seq[:length]

from grammar import Grammar
from progression import generate_progression

def parse_key(key_str):
    """'C Major' -> ('C', 'Major')"""
    parts = key_str.strip().split()
    tonic = parts[0]
    mode = parts[1].capitalize()
    return tonic, mode

def degree_to_chord(degree, tonic, mode='Major'):
    chromatic = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    major_intervals = [0, 2, 4, 5, 7, 9, 11]
    minor_intervals = [0, 2, 3, 5, 7, 8, 10]

    base_degree = degree
    suffix = ''
    if '7' in degree:
        base_degree = degree.replace('7','')
        suffix = '7'
    if 'dis' in degree:
        base_degree = degree.replace('dis','')
        suffix = 'dim'
    elif 'dim' in degree:
        base_degree = degree.replace('dim','')
        suffix = 'dim'

    deg_map = {'I':0,'II':1,'III':2,'IV':3,'V':4,'VI':5,'VII':6,
               'i':0,'ii':1,'iii':2,'iv':3,'v':4,'vi':5,'vii':6}
    chord_types_major = ['', 'm', 'm', '', '', 'm', 'dim']
    chord_types_minor = ['m', 'dim', '', 'm', 'm', '', 'dim']

    if mode == 'Major':
        intervals = major_intervals
        types = chord_types_major
    else:
        intervals = minor_intervals
        types = chord_types_minor

    tonic_idx = chromatic.index(tonic) if tonic in chromatic else 0
    deg_idx = deg_map.get(base_degree, 0)
    interval = intervals[deg_idx]
    root = chromatic[(tonic_idx + interval) % 12]

    if suffix == '7':
        return root + types[deg_idx] + '7'
    elif suffix == 'dim':
        return root + 'dim'
    else:
        return root + types[deg_idx]

def chord_to_notes(chord_name):

    chromatic = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    root = chord_name[0]
    if len(chord_name) > 1 and chord_name[1] in ('#','b'):
        root = chord_name[:2]
        qual = chord_name[2:]
    else:
        qual = chord_name[1:]

    if root not in chromatic:
        return ['C4','E4','G4']

    root_idx = chromatic.index(root)
    intervals = [0, 4, 7]
    if qual == '' or qual == 'M':
        pass
    elif qual == 'm':
        intervals = [0, 3, 7]
    elif qual == 'dim':
        intervals = [0, 3, 6]
    elif '7' in qual:
        base_qual = qual.replace('7','')
        if base_qual == '' or base_qual == 'M':
            intervals = [0, 4, 7, 10]
        elif base_qual == 'm':
            intervals = [0, 3, 7, 10]
        else:
            intervals = [0, 4, 7, 10]
    else:
        intervals = [0, 4, 7]

    notes = []
    for i in intervals:
        note = chromatic[(root_idx + i) % 12]
        notes.append(f"{note}4")
    return notes

def generate_melody_measure(chord_name, rhythm_pattern):
    notes = chord_to_notes(chord_name)
    melody = []
    for i, dur in enumerate(rhythm_pattern):
        melody.append(notes[i % len(notes)])
    return melody

def generate_harmony(key="C Major", measures=8, rhythm=None, grammar_file="grammar/grammar_major.txt"):
    """
    input:
        key: ...
        measures: ...
        rhythm: ...
    output:
        dict : "progression" and "melody"
    """
    if rhythm is None:
        # default
        rhythm = [[1,1,1,1] for _ in range(measures)]

    g = Grammar()
    g.load(grammar_file)

    tonic, mode = parse_key(key)

    prog_raw = generate_progression(g, 'S', measures + 1)
    prog_degrees = [sym for sym in prog_raw if sym != 'ana']
    prog_degrees = prog_degrees[:measures]

    while len(prog_degrees) < measures:
        # temp
        extra = generate_progression(g, 'S', measures - len(prog_degrees))
        extra_clean = [sym for sym in extra if sym != 'ana']
        prog_degrees.extend(extra_clean)
    prog_degrees = prog_degrees[:measures]

    progression = [degree_to_chord(deg, tonic, mode) for deg in prog_degrees]

    melody = []
    for i in range(measures):
        chord = progression[i]
        r = rhythm[i] if i < len(rhythm) else [1,1,1,1]
        measure_melody = generate_melody_measure(chord, r)
        melody.append(measure_melody)

    return {
        "progression": progression,
        "melody": melody
    }


# test

if __name__ == "__main__":
    test_rhythm = [
        [1, 0.5, 0.5, 2],
        [1, 1, 1, 1],
        [0.5, 0.5, 1, 2],
        [2, 1, 1]
    ]
    res = generate_harmony("C Major", 4, test_rhythm)
    print(res)

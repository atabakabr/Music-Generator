def degree_to_chord(degree, tonic, mode='Major'):
    chromatic = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    
    major_intervals = [0, 2, 4, 5, 7, 9, 11]
    minor_intervals = [0, 2, 3, 5, 7, 8, 10]
    
    deg_map = {'I':0,'II':1,'III':2,'IV':3,'V':4,'VI':5,'VII':6,
               'i':0,'ii':1,'iii':2,'iv':3,'v':4,'vi':5,'vii':6}

    chord_types_major = ['', 'm', 'm', '', '', 'm', 'dim']
    chord_types_minor = ['m', 'dim', '', 'm', 'm', '', '']
    
    if mode == 'Major':
        intervals = major_intervals
        types = chord_types_major
    else:
        intervals = minor_intervals
        types = chord_types_minor
    
    tonic_idx = chromatic.index(tonic) if tonic in chromatic else 0
    deg_idx = deg_map.get(degree, 0)
    interval = intervals[deg_idx]
    root = chromatic[(tonic_idx + interval) % 12]
    chord_type = types[deg_idx]
    
    return root + chord_type

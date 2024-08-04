from music21 import note, chord, scale

# Superclass representing a musical element
class MusicalElement:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Subclass representing a musical note
class Note(MusicalElement):
    def __init__(self, pitch):
        super().__init__(pitch)
        self.note = note.Note(pitch)

    def transpose(self, semitones):
        """Transpose the note by a given number of semitones."""
        self.note.transpose(semitones, inPlace=True)

    def __str__(self):
        return f"Note: {self.note.nameWithOctave}"

# Subclass representing a musical chord
class Chord(MusicalElement):
    def __init__(self, name, pitches):
        super().__init__(name)
        self.chord = chord.Chord(pitches)

    def add_note(self, pitch):
        """Add a note to the chord."""
        self.chord.add(note.Note(pitch))

    def remove_note(self, pitch):
        """Remove a note from the chord."""
        self.chord.remove(note.Note(pitch))

    def transpose_diatonic(self, semitones):
        """
        Transpose the chord diatonically (by semitones).
        
        Parameters:
        - semitones (int): Number of semitones to transpose the chord by.
        """
        self.chord.transpose(semitones, inPlace=True)

    def transpose_harmonic(self, interval):
        """
        Transpose the chord harmonically (by interval).
        
        Parameters:
        - interval (str): Interval to transpose the chord by (e.g., 'P5', 'M3').
        """
        self.chord.transpose(interval, inPlace=True)

    def __str__(self):
        return f"Chord: {' '.join(n.nameWithOctave for n in self.chord.notes)}"

# Subclass representing a musical scale
class Scale(MusicalElement):
    def __init__(self, name, tonic, scale_type='major'):
        super().__init__(name)
        if scale_type == 'major':
            self.scale = scale.MajorScale(tonic)
        elif scale_type == 'minor':
            self.scale = scale.MinorScale(tonic)
        else:
            raise ValueError('Unsupported scale type')

    def get_pitches(self):
        """Get the pitches of the scale."""
        return [str(p) for p in self.scale.pitches]

    def __str__(self):
        return f"{self.name} Scale: {' '.join(self.get_pitches())}"

# Subclass representing an instrument
class Instrument(MusicalElement):
    def __init__(self, name):
        super().__init__(name)
        self.elements = []

    def add_element(self, element):
        """Add a musical element (note, chord, or scale) to the instrument."""
        if isinstance(element, MusicalElement):
            self.elements.append(element)
        else:
            raise TypeError('Can only add instances of MusicalElement')

    def __str__(self):
        return f"Instrument: {self.name}\nElements:\n" + '\n'.join(str(e) for e in self.elements)

# Example usage
def main():
    note_c4 = Note('C4')
    print(note_c4)
    note_c4.transpose(2)
    print(note_c4)

    chord_c_major = Chord('C Major', ['C4', 'E4', 'G4'])
    print(chord_c_major)
    chord_c_major.add_note('B4')
    print(chord_c_major)
    chord_c_major.transpose_harmonic('P5')
    print(chord_c_major)

    scale_c_major = Scale('C', 'C')
    print(scale_c_major)
    scale_a_minor = Scale('A', 'A', 'minor')
    print(scale_a_minor)

    guitar = Instrument('Guitar')
    guitar.add_element(note_c4)
    guitar.add_element(chord_c_major)
    guitar.add_element(scale_c_major)
    print(guitar)

if __name__ == "__main__":
    main()

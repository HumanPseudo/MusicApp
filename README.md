# 🎵 Musical Elements Library 🎶

Welcome to the Musical Elements Library! This Python library allows you to create and manipulate musical notes, chords, scales, and instruments using the `music21` library. 🎹🎸🎷

## Features ✨

- **🎵 Notes**: Create and transpose musical notes.
- **🎶 Chords**: Create, modify, and transpose chords.
- **🎼 Scales**: Generate major and minor scales.
- **🎻 Instruments**: Combine musical elements into instruments.

## Installation 📦

Make sure you have `music21` installed:

```bash
pip install music21
```

## Usage 📖

Here’s a quick guide on how to use the library.

### Creating a Note 🎵

You can create a musical note and transpose it:

```python
note_c4 = Note('C4')
print(note_c4)  # Output: Note: C4
note_c4.transpose(2)
print(note_c4)  # Output: Note: D4
```

### Creating a Chord 🎶

You can create a chord, add or remove notes, and transpose it:

```python
chord_c_major = Chord('C Major', ['C4', 'E4', 'G4'])
print(chord_c_major)  # Output: Chord: C4 E4 G4
chord_c_major.add_note('B4')
print(chord_c_major)  # Output: Chord: C4 E4 G4 B4
chord_c_major.transpose_harmonic('P5')
print(chord_c_major)  # Output: Chord: G4 B4 D5 F#5
```

### Creating a Scale 🎼

You can generate a major or minor scale:

```python
scale_c_major = Scale('C', 'C')
print(scale_c_major)  # Output: C Scale: C D E F G A B

scale_a_minor = Scale('A', 'A', 'minor')
print(scale_a_minor)  # Output: A Scale: A B C D E F G
```

### Creating an Instrument 🎻

Combine musical elements into an instrument:

```python
guitar = Instrument('Guitar')
guitar.add_element(note_c4)
guitar.add_element(chord_c_major)
guitar.add_element(scale_c_major)
print(guitar)
# Output:
# Instrument: Guitar
# Elements:
# Note: D4
# Chord: G4 B4 D5 F#5
# C Scale: C D E F G A B
```

## Class Descriptions 📚

### MusicalElement

The superclass representing a musical element.

### Note

A subclass representing a musical note.

- **`__init__(pitch)`**: Initializes a note with the given pitch.
- **`transpose(semitones)`**: Transposes the note by the given number of semitones.

### Chord

A subclass representing a musical chord.

- **`__init__(name, pitches)`**: Initializes a chord with the given name and pitches.
- **`add_note/pitch)`**: Adds a note to the chord.
- **`remove_note/pitch)`**: Removes a note from the chord.
- **`transpose_diatonic(semitones)`**: Transposes the chord diatonically.
- **`transpose_harmonic(interval)`**: Transposes the chord harmonically.

### Scale

A subclass representing a musical scale.

- **`__init__(name, tonic, scale_type='major')`**: Initializes a scale with the given name, tonic, and scale type.
- **`get_pitches()`**: Returns the pitches of the scale.

### Instrument

A subclass representing an instrument.

- **`__init__(name)`**: Initializes an instrument with the given name.
- **`add_element(element)`**: Adds a musical element to the instrument.

## Example Usage 🎬

Check out the example usage in `main()` to see how to create and manipulate musical elements and combine them into an instrument.

```python
def main():
    # Create a note
    note_c4 = Note 'C4')
    print(note_c4)
    note_c4.transpose(2)
    print(note_c4)

    # Create a chord
    chord_c_major = Chord('C Major', ['C4', 'E4', 'G4'])
    print(chord_c_major)
    chord_c_major.add_note 'B4')
    print(chord_c_major)
    chord_c_major.transpose_harmonic 'P5')
    print(chord_c_major)

    # Create scales
    scale_c_major = Scale 'C', 'C')
    print(scale_c_major)
    scale_a_minor = Scale 'A', 'A', 'minor')
    print(scale_a_minor)

    # Create an instrument
    guitar = Instrument 'Guitar')
    guitar.add_element note_c4)
    guitar.add_element chord_c_major)
    guitar.add_element scale_c_major)
    print(guitar)

if __name__ == "__main__":
    main()
```

## Contributing 🤝

Feel free to fork this repository and contribute by submitting pull requests. Let’s make music together! 🎉

## License 📄

This project is licensed under the MIT License.

---

Happy Coding! 🎹
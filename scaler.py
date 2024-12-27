import argparse
import random

# Define scales and modes
SCALES = {
    "major": [2, 2, 1, 2, 2, 2, 1],  # Whole and half step pattern
    "dorian": [2, 1, 2, 2, 2, 1, 2],
    "phrygian": [1, 2, 2, 2, 1, 2, 2],
    "lydian": [2, 2, 2, 1, 2, 2, 1],
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "locrian": [1, 2, 2, 1, 2, 2, 2],
}

# Define key signatures
KEY_SIGNATURES = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "G": ["C", "D", "E", "F#", "G", "A", "B"],
    "D": ["C#", "D", "E", "F#", "G", "A", "B"],
    "A": ["C#", "D", "E", "F#", "G#", "A", "B"],
    "E": ["C#", "D#", "E", "F#", "G#", "A", "B"],
    "B": ["C#", "D#", "E", "F#", "G#", "A#", "B"],
    "F#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "F": ["C", "D", "E", "F", "G", "A", "Bb"],
    "Bb": ["C", "D", "Eb", "F", "G", "A", "Bb"],
    "Eb": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "Ab": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
    "Db": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
    "Gb": ["Cb", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
    "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
}

def generate_scale(root_note, pattern):
    """Generates a scale based on the root note and interval pattern."""
    notes = KEY_SIGNATURES[root_note]
    scale = [root_note]
    note_index = notes.index(root_note)
    for step in pattern:
        note_index = (note_index + step) % len(notes)
        scale.append(notes[note_index])
    return scale

def main():
    parser = argparse.ArgumentParser(
        description="Learn music scales with this flashcard app."
    )
    parser.add_argument(
        "-s", "--scale",
        type=str,
        default="major",
        choices=SCALES.keys(),
        help="Specify the scale or mode (default: major)."
    )
    parser.add_argument(
        "--fifths",
        action="store_true",
        help="Cycle through keys using the circle of fifths."
    )
    parser.add_argument(
        "--fourths",
        action="store_true",
        help="Cycle through keys using the circle of fourths."
    )
    args = parser.parse_args()

    # Determine the order of keys
    keys = list(KEY_SIGNATURES.keys())
    if args.fifths:
        key_order = keys
        use_random = False
    elif args.fourths:
        key_order = keys[::-1]  # Reverse the order for circle of fourths
        use_random = False
    else:
        key_order = keys
        use_random = True

    key_index = 0
    while True:
        # Determine the root note
        if use_random:
            root_note = random.choice(keys)
        else:
            root_note = key_order[key_index]

        # Get the selected scale pattern
        scale_pattern = SCALES[args.scale]

        # Generate and display the scale
        scale = generate_scale(root_note, scale_pattern)
        print(f"\nRoot Note: {root_note}")
        print(f"Scale ({args.scale.capitalize()}): {' '.join(scale)}")

        # Ask user for next action
        action = input("\nPress Enter for the next key or 'q' to quit: ").strip().lower()
        if action == 'q':
            print("\nExiting. Goodbye!")
            break

        # Move to the next key in the order if cycling
        if not use_random:
            key_index = (key_index + 1) % len(key_order)

if __name__ == "__main__":
    main()
import random
import argparse

# Define scales and modes
SCALES = {
    "major": [2, 2, 1, 2, 2, 2, 1],  # Whole and half step pattern
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "dorian": [2, 1, 2, 2, 2, 1, 2],
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "lydian": [2, 2, 2, 1, 2, 2, 1],
    "phrygian": [1, 2, 2, 2, 1, 2, 2],
    "locrian": [1, 2, 2, 1, 2, 2, 2],
}

# Define notes
NOTES_FLATS = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
NOTES_SHARPS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def generate_scale(root_note, pattern, use_sharps):
    """Generates a scale based on the root note, interval pattern, and notation."""
    notes = NOTES_SHARPS if use_sharps else NOTES_FLATS
    scale = [root_note]
    note_index = notes.index(root_note)
    for step in pattern:
        note_index = (note_index + step) % len(notes)
        scale.append(notes[note_index])
    return scale

def random_note():
    """Returns a random note."""
    return random.choice(NOTES_FLATS)

def random_notation():
    """Randomly decide between using flats or sharps."""
    return random.choice([True, False])  # True for sharps, False for flats

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
        "-n", "--note",
        type=str,
        help="Specify a root note (default: random).",
        choices=NOTES_FLATS + NOTES_SHARPS,
    )
    parser.add_argument(
        "-sf", "--sharps",
        action="store_true",
        help="Display notes using sharps."
    )
    parser.add_argument(
        "-fl", "--flats",
        action="store_true",
        help="Display notes using flats."
    )
    parser.add_argument(
        "-r", "--random-notation",
        action="store_true",
        help="Randomly choose flats or sharps."
    )
    args = parser.parse_args()

    while True:
        # Determine the root note
        root_note = args.note if args.note else random_note()

        # Determine notation (sharps or flats)
        if args.random_notation:
            use_sharps = random_notation()
        elif args.sharps:
            use_sharps = True
        elif args.flats:
            use_sharps = False
        else:
            use_sharps = False  # Default to flats

        # Get the selected scale pattern
        scale_pattern = SCALES.get(args.scale)

        # Display the root note
        print(f"\nRoot Note: {root_note}")
        action = input("Press any key to see the scale, or 'q'/'Esc' to quit: ").strip().lower()

        if action in ['q', '\x1b']:  # Quit on 'q' or 'Esc'
            print("\nExiting. Goodbye!")
            break

        # Display the scale
        scale = generate_scale(root_note, scale_pattern, use_sharps)
        print(f"Scale ({args.scale.capitalize()}): {' '.join(scale)}")

        # Ask for next input
        action = input("\nPress any key for another key or 'q'/'Esc' to exit: ").strip().lower()
        if action in ['q', '\x1b']:
            print("\nExiting. Goodbye!")
            break

if __name__ == "__main__":
    main()
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

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def generate_scale(root_note, pattern):
    """Generates a scale based on the root note and interval pattern."""
    scale = [root_note]
    note_index = NOTES.index(root_note)
    for step in pattern:
        note_index = (note_index + step) % len(NOTES)
        scale.append(NOTES[note_index])
    return scale

def random_note():
    """Returns a random note from the chromatic scale."""
    return random.choice(NOTES)

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
        choices=NOTES,
    )
    args = parser.parse_args()

    # Determine the root note
    root_note = args.note if args.note else random_note()

    # Get the selected scale pattern
    scale_pattern = SCALES.get(args.scale)

    # Generate and display the scale
    scale = generate_scale(root_note, scale_pattern)
    print(f"\nRoot Note: {root_note}")
    print(f"Scale ({args.scale.capitalize()}): {' '.join(scale)}")

    # Prompt for next action
    input("\nPress Enter for another scale or Ctrl+C to exit.\n")

    # Restart with a new random note
    main()

if __name__ == "__main__":
    main()
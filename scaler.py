import argparse

# Chromatic scale with embedded enharmonic equivalents
CHROMATIC = [
    ["C"],           # C
    ["C#", "Db"],    # C# / Db
    ["D"],           # D
    ["D#", "Eb"],    # D# / Eb
    ["E"],           # E
    ["F"],           # F
    ["F#", "Gb"],    # F# / Gb
    ["G"],           # G
    ["G#", "Ab"],    # G# / Ab
    ["A"],           # A
    ["A#", "Bb"],    # A# / Bb
    ["B"],           # B
]

# Define scales and modes
SCALES = {
    "major": [2, 2, 1, 2, 2, 2, 1],  # Whole and half step pattern
    "dorian": [2, 1, 2, 2, 2, 1, 2],
    "phrygian": [1, 2, 2, 2, 1, 2, 2],
    "lydian": [2, 2, 2, 1, 2, 2, 1],
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "minor": [2, 1, 2, 2, 1, 2, 2],
    "locrian": [1, 2, 2, 1, 2, 2, 2],
    "diminished": [2, 1, 2, 1, 2, 1, 2, 1],
    "augmented": [2, 2, 2, 2, 2, 2],
    "dominant": [2, 2, 1, 2, 2, 1, 1],
}

def determine_accidentals(root_note, scale_type):
    """
    Determine whether to prefer sharps or flats based on the key and scale type.
    """
    # Key-based preferences
    if "b" in root_note:
        return "flats"
    elif "#" in root_note:
        return "sharps"
    elif root_note == "F":
        return "flats"
    else:
        # Natural keys default to sharps
        return "sharps"

    # Scale-based preferences (overrides key-based in some cases)
    if scale_type in ["minor", "diminished", "dominant"]:
        return "flats"
    elif scale_type in ["major", "augmented", "lydian"]:
        return "sharps"
    else:
        return "sharps"  # Default to sharps if scale type is unknown

def get_chromatic_scale(root_note):
    """
    Return the chromatic scale starting from the given root note.
    Dynamically resolves enharmonic equivalents.
    """
    for i, equivalents in enumerate(CHROMATIC):
        if root_note in equivalents:
            return CHROMATIC[i:] + CHROMATIC[:i]
    raise ValueError(f"Invalid root note: {root_note}")

def generate_scale(root_note, pattern, prefer_accidentals):
    """
    Generate a scale dynamically based on the root note and interval pattern.
    Ensures note integrity using embedded enharmonic equivalents.
    """
    chromatic = get_chromatic_scale(root_note)
    scale = [root_note]  # Start with the root note
    used_letters = {root_note[0]}  # Track used note letters (A-G)
    current_index = 0

    for step in pattern:
        current_index = (current_index + step) % len(chromatic)
        next_note_options = chromatic[current_index]

        # Select the preferred enharmonic equivalent
        if prefer_accidentals == "flats":
            next_note = next_note_options[-1]  # Choose flat equivalent if available
        else:
            next_note = next_note_options[0]  # Choose sharp equivalent if available

        # Ensure note integrity (one of each letter A-G in the scale)
        next_letter = next_note[0]
        if next_letter in used_letters:
            # Conflict: Use the alternate enharmonic equivalent based on preference
            next_note = (
                next_note_options[0] if prefer_accidentals == "flats" else next_note_options[-1]
            )

        scale.append(next_note)
        used_letters.add(next_letter)

    # Ensure the final note is an exact match of the root note
    scale[-1] = root_note

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
        "-n", "--note",
        type=str,
        required=True,
        help="Specify the root note (e.g., C, G, Bb, F#) for debugging purposes.",
    )
    args = parser.parse_args()

    # Determine accidental preference
    prefer_accidentals = determine_accidentals(args.note, args.scale)

    # Get the selected scale pattern
    scale_pattern = SCALES[args.scale]

    # Generate and display the scale
    try:
        scale = generate_scale(args.note, scale_pattern, prefer_accidentals)
        print(f"Root Note: {args.note}")
        print(f"Scale ({args.scale.capitalize()}): {' '.join(scale)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
# Scaler

**Scaler** is a Python-based flashcard app designed to help musicians learn and practice music scales and modes interactively. It generates random notes or allows specifying a root note and scale/mode, making it an invaluable tool for learning and practice.

## Features

- **Random Note Practice:** Run the script without arguments to get a random root note and its corresponding major scale.
- **Custom Scales and Modes:** Specify a root note and choose from various scales/modes (e.g., Dorian, Minor, Mixolydian).
- **Interactive Experience:** After displaying a scale, press `Enter` to generate another scale or mode.
- **Extensible Design:** Easily add new scales and modes by updating the `SCALES` dictionary.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
    
       git clone https://github.com/your-username/scaler.git
    
2. Navigate to the directory:
    
       cd scaler
    
3. (Optional) Create and activate a virtual environment:
    
       python3 -m venv env
       source env/bin/activate  # On Windows: env\Scripts\activate
    
4. Install dependencies (if any; none currently).

## Usage

Run the script with optional arguments to customize your practice session.

### Basic Usage

Generate a random note and display its major scale:

       python scaler.py

### Custom Root Note and Scale

Specify a root note and a scale/mode:

       python scaler.py -n G -s dorian

### Available Scales/Modes

- Major
- Minor
- Dorian
- Mixolydian
- Lydian
- Phrygian
- Locrian

## Example Output

       Root Note: G
       Scale (Dorian): G A Bb C D E F G

       Press Enter for another scale or Ctrl+C to exit.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
       
       git checkout -b feature-name
       
3. Commit your changes:
       
       git commit -m "Add feature description"
       
4. Push to your fork:
       
       git push origin feature-name
       
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Future Features

- Add support for custom user-defined scales/modes.
- Implement a quiz mode for enhanced learning.
- Provide MIDI output for auditory feedback.
- Track user progress over time.
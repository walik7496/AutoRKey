# AutoRKey

**AutoRKey** is a simple Python script that globally replaces custom text sequences with special characters as you type.  
For example, typing `oo` will be automatically replaced with `ö`, `ae` → `ä`, and `ue` → `ü`.  

It works in **any application** where text input is possible.

---

## Features

- Global keyboard listener using `pynput`
- Automatic replacement of predefined sequences
- Easy to customize by editing the `mapping` dictionary
- Works with multiple languages or custom characters

---

## Requirements

- Python 3.7 or higher
- `pynput` library

Install `pynput` via pip:

```bash
pip install pynput
```

## Usage

1. Clone or download this repository.

2. Edit the mapping dictionary in AutoRKey.py to add your own replacement sequences:

mapping = {
    "oo": "ö",
    "ae": "ä",
    "ue": "ü"
}

3. Run the script:

python AutoRKey.py

4. Start typing in any application. When you type a sequence from the mapping dictionary, it will be automatically replaced by the corresponding character.

## How It Works

- The script listens to all key presses globally.

- Each character is stored in a buffer.

- If the end of the buffer matches a trigger from mapping:

- The trigger characters are deleted using Backspace.

- The replacement characters are typed automatically.

## Notes

- The script only works for character keys (key.char). Special keys like Shift, Ctrl, or Alt are ignored.

- Designed for personal productivity; it simulates key presses.

- Works on Windows, macOS, and Linux.

## Contributing

Feel free to fork and customize:

- Add more replacement sequences
- Extend for multiple languages
- Integrate JSON-based mapping for easier editing

## License

MIT License

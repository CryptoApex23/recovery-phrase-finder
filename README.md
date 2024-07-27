# CryptoAppex

**CryptoAppex** is a tool for recovering Ethereum mnemonic phrases. This script attempts to find a valid 12-word mnemonic phrase by filling in placeholders (`x`) and checks if the resulting mnemonic produces a target Ethereum address.

## Features

- **Mnemonic Phrase Recovery**: Given a partial mnemonic phrase with placeholders, the tool tries all possible combinations from a word list.
- **Ethereum Address Validation**: Checks if the resulting mnemonic generates the specified Ethereum address.
- **Progress Tracking**: Displays a live progress bar while searching for the correct mnemonic.

## Setup

### Prerequisites

Ensure you have Python 3.8 or later installed on your system.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cryptoappex.git
   cd cryptoappex
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare a word list file:**

   Ensure you have a `wordlist.txt` file with one word per line. This file is used to generate mnemonic combinations.

2. **Run the script:**

   ```bash
   python cryptoappex.py
   ```

3. **Follow the prompts:**

   - Enter the partial mnemonic phrase with `x` as placeholders for missing words.
   - Enter the target Ethereum address.

   Example input:

   ```
   What is the mnemonic phrase (put 'x' where you are missing a word)?
   tornado glass tribe limit talent festival soup helmet brass elevator x
   What is the target wallet address?
   0xYourTargetEthereumAddressHere
   ```

   The script will try all possible combinations and display the correct mnemonic phrase if found.

## Example

![Example Screenshot](screenshots/screenshot_1.png)

## Troubleshooting

- **Invalid Mnemonic Phrase**: Ensure your mnemonic phrase has exactly 12 words with `x` placeholders.
- **Invalid Ethereum Address**: Make sure you provide a valid Ethereum address.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

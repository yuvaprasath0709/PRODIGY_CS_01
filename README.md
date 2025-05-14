# Caesar Cipher Implementation

## Overview

This project is a Python implementation of the Caesar Cipher, a simple substitution cipher used for encrypting and decrypting text. This was developed as part of an internship task.

## Features

* Encrypts text using the Caesar Cipher algorithm.
* Decrypts text using the Caesar Cipher algorithm.
* Allows the user to specify the shift value (key).
* Handles both uppercase and lowercase letters.
* Handles non-alphabetic characters
* Provides a command-line interface.

## How It Works

The Caesar Cipher works by shifting each letter in the plaintext a certain number of positions down the alphabet. The shift value, or key, determines the number of positions each letter is moved.

For example, with a shift of 3:

* A becomes D
* B becomes E
* ...
* Z becomes C

Decryption is performed by shifting the letters in the ciphertext back by the same shift value.

## Tools and Installation

To run this project, you need to have Python 3 installed on your system.

### Installation Steps

1.  **Install Python 3:**

    * **Windows:** Download the latest version of Python 3 from the official website (python.org) and follow the installation instructions. Make sure to add Python to your PATH environment variable during installation.
    * **macOS:** Python 3 is usually pre-installed. You can verify by typing `python3 --version` in your terminal. If not installed, you can install it using Homebrew:

        ```bash
        brew install python
        ```
    * **Linux:** Use your distribution's package manager. For example, on Ubuntu or Debian:

        ```bash
        sudo apt update
        sudo apt install python3
        ```
2.  **Clone the Repository:**

    Clone the repository to your local machine using Git:

    ```bash
    git clone [Your GitHub Repository Link]
    ```

3.  **Navigate to the Project Directory:**

    ```bash
    cd [Project Directory Name]
    ```

4.  **Run the Program:**

    ```bash
    python caesar_cipher.py
    ```

    Follow the prompts to encrypt or decrypt text.

## Usage

1.  Clone the repository to your local machine:

    ```bash
    git clone [Your GitHub Repository Link]
    ```

2.  Navigate to the project directory:

    ```bash
    cd [Project Directory Name]
    ```

3.  Run the program:

    ```bash
    python caesar_cipher.py
    ```

4.  Follow the prompts to encrypt or decrypt text.

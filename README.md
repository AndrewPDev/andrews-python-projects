# Andrew's Python Projects

A collection of Python tools and utilities for various purposes.

## 📋 Overview

This repository contains Python scripts and tools developed for educational and professional use. Currently featuring a hash identification tool for cybersecurity analysis.

## 🛠️ Hash Identifier Tool

**File:** `hash_tester_main.py`

A powerful hash identification tool that analyzes hash strings and identifies the most likely hash algorithm based on pattern matching and characteristic analysis.

**Features:**
- Supports 15+ hash types including MD5, SHA variants, bcrypt, scrypt, Argon2, PBKDF2
- Single hash analysis with confidence scoring
- Batch file processing for multiple hashes
- Character set analysis and security recommendations
- Interactive command-line interface

**Supported Hash Types:**
- **Cryptographic Hashes:** MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512
- **Password Hashing:** bcrypt, scrypt, Argon2, PBKDF2
- **Windows Hashes:** NTLM, LM Hash
- **Application-Specific:** MySQL5, WordPress, Drupal 7, Joomla

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses standard library only)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/AndrewPDev/andrews-python-projects.git
   cd andrews-python-projects
   ```

2. Make script executable (Unix/Linux):
   ```bash
   chmod +x hash_tester_main.py
   ```

### Running the Hash Identifier

```bash
python hash_tester_main.py
```

## 💡 Usage Examples

### Single Hash Analysis
```
Enter hash to identify (or command): 5d41402abc4b2a76b9719d911017c592
```

### Batch File Analysis
```
Enter hash to identify (or command): file:sample_hashes.txt
```

### Sample Hash File Format
Create a text file with one hash per line:
```
# Sample hash file - comments start with #
5d41402abc4b2a76b9719d911017c592
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
*23AE809DDACAF96AF0FD78ED04B6A265E05AA257
```

## 📊 Output Example

```
============================================================
Hash Analysis for: 5d41402abc4b2a76b9719d911017c592
============================================================

Found 3 possible match(es):

1. MD5 - MD5 (Message Digest 5)
   Confidence: 80%
   Example: 5d41402abc4b2a76b9719d911017c592

2. NTLM - NTLM Hash
   Confidence: 50%
   Example: b4b9b02e6f09a9bd760f388b67351e2b

3. LM - LM Hash (LAN Manager)
   Confidence: 50%
   Example: aad3b435b51404eeaad3b435b51404ee

Additional Analysis:
   Length: 32 characters
   Character set: Hexadecimal (0-9, a-f)
   Most likely: MD5 (80%)
   WARNING: This appears to be a weak hash algorithm!
```

## 🔧 Commands

| Command | Description |
|---------|-------------|
| `help` | Display usage information |
| `quit`, `exit`, `q` | Exit the program |
| `file:filename.txt` | Analyze multiple hashes from file |

## Security Notes

- **MD5 and SHA-1** are considered cryptographically weak and should not be used for security purposes
- **bcrypt, scrypt, Argon2** are recommended for password hashing
- This tool is for **authorized testing only** - ensure proper permissions before use
- Always verify hash identification results with additional testing

## Project Structure

```
andrews-python-projects/
├── README.md
├── hash_tester_main.py      # Hash identifier tool
└── examples/
    └── sample_hashes.txt    # Example hash file (optional)
```

## Contributing

Feel free to contribute additional Python tools and utilities! Please:
- Follow existing code style and commenting patterns
- Include appropriate documentation
- Test thoroughly before submission
- Add examples for new features

## License

This software is intended for educational and authorized professional use. Users are responsible for ensuring they have proper authorization before using these tools in professional environments.

## Author

**Andrew Piggot**

## Purpose

Created for educational purposes and authorized penetration testing scenarios.

---

**DISCLAIMER:** This tool is for educational and authorized testing only. Unauthorized use may violate laws in your jurisdiction. Users assume all responsibility for legal and ethical use.

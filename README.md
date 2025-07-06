# Andrew's Python Projects

A collection of Python tools and utilities for various purposes.

## 📋 Overview

This repository contains Python scripts and tools developed for educational and professional use. Currently featuring a hash identification tool for cybersecurity analysis, a CSV/Excel analyzer for data processing, and an SEO website analyzer for optimization auditing.

---

## 🔐 Hash Identifier Tool

**File:** `hash_tester_main.py`

A powerful hash identification tool that analyzes hash strings and identifies the most likely hash algorithm based on pattern matching and characteristic analysis.

### Features
- Supports 15+ hash types including MD5, SHA variants, bcrypt, scrypt, Argon2, PBKDF2
- Single hash analysis with confidence scoring
- Batch file processing for multiple hashes
- Character set analysis and security recommendations
- Interactive command-line interface

### Supported Hash Types
- **Cryptographic Hashes:** MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512
- **Password Hashing:** bcrypt, scrypt, Argon2, PBKDF2
- **Windows Hashes:** NTLM, LM Hash
- **Application-Specific:** MySQL5, WordPress, Drupal 7, Joomla

### Installation & Usage
```bash
# Clone repository (if not already done)
git clone https://github.com/AndrewPDev/andrews-python-projects.git
cd andrews-python-projects

# Run the hash identifier
python hash_tester_main.py
```

### Usage Examples
#### Single Hash Analysis
```
Enter hash to identify (or command): 5d41402abc4b2a76b9719d911017c592
```

#### Batch File Analysis
```
Enter hash to identify (or command): file:sample_hashes.txt
```

#### Sample Hash File Format
Create a text file with one hash per line:
```
# Sample hash file - comments start with #
5d41402abc4b2a76b9719d911017c592
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
*23AE809DDACAF96AF0FD78ED04B6A265E05AA257
```

### Output Example
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

### Commands
| Command | Description |
|---------|-------------|
| `help` | Display usage information |
| `quit`, `exit`, `q` | Exit the program |
| `file:filename.txt` | Analyze multiple hashes from file |

### Security Notes
- **MD5 and SHA-1** are considered cryptographically weak and should not be used for security purposes
- **bcrypt, scrypt, Argon2** are recommended for password hashing
- This tool is for **authorized testing only** - ensure proper permissions before use
- Always verify hash identification results with additional testing

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## 📊 CSV/Excel Analyzer and Cleaner

**File:** `csv_main/csv_analyzer.py`

A comprehensive data analysis and cleaning tool for CSV files that provides insights into your data and helps clean it up for better analysis.

### Features
- Load and analyze CSV files with automatic delimiter detection
- Column-wise data analysis with type detection
- Data quality assessment (duplicates, empty rows, inconsistencies)
- Interactive data cleaning options
- Export cleaned data to new files
- Generate detailed analysis reports
- Support for various CSV formats

### Analysis Capabilities
- **Basic Statistics:** Row/column counts, file size, data types
- **Column Analysis:** Empty values, unique values, sample data
- **Data Quality:** Duplicate detection, empty row identification, inconsistent formatting
- **Type Detection:** Automatic detection of numeric, date, and text columns

### Cleaning Options
- Remove completely empty rows
- Trim whitespace from all cells
- Remove special characters
- Remove duplicate rows
- Export cleaned data

### Installation & Usage
```bash
# Clone repository (if not already done)
git clone https://github.com/AndrewPDev/andrews-python-projects.git
cd andrews-python-projects

# Run the CSV analyzer
python csv_main/csv_analyzer.py
```

### Usage Examples
#### Basic Workflow
```
csv-analyzer> load csv_main/sample_data.csv
csv-analyzer> analyze
csv-analyzer> clean
csv-analyzer> export cleaned_data.csv
```

#### Sample CSV Data
A sample CSV file (`csv_main/sample_data.csv`) is included for testing the analyzer.

### Commands
| Command | Description |
|---------|-------------|
| `load <filename>` | Load a CSV file for analysis |
| `analyze` | Analyze the loaded data |
| `clean` | Clean data with interactive options |
| `export <filename>` | Export cleaned data to new file |
| `report` | Generate analysis report |
| `help` | Display usage information |
| `quit`, `exit` | Exit the program |

---

## 🌐 SEO Website Analyzer

**File:** `seo_tools/seo_analyzer.py`

A comprehensive SEO analysis tool that audits websites for optimization opportunities and provides actionable recommendations to improve search engine rankings.

### Features
- Complete on-page SEO analysis with scoring system
- Title tag optimization analysis (length, structure)
- Meta description evaluation and recommendations
- Heading structure analysis (H1-H6 hierarchy)
- Image alt text optimization checking
- Internal/external link analysis
- Content quality assessment (word count, readability)
- Technical SEO factors (HTTPS, page size, schema markup)
- Detailed reporting with actionable recommendations
- JSON export functionality for reports

### Analysis Categories
- **Title & Meta:** Title tags, meta descriptions, meta keywords
- **Content Structure:** Heading hierarchy, content length, text quality
- **Images:** Alt text optimization, image count analysis
- **Links:** Internal linking structure, external link evaluation
- **Technical SEO:** HTTPS usage, page size, structured data detection
- **Overall Scoring:** 0-10 scale with improvement recommendations

### Installation & Usage
```bash
# Clone repository (if not already done)
git clone https://github.com/AndrewPDev/andrews-python-projects.git
cd andrews-python-projects

# Run the SEO analyzer
python seo_tools/seo_analyzer.py
```

### Usage Examples
#### Basic Website Analysis
```
Enter website URL to analyze: https://example.com
Enter website URL to analyze: example.com  # HTTPS added automatically
```

#### Export Analysis Report
```
Enter website URL to analyze: export my_seo_report.json
```

### Sample Analysis Output
```
==============================================================
SEO ANALYSIS REPORT
==============================================================
URL: https://example.com
Overall SEO Score: 7/10 🟡 Good
==============================================================

📝 TITLE ANALYSIS
Title: 'Example Domain - Your Website Title Here'
Length: 42 characters
   ✅ Title length is optimal (30-60 characters)

📄 META DESCRIPTION ANALYSIS
Description: 'This domain is for use in illustrative examples in documents...'
Length: 140 characters
   ✅ Meta description length is optimal (120-160 characters)

💡 KEY RECOMMENDATIONS
   1. Add more internal links for better navigation
   2. Consider adding schema markup for rich snippets
   3. Expand content to over 600 words for better SEO
```

### SEO Score Breakdown
| Score | Rating | Description |
|-------|--------|-------------|
| 🟢 8-10 | Excellent | Well-optimized, minor tweaks needed |
| 🟡 6-7 | Good | Solid foundation, some improvements needed |
| 🟠 4-5 | Needs Work | Several issues to address |
| 🔴 0-3 | Poor | Major SEO problems requiring attention |

### Commands
| Command | Description |
|---------|-------------|
| `URL` | Analyze any website URL |
| `export filename.json` | Export last analysis to JSON file |
| `help` | Display usage information |
| `quit`, `exit` | Exit the program |

### What Gets Analyzed
- **Title Tags:** Length, optimization, brand inclusion
- **Meta Descriptions:** Length, compelling content, keyword usage
- **Heading Structure:** Proper H1-H6 hierarchy and usage
- **Images:** Alt text presence, optimization opportunities
- **Links:** Internal linking strategy, external link quality
- **Content:** Word count, readability, content depth
- **Technical Factors:** HTTPS, page speed indicators, structured data

### Use Cases
- **Website Audits:** Comprehensive SEO health checks
- **Content Optimization:** Improve existing page performance
- **Competitor Analysis:** Compare SEO implementations
- **Client Reporting:** Professional SEO audit reports
- **Learning Tool:** Understand SEO best practices

---

## 🚀 General Information

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses standard library only)

### Installation
```bash
git clone https://github.com/AndrewPDev/andrews-python-projects.git
cd andrews-python-projects
```

### Make Scripts Executable (Unix/Linux)
```bash
chmod +x hash_tester_main.py
chmod +x csv_main/csv_analyzer.py
chmod +x seo_tools/seo_analyzer.py
```

## 🏗️ Project Structure

```
andrews-python-projects/
├── README.md
├── hash_tester_main.py      # Hash identifier tool
├── DEVELOPMENT_NOTES.md     # Development guidelines and lessons learned
├── CODE_TEMPLATES.md        # Reusable code patterns and templates
├── csv_main/                # CSV analyzer module
│   ├── csv_analyzer.py      # CSV/Excel analyzer and cleaner
│   └── sample_data.csv      # Sample CSV file for testing
├── seo_tools/               # SEO analysis module
│   └── seo_analyzer.py      # SEO website analyzer and auditor
└── examples/
    └── sample_hashes.txt    # Example hash file (optional)
```

## 📝 Contributing

Feel free to contribute additional Python tools and utilities! Please:
- Follow existing code style and commenting patterns
- Include appropriate documentation
- Test thoroughly before submission
- Add examples for new features

## 📄 License

This software is intended for educational and authorized professional use. Users are responsible for ensuring they have proper authorization before using these tools in professional environments.

## 👤 Author

**Andrew Piggot**

## 🤝 Purpose

Created for educational purposes and authorized penetration testing scenarios.

---

**⚠️ DISCLAIMER:** This tool is for educational and authorized testing only. Unauthorized use may violate laws in your jurisdiction. Users assume all responsibility for legal and ethical use.

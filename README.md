# Project Analyzer with Amazon Q Developer

A command-line tool that helps developers analyze their projects using Amazon Q Developer.

[Project Analyzer Demo](hhttps://imgur.com/a/p1fJRCk)

## Features
- Analyzes any project directory using Amazon Q Developer
- Provides detailed analysis reports with colored output
- Exports results to a file
- Displays statistics about analysis and project
- Handles errors gracefully
- Simple and intuitive command-line interface

Installation

Prerequisites
1. Make sure you have Python 3.x installed
2. Install Amazon Q Developer CLI by following the [official guide](https://docs.aws.amazon.com/amazonq/latest/qdev-ug/what-is-q-developer.html)

### Steps
1. Clone this repository:
```bash
git clone https://github.com/Maschiett/Project-Analyzer-with-Amazon-Q-Developer-CLI/.git
cd project-analyzer
```

2. You're ready to go! No additional Python packages are required.

Usage

Basic Usage
```bash
python q_analyze.py <project_path>
```

With Parameters
```bash
python q_analyze.py <project_path> -o results.txt -v
```

Command Options
- `<project_path>` - Path to the project directory to analyze
- `-o, --output FILE` - Save results to the specified file
- `-v, --verbose` - Enable verbose output with additional information
- `-h, --help` - Show help message

Examples

Basic Analysis
```bash
python q_analyze.py ./my_project
```

Save Results to File
```bash
python q_analyze.py ./my_project -o results.txt
```

Verbose Analysis
```bash
python q_analyze.py ./my_project -v
```

Combine Options
```bash
python q_analyze.py ./my_project -o results.txt -v
```

Output Example

```
Launching Amazon Q Developer Analysis
Project: my_project
Path: /full/path/to/my_project
Start time: 2023-05-04 14:30:22

Scanning project structure...
Files found: 156

Executing analysis command...

=== ANALYSIS RESULTS ===
[Amazon Q Developer analysis output here]

=== STATISTICS ===
Execution time: 5.23 seconds
```

Technical Details

Requirements
- Python 3.x
- Amazon Q Developer CLI
- Standard Python modules:
  - subprocess
  - os
  - sys
  - argparse
  - time
  - datetime

How It Works
1. The script validates the provided project path
2. It collects project information (name, file count, etc.)
3. Amazon Q Developer CLI is executed with appropriate parameters
4. Results are processed, formatted with colors for better readability
5. If requested, results are saved to a file
6. Execution statistics are displayed

How I Used Amazon Q Developer
I used Amazon Q Developer to:
- Create the initial script structure
- Implement error handling and input validation
- Optimize command execution
- Add color output functionality
- Test the script with different project types

Troubleshooting

Common Issues
- "Amazon Q Developer CLI not found": Make sure you have installed Amazon Q Developer CLI correctly and it's available in your PATH
- "Not a directory": The provided path is not a valid directory
- Permission errors: Make sure you have proper permissions to access the directory

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

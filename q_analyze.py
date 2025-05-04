import subprocess
import sys
import os
import argparse
import time
from datetime import datetime

# ANSI color codes for colored output
COLORS = {
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "END": "\033[0m"
}

def color_print(text, color):
    """Print text with the specified color."""
    print(f"{COLORS.get(color, '')}{text}{COLORS['END']}")

def analyze_project(project_path, output_file=None, verbose=False):
    """
    Analyzes the specified project using Amazon Q Developer.
    
    Args:
        project_path (str): Path to the project directory
        output_file (str): Path to file for saving results
        verbose (bool): Verbose output flag
    """
    if not os.path.isdir(project_path):
        color_print(f"Error: The specified path is not a directory: {project_path}", "RED")
        return False

    start_time = time.time()
    project_name = os.path.basename(os.path.abspath(project_path))
    
    color_print(f"\n{COLORS['BOLD']}Launching Amazon Q Developer Analysis{COLORS['END']}", "BLUE")
    color_print(f"Project: {project_name}", "BLUE")
    color_print(f"Path: {os.path.abspath(project_path)}", "BLUE")
    color_print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "BLUE")
    
    if verbose:
        print("\nScanning project structure...")
        file_count = count_files(project_path)
        print(f"Files found: {file_count}")
    
    try:
        print("\nExecuting analysis command...")
        result = subprocess.run(
            ["q", "analyze", project_path],
            capture_output=True,
            text=True
        )
        
        elapsed_time = time.time() - start_time
        
        # Output results
        color_print("\n=== ANALYSIS RESULTS ===", "GREEN")
        if result.stdout:
            print(result.stdout)
        else:
            color_print("No data in standard output.", "YELLOW")
            
        if result.stderr:
            color_print("\n=== ERRORS ===", "RED")
            print(result.stderr)
        
        # Save to file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Project Analysis: {project_name}\n")
                f.write(f"Path: {os.path.abspath(project_path)}\n")
                f.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("=== ANALYSIS RESULTS ===\n")
                f.write(result.stdout)
                if result.stderr:
                    f.write("\n=== ERRORS ===\n")
                    f.write(result.stderr)
            color_print(f"\nResults saved to file: {output_file}", "GREEN")
        
        # Display statistics
        color_print(f"\n=== STATISTICS ===", "BLUE")
        print(f"Execution time: {elapsed_time:.2f} seconds")
        if verbose:
            print(f"Return code: {result.returncode}")
        
        return True
        
    except FileNotFoundError:
        color_print("Error: Amazon Q Developer CLI tool not found.", "RED")
        color_print("Please install Amazon Q Developer CLI by following the official guide:", "YELLOW")
        color_print("https://docs.aws.amazon.com/amazonq/latest/qdev-ug/what-is-q-developer.html", "YELLOW")
        return False
    except Exception as e:
        color_print(f"Error during analysis: {e}", "RED")
        return False

def count_files(directory):
    """Count the number of files in the directory and subdirectories."""
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count

def main():
    """Main function of the script."""
    parser = argparse.ArgumentParser(
        description="Project Analyzer using Amazon Q Developer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("project_path", 
                      help="Path to the project directory to analyze")
    parser.add_argument("-o", "--output", 
                      help="File to save analysis results")
    parser.add_argument("-v", "--verbose", action="store_true", 
                      help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Run analysis
    analyze_project(args.project_path, args.output, args.verbose)

if __name__ == "__main__":
    main()
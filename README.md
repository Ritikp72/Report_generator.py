# Report Generator

## Overview
This Python program reads a log file, analyzes its contents, and generates a report. It counts the total number of lines, the number of lines containing "error" or "warning", and ignores lines containing "info".

## Features
- Read any text log file from a user-specified path.
- Count total lines in the file.
- Count the number of lines containing "error" (case-insensitive).
- Count the number of lines containing "warning" (case-insensitive).
- Generate a report in `report.txt`.

## How to Use
1. Run the `Report_Generator.py` script.
2. When prompted, enter the full path of your log file.
3. The program will generate a `report.txt` file with the analysis.

## Example
Input log file (`check.txt`):

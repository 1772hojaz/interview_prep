#!/bin/bash
# Run a test from src/arrays/intermediate/
# Usage: ./run_test.sh test_find_duplicates.py

if [ $# -eq 0 ]; then
  echo "Usage: $0 <test_file>"
  echo "Example: $0 test_find_duplicates.py"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

MODULE=$(echo "$1" | sed 's|\.py$||')
cd "$PROJECT_ROOT"
python3 -m unittest tests.arrays.intermediate."$MODULE" -v

#!/bin/bash
# Run a single test file
# Usage: ./bin/run_test.sh tests/arrays/basic/test_find_max.py

if [ $# -eq 0 ]; then
  echo "Usage: $0 <test_file_path>"
  echo ""
  echo "Examples:"
  echo "  $0 tests/arrays/basic/test_find_max.py"
  echo "  $0 tests/sorting/basic/test_merge_sort.py"
  exit 1
fi

TEST_FILE=$1

if [ ! -f "$TEST_FILE" ]; then
  echo "Error: File not found: $TEST_FILE"
  exit 1
fi

cd /home/humphrey/interview_prep

# Convert path to module path
MODULE=$(echo $TEST_FILE | sed 's|/|.|g; s|\.py$||')

echo "Running: $TEST_FILE"
echo "---"
python3 -m unittest "$MODULE" -v

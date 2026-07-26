#!/bin/bash
# Run tests with various filters
# Usage: ./bin/run_tests.sh [options]

show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -f, --file <path>      Run specific test file"
  echo "  -d, --dir <path>       Run all tests in directory"
  echo "  -l, --level <level>    Run all tests for level (basic|intermediate|advanced)"
  echo "  -s, --subject <name>   Run all tests for subject (arrays|strings|...)"
  echo "  -a, --all              Run all tests"
  echo "  -h, --help             Show this help"
  echo ""
  echo "Examples:"
  echo "  $0 -f tests/arrays/basic/test_find_max.py"
  echo "  $0 -d tests/arrays/basic"
  echo "  $0 -l basic"
  echo "  $0 -s arrays"
  echo "  $0 -a"
}

cd /home/humphrey/interview_prep

case $1 in
  -f|--file)
    if [ ! -f "$2" ]; then
      echo "Error: File not found: $2"
      exit 1
    fi
    MODULE=$(echo $2 | sed 's|/|.|g; s|\.py$||')
    echo "Running: $2"
    python3 -m unittest "$MODULE" -v
    ;;
  -d|--dir)
    if [ ! -d "$2" ]; then
      echo "Error: Directory not found: $2"
      exit 1
    fi
    echo "Running tests in: $2"
    python3 -m unittest discover -s "$2" -p "test_*.py" -v
    ;;
  -l|--level)
    echo "Running all $2 tests..."
    find tests -path "*/$2/test_*.py" -exec python3 -m unittest {} \;
    ;;
  -s|--subject)
    echo "Running all $2 tests..."
    python3 -m unittest discover -s "tests/$2" -p "test_*.py" -v
    ;;
  -a|--all)
    echo "Running all tests..."
    python3 -m unittest discover -s tests -p "test_*.py" -v
    ;;
  *)
    show_help
    ;;
esac

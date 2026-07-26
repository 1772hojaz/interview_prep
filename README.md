# Interview Prep Project

ALX-style interview prep with questions and tests organized by data structures and algorithms.

## Project Structure

```
interview_prep/
├── src/                           # Question files
│   ├── arrays/                    
│   ├── strings/                   
│   ├── linked_lists/              
│   ├── stacks/                    
│   ├── queues/                    
│   ├── hash_tables/               
│   ├── trees/                     
│   │   ├── binary_tree/           
│   │   ├── bst/                   
│   │   └── avl/                   
│   ├── graphs/                    
│   ├── heaps/                     
│   ├── sorting/                   
│   ├── searching/                 
│   ├── dynamic_programming/       
│   └── bit_manipulation/          
│
├── tests/                         # Test files (mirrors src/)
│
├── bin/                           # Helper scripts
│   ├── run_test.sh                # Run single test
│   └── run_tests.sh               # Run multiple tests
│
└── README.md
```

## Quick Start

### Run a Single Test

```bash
# From project root
./bin/run_test.sh tests/arrays/basic/test_find_max.py

# Or any test file
./bin/run_test.sh tests/sorting/basic/test_merge_sort.py
./bin/run_test.sh tests/trees/bst/basic/test_bst_insert.py
./bin/run_test.sh tests/graphs/advanced/test_dijkstra.py
```

### Run Multiple Tests

```bash
# Run all tests in a directory
./bin/run_tests.sh -d tests/arrays/basic

# Run all tests for a subject
./bin/run_tests.sh -s arrays

# Run all tests for a difficulty level
./bin/run_tests.sh -l basic

# Run all tests
./bin/run_tests.sh -a
```

### Using Python Directly

```bash
# Run single test
python3 -m unittest tests.arrays.basic.test_find_max -v

# Run all tests in directory
python3 -m unittest discover -s tests/arrays/basic -v

# Run all tests
python3 -m unittest discover -s tests -v
```

## Question File Format

Each question has its own file with function stub and docstring:

```python
#!/usr/bin/env python3
"""Find Maximum Element"""


def find_max(arr):
    """Find and return the maximum element.
    
    Args:
        arr: List of integers
        
    Returns:
        int: Maximum element
    """
    pass
```

## Test File Format

Each test file has a test class ready for you to implement:

```python
#!/usr/bin/env python3
"""Test for Find Maximum Element"""
import unittest
from src.arrays.basic.find_max import find_max


class TestFind_max(unittest.TestCase):
    """Tests for find_max"""

    def test_basic(self):
        # Add your test here
        pass

    def test_empty(self):
        # Add your test here
        pass

    def test_single_element(self):
        # Add your test here
        pass


if __name__ == '__main__':
    unittest.main()
```

## Difficulty Levels

| Level | Questions | Description |
|-------|-----------|-------------|
| basic | 120 | Entry-level with hints |
| intermediate | 120 | Medium difficulty |
| advanced | 82 | Hard problems, no hints |

## Total Count

- **322 question files**
- **322 test files**
- **14 data structures**

## Data Structures

| Subject | Questions |
|---------|-----------|
| arrays | 24 |
| strings | 24 |
| linked_lists | 24 |
| stacks | 21 |
| queues | 18 |
| hash_tables | 22 |
| trees/binary_tree | 24 |
| trees/bst | 22 |
| trees/avl | 16 |
| graphs | 22 |
| heaps | 19 |
| sorting | 21 |
| searching | 22 |
| dynamic_programming | 26 |
| bit_manipulation | 22 |

## How to Use

1. Pick a topic directory (e.g., `src/arrays/`)
2. Choose difficulty level (basic → intermediate → advanced)
3. Open question file and implement the function
4. Run the test to verify:
   ```bash
   ./bin/run_test.sh tests/arrays/basic/test_find_max.py
   ```
5. Move to next question when test passes

## Tips

- Start with **basic** to build fundamentals
- Focus on **intermediate** for common interview questions
- Tackle **advanced** for top-tier companies
- Write test cases for edge cases
- Review solutions after implementing

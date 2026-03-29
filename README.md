# CodeWars Solutions Repository

This repository stores my Codewars kata solutions across multiple languages, organized by difficulty level (`Kyu`).

## Repository Structure

```text
CodeWars/
├── C/
├── CPP/
├── Python/
└── Rust/
```

Inside each language folder, solutions are grouped by `Kyu` (for example `8 Kyu`, `7 Kyu`, `6 Kyu`), and some folders include `dunno` for uncategorized solutions.

## Current Coverage (as of 2026-03-28)

- Python: 619 solutions
- Rust: 73 solutions
- C: 59 solutions
- C++: 30 solutions

## How Files Are Organized

- One file usually represents one kata solution.
- File names typically reflect the kata/problem name.
- Difficulty folders make it easy to track progression from beginner to advanced katas.

## Running Solutions Locally

### Python

```bash
python3 path/to/solution.py
```

### C

```bash
gcc path/to/solution.c -o solution
./solution
```

### C++

```bash
g++ path/to/solution.cpp -o solution
./solution
```

### Rust

```bash
rustc path/to/solution.rs -o solution
./solution
```

## Notes

- Solutions are focused on practice and learning, so style and approach may vary between files.
- Some problems may have more than one valid implementation strategy.
- Update counts with `scripts/update_readmes.sh`.

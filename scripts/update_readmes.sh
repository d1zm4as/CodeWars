#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE="$(date +%F)"

count_py="$(rg --files -g '*.py' "$ROOT_DIR/Python" | wc -l | tr -d ' ')"
count_js="$(rg --files -g '*.js' "$ROOT_DIR/Python" | wc -l | tr -d ' ')"
count_c="$(rg --files -g '*.c' "$ROOT_DIR/C" | wc -l | tr -d ' ')"
count_cpp="$(rg --files -g '*.cpp' "$ROOT_DIR/CPP" | wc -l | tr -d ' ')"
count_rs="$(rg --files -g '*.rs' "$ROOT_DIR/Rust" | wc -l | tr -d ' ')"

perl -0pi -e "s/## Current Coverage \\(as of [0-9-]+\\)/## Current Coverage (as of $DATE)/" \
  "$ROOT_DIR/README.md"
perl -0pi -e "s/- Python: [0-9]+ solutions/- Python: $count_py solutions/" \
  "$ROOT_DIR/README.md"
perl -0pi -e "s/- Rust: [0-9]+ solutions/- Rust: $count_rs solutions/" \
  "$ROOT_DIR/README.md"
perl -0pi -e "s/- C: [0-9]+ solutions/- C: $count_c solutions/" \
  "$ROOT_DIR/README.md"
perl -0pi -e "s/- C\\+\\+: [0-9]+ solutions/- C++: $count_cpp solutions/" \
  "$ROOT_DIR/README.md"

perl -0pi -e 's/- (?:Around |around )?[0-9]+ `\.py` files\./- '"$count_py"' `.py` files./' \
  "$ROOT_DIR/Python/README.md"
perl -0pi -e 's/- (?:A few |around |Around )?[0-9]+ `\.js` files stored alongside Python solutions\./- '"$count_js"' `.js` files stored alongside Python solutions./' \
  "$ROOT_DIR/Python/README.md"

perl -0pi -e 's/- (?:Around |around )?[0-9]+ `\.c` solution files\./- '"$count_c"' `.c` solution files./' \
  "$ROOT_DIR/C/README.md"
perl -0pi -e 's/- (?:Around |around )?[0-9]+ `\.cpp` solution files\./- '"$count_cpp"' `.cpp` solution files./' \
  "$ROOT_DIR/CPP/README.md"
perl -0pi -e 's/- (?:Around |around )?[0-9]+ `\.rs` solution files\./- '"$count_rs"' `.rs` solution files./' \
  "$ROOT_DIR/Rust/README.md"

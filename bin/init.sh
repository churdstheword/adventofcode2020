#! /bin/bash

PROJECT_DIR=${PWD}

for DAY in {1..25}; do

    # Setup the directory for the challenge
    DAY_DIR="${PROJECT_DIR}/day${DAY_LABEL}"
    mkdir -p $DAY_DIR
    
    # Create the files for the challenge
    touch $DAY_DIR/input.txt
    cat /dev/null > $DAY_DIR/input.txt

    touch $DAY_DIR/solution.py
    cat /dev/null > $DAY_DIR/solution.py

    # Lets create an README file
    touch $DAY_DIR/README.md
    echo "# DAY ${DAY}" > $DAY_DIR/README.md
    echo "" >> $DAY_DIR/README.md
    echo "[https://adventofcode.com/2020/day/${DAY}](https://adventofcode.com/2020/day/${DAY})" >> $DAY_DIR/README.md
    
done

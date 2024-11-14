#!/bin/bash
pipenv run python3 main.py -i datasets/reduced_balanced_kronodroid_emulator.csv  --batch_size 256 --number_epochs 100 --k_fold 2


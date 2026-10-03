# Lexical Decision Task

A lexical decision task written using PsychoPy's Coder, with no Builder. In this experiment, participants decide whether a string of letters is a real word or not.

## What it measures
Reaction time and accuracy when classifying strings as words or non-words (Faster responses to words than to non-words are the most common outcome).

## How it works
- Stimuli are read from `conditions.csv`. The first column is the letter string and the second column is 1 for a word or 0 for a non-word. The first row is a header and is skipped.
- Trial order is randomized.
- Participants press the right arrow key for a word and the left arrow key for a non-word.
- A fixation cross (+) appears for 1 second between trials.
- Accuracy and reaction time are recorded for each trial and saved to a timestamped file, `results-<timestamp>.csv`.

## How to run
1. Install PsychoPy.
2. Keep `LDT.py` and `conditions.csv` in the same folder.
3. Open `LDT.py` in PsychoPy Coder and press Run.

## Files
- `LDT.py`: the experiment script
- `conditions.csv`: the stimuli

## Note
This is a coder-only script, so it runs locally in PsychoPy and not online through Pavlovia.

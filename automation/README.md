# Automating Astrofox

These features added by moltenform(Ben Fisher).

See also: [astrofox speed tips](./astrofox-speed-tips.md)

## Prereqs

- Python 3
- pywinauto
- currently lnzscript.exe from [here](https://github.com/moltenform/lnzscript)
    - (if you're using this project, should be quick to remove this dependency, let me know)
- Node and Yarn
    - (see astrofox's readme, you'll need enough preqreqs to build astrofox from source)

## Configuration

- edit `components/modals/VideoSettings.js`
    - go to `autoSetVidSettings()`
    - enter your desired output path and frame rate
- edit `go_automate.py`
    - edit configs at top of file
- edit `go_automate_lnz_part.js`
    - edit configs at top of file

## Building

- build astrofox with `yarn build`, refer to its docs

## Running

- run `go_automate.py` and wait.
- it will look at input audio in the directory you provided when you edited the configs at top of the script
- it will start astrofox, do the rendering, and exit.





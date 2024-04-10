# Automating Astrofox

These features added by moltenform(Ben Fisher).

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
- edit 

## Building

- build astrofox with `yarn build`, refer to its docs

## Running

- run `go_automate.py` and wait.
- it will start astrofox, do the rendering, and exit.


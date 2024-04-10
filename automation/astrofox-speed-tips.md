
# astrofox speed tips

These thoughts added by moltenform(Ben Fisher).

- use a ram drive
    - install software like ImDisk (Virtual Disk Driver)
    - create a virtual drive backed by physical ram
    - delete any existing `C:\Users\(username)\AppData\Local\Temp\Astrofox`
    - make symlink that maps `C:\Users\(username)\AppData\Local\Temp\Astrofox` to ram drive

- rendering qualities
    - compare 12fps at low quality vs 8fps at high quality and use what works best

- potential bottlenecks (more research needed)
    - reading large input files from hdd
    - graphics card strength
    - flac to aac conversion
        - (astrofox sets it to 192kpbs)
        - (aac lc, 44100 Hz, stereo, 192 kb/s)
    

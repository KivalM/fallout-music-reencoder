This program will go through the fallout directory recursively and use ffmpeg to reencode all mp3s to 192kbps to avoid skipping of tracks caused by Proton's recent regressions

`USAGE:`

`main.py -d FALLOUTDIRECTORY -b`

`-d or --dir`

    tells the program where to look for fallout.
    
    Default location is $HOME/.local/share/Steam/steamapps/common/Fallout 3 goty
    
    point it to your Data directory. it will work faster
    
`-a or --debug`

    shows the output of ffmpeg  
    
`-b or --nobackup`

    tells the program to delete the unencoded files
    
`-g or --game`

    chooses the game
    
    this is only effective if using the default game directory
    
    i.e not using -d to specify a dir
    
    valid options are '3' and 'nv'
    
    Fallout 3 by default
`-h`

    displays this message
   
 TODO: neaten readme

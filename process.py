#This is the code I used to generate the 144 discs in ItemGenerator.java
for x in range(1,145):
    print('public static final Item DISC_{0:03} = registerItem("disc_{0:03}", new mdpDiscs(14, musicDiscsPlusSE.DISC_{0:03}, DISC_SETTINGS));'.format(x))
print("done")

#This is the code I used to generate the 144 discs in musicDiscPlusSE.java
for x in range(1,145):
    print('public static final SoundEvent DISC_{0:03} = register("disc_{0:03}");'.format(x))
print("done")

#This is the code I used to generate the creeper_drop_music_discs.json
for x in range(1,145):
    print('"musicdiscsplus-pupp:disc_{0:03}",'.format(x))
print("done")

#This is the code I used to generate the en_us.json
for x in range(1,145):
    print('"item.musicdiscsplus-pupp.disc_{0:03}": "Music Disc",'.format(x))
    print('"item.musicdiscsplus-pupp.disc_{0:03}.desc": "Artist - Song Name",'.format(x))
print("done")

#This is the code I used to generate the sounds.json <--- can definitely be improved this was just a brain fart and was needing to get it done
for x in range(1,145):
    print('"disc_{0:03}": '.format(x), end="")
    print("{")
    print('\t"sounds": [')
    print('\t  {')
    print('\t\t"name": "musicdiscsplus-pupp:disc_{0:03}",'.format(x))
    print('\t"stream": true')
    print('  }')
    print(']')
    print('},')
print("done")

#Use this code in a batch file to mass produce the PNG's.
@echo off
setlocal enabledelayedexpansion
set /a count = 1
for /f "delims=" %%a in ('dir *.png /b /a-d ') do (
set "formattedValue=000000!count!"
copy "%%a" "C:\FolderB\disc_!formattedValue:~-3!.png"
set /a count+=1
)

#x
"""Test ANSI formatting codes for console applications."""

print('\x1b[0m Reset / Normal \x1b[0m')
print('\x1b[1m Bold or increased intensity \x1b[0m')
print('\x1b[2m Faint (decreased intensity) \x1b[0m')
print('\x1b[3m Italic \x1b[0m')
print('\x1b[4m Underline \x1b[0m')
print('\x1b[5m Slow Blink \x1b[0m')
print('\x1b[6m Rapid Blink \x1b[0m')
print('\x1b[7m reverse video \x1b[0m')
print('\x1b[8m Conceal \x1b[0m')
print('\x1b[9m Crossed-out \x1b[0m')
print('\x1b[10m Primary(default) font \x1b[0m')
print('Alternative Fonts:')
print('\t\x1b[11m Alternative font 0\x1b[0m')
print('\t\x1b[12m Alternative font 1\x1b[0m')
print('\t\x1b[13m Alternative font 2\x1b[0m')
print('\t\x1b[14m Alternative font 3\x1b[0m')
print('\t\x1b[15m Alternative font 4\x1b[0m')
print('\t\x1b[16m Alternative font 5\x1b[0m')
print('\t\x1b[17m Alternative font 6\x1b[0m')
print('\t\x1b[18m Alternative font 7\x1b[0m')
print('\t\x1b[19m Alternative font 8\x1b[0m')
print('\x1b[20m Fraktur \x1b[0m')
print('\x1b[21m Doubly underline or Bold off \x1b[0m')
print('\x1b[22m Normal color or intensity \x1b[0m')
print('\x1b[23m Not italic, not Fraktur \x1b[0m')
print('\x1b[24m Underline off \x1b[0m')
print('\x1b[25m Blink off \x1b[0m')
print('\x1b[27m Inverse off \x1b[0m')
print('\x1b[28m Reveal \x1b[0m')
print('\x1b[29m Not crossed out \x1b[0m')

print(' Basic Foreground Colors:')
print('\t\x1b[30m Black foreground\x1b[0m')
print('\t\x1b[31m Red foreground\x1b[0m')
print('\t\x1b[32m Green foreground\x1b[0m')
print('\t\x1b[33m Yellow foreground\x1b[0m')
print('\t\x1b[34m Blue foreground\x1b[0m')
print('\t\x1b[35m Magenta foreground\x1b[0m')
print('\t\x1b[36m Cyan foreground\x1b[0m')
print('\t\x1b[37m White foreground\x1b[0m')
print('\t\x1b[39m Default foreground color \x1b[0m')

print(' Basic Background Colors:')
print('\t\x1b[40m Black background\x1b[0m')
print('\t\x1b[41m Red background\x1b[0m')
print('\t\x1b[42m Green background\x1b[0m')
print('\t\x1b[43m Yellow background\x1b[0m')
print('\t\x1b[44m Blue background\x1b[0m')
print('\t\x1b[45m Magenta background\x1b[0m')
print('\t\x1b[46m Cyan background\x1b[0m')
print('\t\x1b[47m White background\x1b[0m')
print('\t\x1b[49m Default background color \x1b[0m')

print('\x1b[51m Framed \x1b[0m')
print('\x1b[52m Encircled \x1b[0m')
print('\x1b[53m Overlined \x1b[0m')
print('\x1b[54m Not framed or encircled \x1b[0m')
print('\x1b[55m Not overlined \x1b[0m')
print('\x1b[60m ideogram underline or right side line \x1b[0m')
print(
    '\x1b[61m ideogram double underline or double line on the right side \x1b[0m'
)
print('\x1b[62m ideogram overline or left side line \x1b[0m')
print(
    '\x1b[63m ideogram double overline or double line on the left side \x1b[0m'
)
print('\x1b[64m ideogram stress marking \x1b[0m')
print('\x1b[65m ideogram attributes off \x1b[0m')

print(' Bright Foreground Colors:')
print('\t\x1b[90m Bright Black foreground\x1b[0m')
print('\t\x1b[91m Bright Red foreground\x1b[0m')
print('\t\x1b[92m Bright Green foreground\x1b[0m')
print('\t\x1b[93m Bright Yellow foreground\x1b[0m')
print('\t\x1b[94m Bright Blue foreground\x1b[0m')
print('\t\x1b[95m Bright Magenta foreground\x1b[0m')
print('\t\x1b[96m Bright Cyan foreground\x1b[0m')
print('\t\x1b[97m Bright White foreground\x1b[0m')

print(' Bright Background Colors:')
print('\t\x1b[100m Bright Black background\x1b[0m')
print('\t\x1b[101m Bright Red background\x1b[0m')
print('\t\x1b[102m Bright Green background\x1b[0m')
print('\t\x1b[103m Bright Yellow background\x1b[0m')
print('\t\x1b[104m Bright Blue background\x1b[0m')
print('\t\x1b[105m Bright Magenta background\x1b[0m')
print('\t\x1b[106m Bright Cyan background\x1b[0m')
print('\t\x1b[107m Bright White background\x1b[0m')

print('\nComplex Colors (8-bit)\n')
print('Foreground')

fgch = "█"
bgch = " "

printString = "  "
for i in range(0, 16):
    printString += f'\x1b[38;5;{i}m{fgch} \x1b[0m'
print(printString)
printString = ""
for i in range(16, 232):
    printString += f'\x1b[38;5;{i}m{fgch}\x1b[0m'
    if ((i - 15) % 36) == 0:
        print(printString)
        printString = ""
print(printString)
printString = "      "
for i in range(232, 256):
    printString += f'\x1b[38;5;{i}m{fgch}\x1b[0m'
print(printString)

print('Background')
printString = "  "
for i in range(0, 16):
    printString += f'\x1b[48;5;{i}m{bgch} \x1b[0m'
print(printString)
printString = ""
for i in range(16, 232):
    printString += f'\x1b[48;5;{i}m{bgch}\x1b[0m'
    if ((i - 15) % 36) == 0:
        print(printString)
        printString = ""
print(printString)
printString = "      "
for i in range(232, 256):
    printString += f'\x1b[48;5;{i}m{bgch}\x1b[0m'
print(printString)

print('\nComplex Colors (24-bit)\n')
INC = 20
printString = ""
newLine = 0
for r in range(0, 256, INC):
    for g in range(0, 256, INC):
        for b in range(0, 256, INC):
            printString += f'\x1b[38;2;{r};{g};{b}m{fgch}\x1b[0m'
            newLine += 1
            if newLine > 90:
                print(printString)
                printString = ""
                newLine = 0
print(printString)
printString = ""

printString = ""
newLine = 0
for r in range(0, 256, INC):
    for g in range(0, 256, INC):
        for b in range(0, 256, INC):
            printString += f'\x1b[48;2;{r};{g};{b}m{bgch}\x1b[0m'
            newLine += 1
            if newLine > 90:
                print(printString)
                printString = ""
                newLine = 0
print(printString)
printString = ""
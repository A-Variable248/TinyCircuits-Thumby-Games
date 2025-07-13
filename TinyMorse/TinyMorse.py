import thumby
from time import sleep


def decodecm():
    global current_morse
    a = "".join(current_morse)
    global showEn
    if a not in morse:
        showEn.append("#")
    else:
        showEn.append(en[morse.index(a)])
def update():
    thumby.display.fill(0)
    thumby.display.drawText("".join(showMorse), 2, 2, 1)
    thumby.display.drawText("".join(showEn), 2, 19, 1)
    thumby.display.update()


thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ".-.-.-", "-....-", "--..--", "..--..", "-..-.", ".----."]
en = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", ",", "?", "/", "'"]
showEn = [""]
showMorse = [""]
current_morse = [""]
thumby.display.fill(0)
thumby.display.drawText("A - dash", 4, 4, 1)
thumby.display.drawText("B - dot", 4, 12, 1)
thumby.display.drawText("^ - space", 4, 20, 1)
thumby.display.drawText("v - slash", 4, 28, 1)
thumby.display.update()
sleep(4)
thumby.display.fill(0)
thumby.display.drawText("< - delete from", 4, 4, 1)
thumby.display.drawText("current letter", 4, 12, 1)
thumby.display.drawText("> - exit", 4, 20, 1)
thumby.display.update()
sleep(3)
thumby.display.fill(0)
thumby.display.update()
while 1:
    if thumby.buttonA.justPressed():
        current_morse.append("-")
        showMorse.append("-")
        update()
    elif thumby.buttonB.justPressed():
        current_morse.append(".")
        showMorse.append(".")
        update()
    elif thumby.buttonU.justPressed():
        decodecm()
        current_morse = [""]
        showMorse.append(" ")
        update()
    elif thumby.buttonD.justPressed():
        showEn.append(" ")
        showMorse.append("/")
        current_morse = [""]
        update()
    elif thumby.buttonL.justPressed() and len(current_morse) >= 1:
        current_morse.pop()
        showMorse.pop()
        update()
    elif thumby.buttonR.justPressed():
        break

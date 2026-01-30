def game():
    return 4462324# if old score is less than this then this score will be overide with that score .but when new score is less than old score then its not do any changes on it

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()

if  hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
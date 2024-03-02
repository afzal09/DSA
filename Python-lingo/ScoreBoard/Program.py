from GameEntry import GameEntry
from ScoreBoard import ScoreBoard

Bob = "Bob"
new_1 = GameEntry(Bob,0)
new_2 = GameEntry(Bob,500)
new_3 = GameEntry(Bob,1000)
new_4 = GameEntry(Bob,1500)
new_5 = GameEntry(Bob,2000)
new_6 = GameEntry(Bob,2500)
new_7 = GameEntry(Bob,3000)
new_8 = GameEntry(Bob,3500)
new_9 = GameEntry(Bob,4000)
new_10 = GameEntry(Bob,4500)
new_11 = GameEntry(Bob,5000)

ScoreBoard = ScoreBoard()
ScoreBoard.add(new_1)
ScoreBoard.add(new_2)
ScoreBoard.add(new_3)
ScoreBoard.add(new_4)
ScoreBoard.add(new_5)
ScoreBoard.add(new_6)
ScoreBoard.add(new_7)
ScoreBoard.add(new_8)
ScoreBoard.add(new_9)
ScoreBoard.add(new_10)
print(str(ScoreBoard))
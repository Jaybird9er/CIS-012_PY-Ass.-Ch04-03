import RPSMod

print("Enter [R]ock, [P]aper, or [S]cissor")
print("Player: ", end = '')
playersMove = RPSMod.collectStringInput()


# Can't figure out why, but for some reason chr casting isn't working as expected
computersMove = RPSMod.generateIntegerValue()
print("Computer's selection:", chr(computersMove))
print(RPSMod.evaluateWinning(playersMove, computersMove))

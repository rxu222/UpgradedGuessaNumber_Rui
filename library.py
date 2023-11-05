def loadTopPlayers(topPlayerFile):
    # Create an empty list to store the top players' data
    topPlayers = []
    with open(topPlayerFile, 'r') as file:
        # Read the content of the top players' file line by line
        for line in file:
            # Extract the score and player name from each line
            score = int(line[:10].strip())
            playerName = line[10:].strip()
            # Append the score and player name as a tuple to the topPlayers list
            topPlayers.append((score, playerName))
    return topPlayers

def writeTopPlayers(topPlayers, topPlayerFile):
    # Write the top players' data back to the top players' file
    with open(topPlayerFile, 'w') as file:
        for score, playerName in topPlayers:
            file.write(f"{score:<10}{playerName}\n")

def updateTopPlayers(playerName, score, topPlayerFile):
    # Load the current top players' data
    topPlayers = loadTopPlayers(topPlayerFile)
    # Add the new score and player name to the top players' list
    topPlayers.append((score, playerName))
    # Sort the top players by score (in ascending order)
    topPlayers.sort(key=lambda x: x[0])
    # Trim the top players' list to retain the top 5 players
    topPlayers = topPlayers[:5]
    # Write the updated top players' data back to the top players' file
    writeTopPlayers(topPlayers, topPlayerFile)
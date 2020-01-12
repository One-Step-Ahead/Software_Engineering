# Learning_Wizard
Learning Wizard is supposed to be a software that enables humans to learn the card game "Wizard".
To help this process we are going to add in a AI client in the future that will learn the
game by playing the game versus instances of itself. That way it will pose a serious challange
to human opponents.

# Download
Note that we currently only support Windows!

Newest release v0.3.2 [Download here!](https://mega.nz/#!MHIBGSaI!C9_VPklvqxs8ffFHEZoaBrn9Df-oAHzToYRv2iskqwQ)

old releases [Check here!](https://mega.nz/#F!YWpSTCAK!uZkUggHo8zuiiqHlUfWVLA)

# How to Play
The game can be played by 3, 4, 5 or 6 players.  
It consists of 60 Cards.  
There are 4 Sets of Cards each with numbers 1 to 13.  
The 4 sets are different in color. There is Red, Yellow, Green, and Blue.  
Additionally to those cards there are 4 jesters (marked [n] on the cards) and 4 wizards (marked [z] on the cards). 
* The wizard is the most powerful card in the game, he defeats any other card BUT another wizard. 
* The jester is the weakest card in the game, who can't beat any other card EXCEPT if there are 4 players each playing a jester.
In that case the first played jester wins.
    
The goal of the game is, like in many other game to achieve the highest score.  
This is done by predicting how many "Stiche"(=tricks) you are going to make with the hand you are given.  
* If you predict right you get +20 Point.  
* If you make a Stich you get +10 Points.  
* For every Stich that deviates from your predicted number of Stiche you get -10 each.

The game starts at Player 1. He "deals" the cards and is the First to play. In the second round Player 2 "deals" the cards and is the first to play, in the third Player 3 and so on...  
Also, in the first round, everyone gets one card dealt. In the second round everyone gets delt two cards and so on...  

At the start of every round there is a Atut determined at random from the deck. 
* If the card is a wizard the player that would be first to go determines the atut. 
* If the card is a jester, there is no atut for this round.  

The first card that is played in every Stich dictates the color that has to be serverd.  
So for example if player 1 plays a red card, all other players HAVE to play a red card as well IF the HAVE one on their hand.  
There are 2 exceptions to this rule:
* The jester [n] and 
* the wizard [z] can be played at any time.  
  
We hope that you enjoy playing. 
# WIP
We are aware that the current state of the game is a bit half-baked. BUT be assured that we continue working on this project
to realize our original idea(s).  
The first one, a GUI is almost ready to go, but you know... deadlines ;)
The second one, a functional AI client needs a lot more work. We have informed ourselves about the subject but its a tough one.  

# Settings

To play the game, you do not need to change any of the default settings.

# MoSCoW
After a few alterations to our goals the implemented requirements are as follows:
* The game has to be playable for 4 players
* The rules of Atut apply
* Your own playing cards (your hand) is visible on the CLI
* The score gets calculated after every trick (Stich)
* After the cards are dealt, predictions about the number of won tricks (Stiche) are made
* The Game consists of 4 decks of red, green, blue and yellow, with 13 cards each and 8 special cards
* Each color of cards has values from 1 to 13
* The 8 special cards are 4 jesters and 4 wizards
* Jesters never win (except if there are 4 in the same trick) and can be played at any time
* The game ends if there are no cards left to determine the Atut (then the last round is played)
* Follow suite rule applies (Farbzwang)
* After every round, one more card is dealt at the start of the next round.
* The player to start the round cycles trough the participants of the game(first round player 1, second round player 2 ,...)
* At the start of every round the Atut is determined from the remaining cards that were not dealt. If the card is a 
jester, there is no atut for that round, if the card is a wizard the player that would start the round decides which color it will be
* In the last round there is never a atut
* After the last round concludes, the player with the highest score wins the game. If there are equal scores, all players
with the same score share the victory.
* It is visible which cards were played by the players previous in the same stich.
* At the end of every round no player may be left with cards on their hand
* At the start of the game, every player can choose a name. If no name is choosen, a random name will be assigned.

## Player Options
If you want to configure something you need tho change the values in the **engine.py**.
* player_count = number of players that will be playing the game
    * the game supports 3 - 6 players

## Developer Options
* cli_inputs = False [default]
    * enables/disables CLI MODE

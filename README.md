# Learning_Wizard
Learning Wizard is supposed to be a software that enables humans to learn the card game "Wizard".
To help this process we are going to add in a AI client in the future that will learn the
game by playing the game versus instances of itself. That way it will pose a serious challange
to human opponents.

# Download
Note that we currently only support Windows!

Newest release v0.3.1 [Download here!](https://mega.nz/#!pagETK7Z!5rX1p-uORL3te_MdQyGxS94RwfPP_HmylGgYPWzNAko)

release v0.3 [Download here!](https://mega.nz/#!BOxShawC!q4xrEJF2lWVVrgR-LScQ-HJ6SXt_SKfgSW_h2p0EeA8)
release v0.2 [Download here!](https://mega.nz/#!0SgjBISQ!ZuFUesRufZHjW1fDlBoqfrtkgvIAIDTIHLkeu4QNi6s)

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

## Player Options
If you want to configure something you need tho change the values in the **engine.py**.
* player_count = number of players that will be playing the game
    * the game supports 3 - 6 players

## Developer Options
* cli_inputs = False [default]
    * enables/disables CLI MODE

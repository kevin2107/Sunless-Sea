# Change Log
#Wishlist:
#Exception catcher for whole script using main
#Create map
#update Map() so its only shown when you are 'fill up' and you have created a port report.

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
The changelog was created 3-4 weeks after the project began so changes before then have not been recorded.

##[Latest] = 2016-03-31
### Added
-Diagloue for King's Hut, finished all interactions with king.
    -You must be "filled up" to access the king's quest otherwise he will shoo you away.

### Changed
-Fixed minor typo-graphical errors. Changed the diaglogue a bit of goback() and interaction with the villagers.
-Fixed a few forgotten lines of code that would interfare with the go back function

##[Latest] = 2016-03-30
### Added
-Created a yes or no function with a dictionary so we can have an easier time guessing the users input.
### Changed
-Put an exception catcher over the secret map to avoid errors for now.
-changed leaveport()'s exit() to sys.exit("You are dead"). Will change rest of exit's later.

## [Latest] - 2016-03-29
### Changed
-Created a much more efficient function for the hue lights, lights(color,brightness)
        -Still a little messy, will rework more later.

## [Latest] - 2016-03-28
### Changed
-Fixed exceptions thrown from Phue if bridge not detected, by using Try: except: pass. If the Phue code runs and throws an exception it is now bypassed.

## [Latest] - 2016-03-27
### Added
-New dependency Phue
-Added ability to use phillip hue lights(Experimental and will not work if bridge I.P is not manually changed in script, will automate later.)
-Added new colorchange 

## [Latest] - 2016-03-26
### Added
-Added new sounds to give new dimension of story. Pageflips, screams, zombie sounds, typewriter.

## [Latest] - 2016-03-25
### Added
-New dependency Pyglet
-Added music using the Pyglet module
-Cannot use MP3 files. Converted them to .Wav format.
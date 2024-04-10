

var config = {}
	
// load a saved astrofox project
config.projectTemplate = 'D:\\project.afx'

// seconds to wait audio load
// if input audio is more than ~2 hrs, you might need to increase this
// if input audio is more than ~5 hrs, astrofox might fail load the file
config.secondsWaitForAudio = 20
	
// open astrofox, then maximize the window
// load an audio file, go to render, then get the coords of the center of the START button
config.btnStartCoordX = 935
config.btnStartCoordY = 781

// get this from the cmd line args
config.audioToLoad = argv[1]


function go() {
	sleepBetweenActions()
	Keyboard.send('<Control><Alt>o');
	sleepBetweenActions()
	Keyboard.send('"' + config.projectTemplate + '"')
	sleepBetweenActions()
	Keyboard.send(@'{ENTER}');
	sleepBetweenActions()
	Keyboard.send('<Control><Alt>l');
	sleepBetweenActions()
	
	Keyboard.send(config.audioToLoad);
	sleepBetweenActions()
	
	Keyboard.send(@'{ENTER}');
	sleepBetweenActions()
	
	Time.sleep(config.secondsWaitForAudio * 1000)
	
	Keyboard.send('<Control><Alt>r'); 
	sleepBetweenActions()
	// now wait again, for it to autofill some video settings
	sleepBetweenActions()
	// click on start
	Mouse.click(config.btnStartCoordX, config.btnStartCoordY)
}

function sleepBetweenActions() {
	// add frequent sleeps, to wait for ui to be ready
	Time.sleep(4000)
}


go()



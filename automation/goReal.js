
function go(param) {
	Keyboard.send('<Control><Alt>o'); Time.sleep(4000)
	Keyboard.send(@'"D:\mirr3\devhere\project2d.afx"'); Time.sleep(4000)
	Keyboard.send(@'{ENTER}'); Time.sleep(4000)
	Keyboard.send('<Control><Alt>l'); Time.sleep(4000)

	Keyboard.send(param); Time.sleep(4000)
	Keyboard.send(@'{ENTER}'); Time.sleep(4000)
	// Time.sleep(20 * 1000) // wait  for it to load a big audio---works fpr < 200mb flac
	Time.sleep(32 * 1000) // wait  for it to load a big audio---works fpr < 200mb flac
	
	Keyboard.send('<Control><Alt>r'); Time.sleep(4000)
	Time.sleep(4000) // wait  for it to autofill dest
	Mouse.click(935, 781)
}


//~ go(@'"G:\larger-files-out\results\balaji_srinivasan.mp3.2c.flac"')
//~ print('0' + argv[0])
//~ print('1' + argv[1])
//~ print('2' + argv[2])
go(argv[1])

/*
win.type_keys(r''); time.sleep(1)
win.type_keys('{ENTER}'); time.sleep(4)
win.type_keys('^%L'); time.sleep(4)
#~ win.type_keys(r'"H:\Fujiyama.flac"'); time.sleep(1)
#~ win.type_keys(r'"H:\Fujiyama.flac"'); time.sleep(1)
win.type_keys(r'"D:\mirr3\devhere\w2bsample2short.ogg"'); time.sleep(1)
win.type_keys('{ENTER}'); time.sleep(4)
win.type_keys('^%R'); time.sleep(4)
time.sleep(6) # wait
pywinauto.mouse.click(button='left', coords=(935, 781))*/
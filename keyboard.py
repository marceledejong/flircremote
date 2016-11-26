from evdev import InputDevice, categorize, ecodes


def sendcode(sendkey):
	from socketIO_client import SocketIO, LoggingNamespace
	
	with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
		if sendkey == 'KEY_NEXTSONG':
			socketIO.emit('next')			
		if sendkey == 'KEY_PREVIOUSSONG':
			socketIO.emit('prev')
		if sendkey == 'KEY_VOLUMEUP':
			socketIO.emit('volume','+')
		if sendkey == 'KEY_VOLUMEDOWN':
			socketIO.emit('volume','-')
		if sendkey == 'KEY_PLAYPAUSE':
			print 'play/pause'
			socketIO.emit('getstate', status)
			print status
			if status == 'play':
				socketIO.emit('pause')
				status = 'pause'
			else:
				socketIO.emit('play')
				status = 'play'
				

		socketIO.wait(seconds=1)

status = 'pause'
device = InputDevice("/dev/input/event0") # my keyboard
for event in device.read_loop():	
    if event.type == ecodes.EV_KEY:
		keybrd = categorize(event)
		if keybrd.keystate == keybrd.key_down:			
			print keybrd
			sendcode(keybrd.keycode)
		
				

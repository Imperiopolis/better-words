from event_monitor import EventMonitor
from os import environ

# Start the event monitor
if 'PORT' in environ:
	port = environ['PORT']
else:
	port = 3000
print port

EventMonitor().start(port=port)

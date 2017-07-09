from event_monitor import EventMonitor
from os import environ

# Start the event monitor
print environ['PORT']
EventMonitor().start(environ['PORT'] or 3000)

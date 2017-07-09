from event_monitor import EventMonitor
from os import environ

# Start the event monitor
EventMonitor().start(environ['PORT'] || 3000)

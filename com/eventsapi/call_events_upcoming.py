from libs.events.upcomingEventCaller import callUpcomingEvent
from libs.fileSaver import save
import json

jsonObj = callUpcomingEvent()

save(json.dumps(jsonObj), "./upcoming.json")



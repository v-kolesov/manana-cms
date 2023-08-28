from core.observer import observer


# Create an instance of the Observer class



from pydantic import BaseModel
class Event(BaseModel):
    a: str = None
    b: str = None
    c: str = None
    
    

event = Event()


# Using the observe decorator
@observer.observe("core.audience.a")
def a(event, ctx):
    event.a = 1
    return event
    
    


@observer.hook("before", "core.audience.a")
@observer.observe("core.audience.b")
def b(event, ctx):
    event.b = 2
    return event
    

@observer.hook("after", "core.audience.b")
def c(event, ctx):
    import ipdb; ipdb.set_trace()
    event.c = 3 
    return event   

tut = a(event, "context_data")
print("Final event:", tut)

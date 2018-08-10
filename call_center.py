class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "ID: " + str(self.id)
        print "Name: " + self.name
        print "Phone Number: " + self.number
        print "Time of Call: " + self.time
        print "Reason for Call: " + self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.call = []
        self.queue_list = len(self.call)

    def add(self, arg):
        self.call.append(arg)
        return self

    def remove(self):
        self.call.pop(0)
        return self
    
    def info(self):
        for key in self.call:
            self.queue_list = len(self.call)
            print "Name: " + key.name + " at: " + key.number + ". Length of queue: " + str(self.queue_list)
        return self


caller1 = Call(123, "Chris", "555-555-5555", "9:15", "My codes not working")
caller2 = Call(123, "Shrek", "255-235-5555", "8:00", "gert out me swamp")
incoming_call = CallCenter()
print incoming_call.add(caller1).add(caller2).info().remove().info()

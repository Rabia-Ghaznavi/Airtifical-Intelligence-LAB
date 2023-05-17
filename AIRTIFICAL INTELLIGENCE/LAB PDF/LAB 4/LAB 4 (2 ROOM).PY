
from abc import abstractmethod


class Environment(object):

    # An abstract method that all subclasses must override
    @abstractmethod
    def __init__(self, agent, rooms):
        self.agent = agent
        self.rooms = rooms
        self.currentRoom = self.rooms[0]

    # An abstract method that all subclasses must override
    @abstractmethod
    def executeStep(self, n=1):
        if n <= 0:
            return

        self.agent.sense(self)
        action = self.agent.act()

        if action == 'clean':
            self.currentRoom.status = 'clean'
            print(f"Room {self.currentRoom.location} IS CLEAN NOW")
        elif action == 'right':
            self.currentRoom = self.rooms[1]
            self.executeStep(n - 1)
        elif action == 'left':
            self.currentRoom = self.rooms[0]
            self.executeStep(n - 1)

    # An abstract method that all subclasses must override
    @abstractmethod
    def executeAll(self):
        while any(room.status == 'dirty' for room in self.rooms):
            self.executeStep()

    def delay(self, n=100):
        self.delay = n


class Room:

    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


class Agent(object):

    # An abstract method that all subclasses must override
    @abstractmethod
    def __init__(self):
        pass

    # An abstract method that all subclasses must override
    @abstractmethod
    def sense(self, environment):
        pass

    # An abstract method that all subclasses must override
    @abstractmethod
    def act(self):
        pass


class VaccumAgent(Agent):

    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            print(f"Room {self.environment.currentRoom.location} IS CURRENTLY DIRTY")
            print(f"Cleaning Room {self.environment.currentRoom.location}...")
            return 'clean'

        if self.environment.currentRoom.location == 'A':
            print(f"Currently in Room {self.environment.currentRoom.location}.")
            print("Moving to the next Room.")
            return 'right'

        if self.environment.currentRoom.location == 'B':
            print(f"Currently in Room {self.environment.currentRoom.location}.")
            print("Moving to the next Room.")
            return 'left'
# The main function that creates the environment, agent, and rooms,
# and then executes the cleaning process
if __name__ == '__main__':
    roomA = Room('A', 'dirty')
    roomB = Room('B', 'dirty')
    rooms = [roomA, roomB]
    vcagent = VaccumAgent()
    env = Environment(vcagent, rooms)
    env.executeAll()
    print("Environment Cleaned Successfully!")
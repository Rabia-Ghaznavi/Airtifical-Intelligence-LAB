from abc import abstractmethod
import time


class Environment(object):

    @abstractmethod
    def __init__(self, agent, rooms):
        self.agent = agent
        self.rooms = rooms
        self.currentRoom = self.rooms[0]

    @abstractmethod
    def executeStep(self, n=1):
        if n <= 0:
            return

        self.agent.sense(self)
        action = self.agent.act()

        if action == 'clean':
            self.currentRoom.status = 'clean'
        elif action == 'right':
            index = self.rooms.index(self.currentRoom)
            if index < len(self.rooms) - 1:
                self.currentRoom = self.rooms[index + 1]
            self.executeStep(n - 1)
        elif action == 'left':
            index = self.rooms.index(self.currentRoom)
            if index > 0:
                self.currentRoom = self.rooms[index - 1]
            self.executeStep(n - 1)

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

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

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
            print(f"Room {self.environment.currentRoom.location} is currently Dirty :(")
            print(f"Cleaning Room {self.environment.currentRoom.location}...")
            print(f"Room {self.environment.currentRoom.location} is clean now :)")
            return 'clean'

        if self.environment.currentRoom.location == 'A':
            print(f"Currently in Room {self.environment.currentRoom.location}.")
            print("Moving to the next Room.")
            return 'right'

        if self.environment.currentRoom.location == 'H':
            print(f"Currently in Room {self.environment.currentRoom.location}.")
            print("Moving to the previous Room.")
            return 'left'

        if self.environment.currentRoom.location in ['B', 'C', 'D', 'E', 'F', 'G']:
            print(f"Currently in Room {self.environment.currentRoom.location}.")
            if self.environment.currentRoom.location in ['B', 'C', 'D', 'E']:
                print("Moving to the next Room.")
                return 'right'
            else:
                print("Moving to the previous Room.")
                return 'left'


if __name__ == '__main__':
    roomA = Room('A', 'dirty')
    roomB = Room('B', 'dirty')
    roomC = Room('C', 'dirty')
    roomD = Room('D', 'dirty')
    roomE = Room('E', 'dirty')
    roomF = Room('F', 'dirty')
    roomG = Room('G', 'dirty')
    roomH = Room('H', 'dirty')
    rooms = [roomA, roomB, roomC, roomD, roomE, roomF, roomG, roomH]
    vcagent = VaccumAgent()
    env = Environment(vcagent, rooms)
    env.executeAll()
    print("Environment Cleaned Successfully!")

# No, the agent in the given implementation does'nt stoped until All Rooms are Cleaned. It keeps moving between the two rooms in a loop, checking and cleaning the rooms if they are dirty.

# To make the Agent stop after cleaning all the Rooms, we can modify the #executeAll() method in the Environment class to stop the execution when all rooms are Clean.
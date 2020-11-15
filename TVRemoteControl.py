import random
import time


class RemoteControl():

    def __init__(self, tv_condition="Off", tv_volume=0, channellist=["Trt"], channel="Trt"):
        self.tv_condition = tv_condition
        self.tv_volume = tv_volume
        self.channellist = channellist
        self.channel = channel

    def TurnOnTV(self):
        if self.tv_condition == "On":
            print("TV is already on")
        else:
            print("Opening")
            self.tv_condition = "On"

    def TurnOffTV(self):
        if self.tv_condition == "Off":
            print("TV is already off")
        else:
            print("Closing")
            self.tv_condition = "Off"

    def VolumeSetting(self):

        while True:
            answer = input("Volume down: '<'\n Volume up: '>'\n Exit: exit ")

            if answer == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print(self.tv_volume)
            elif answer == ">":
                if self.tv_volume != 31:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)

            else:
                print("Volume is updated:", self.tv_volume)
                break

    def AddChannel(self, channel_name):
        print("Channel is adding..")
        time.sleep(1)
        self.channellist.append(channel_name)

    def RandomChannel(self):
        channel_random = random.randint(0, len(self.channellist) - 1)
        self.channel = self.channellist[channel_random]
        print("Channel on TV:", self.channel)

    def __len__(self):
        return len(self.channellist)

    def __str__(self):
        return "TV Condition: {}\nTV Volume: {}\nChannel: {}\nChannel List:{}".format(self.tv_condition, self.tv_volume, self.channel,self.channellist)


controller = RemoteControl()

print("""
TV Application

1. Turn On TV

2. Turn Off TV

3. Volume Setting

4. Adding Channel

5. Learning Number of Channels

6. Random Channel

7. TV Information

To exit press "q"

""")

while True:

    operation = input("Please chose the operation: ")

    if operation == "q":
        print("Operation is end")
        break

    elif operation == "1":
        controller.TurnOnTV()

    elif operation == "2":
        controller.TurnOffTV()

    elif operation == "3":
        controller.VolumeSetting()

    elif operation == "4":
        channel_names = input("Channels should be entered with ',':")
        channel_list = channel_names.split(",")

        for channel in channel_list:
            controller.AddChannel(channel)

    elif operation == "5":
        print("Number of Channel:", len(controller))

    elif operation == "6":
        controller.RandomChannel()

    elif operation == "7":
        print(controller)

    else:
        print("Invalid operation..")

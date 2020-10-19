from time import sleep


class TrafficLight:
    __colour = ["Red!", "Yellow", "Green!"]

    def traf(self):
        i = 0
        while i < 3:
            print(f"Traffic light's colour is \n" f"{TrafficLight.__colour[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1



TrafficLight = TrafficLight()
TrafficLight.traf()
print("Trfficlight is over")

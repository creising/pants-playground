import time

import zmq

random_facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "Octopuses have three hearts. Two hearts pump blood to the gills, while the third pumps it to the rest of the body.",
    "The Great Wall of China is not visible from space with the naked eye, contrary to popular belief. It's often too narrow and blends in with the natural landscape.",
    "The world's smallest mammal is the bumblebee bat, which weighs about as much as a paperclip.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The Eiffel Tower can grow up to 6 inches (15 centimeters) taller during the summer due to the expansion of the iron in the heat.",
    "Cows have best friends and can become stressed when they're separated from them.",
    "Bananas are berries, but strawberries are not true berries – they're considered aggregate fruits.",
    "There are more than 1,500 active volcanoes in the world, with around 50 to 70 erupting each year.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes."
]


def log_it(input):
    print(input, flush=True)


def main():
    log_it("Starting server!")
    context = zmq.Context()
    log_it("Created context")
    socket = context.socket(zmq.REP)
    log_it("Created socket")
    socket.bind("tcp://0.0.0.0:5555")
    log_it("Bound to local host. Waiting for data")

    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        number = int(message)
        log_it(f"Received request!: {message}")

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        index = number % len(random_facts)
        fact = random_facts[index]
        log_it(f"Index: {index} with fact {fact}")
        socket.send_string(fact)
        log_it("message sent")

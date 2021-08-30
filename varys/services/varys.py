import logging


class Varys:  # Engine
    def __init__(self):
        pass

    def listen(self):
        logging.info('Listening...')

    def respond(self):
        logging.info('Responding...')


MasterOfWhispers = Varys()

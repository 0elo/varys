from varys.services import MasterOfWhispers


def publish():
    MasterOfWhispers.listen()


def bulk_publish():
    MasterOfWhispers.listen()

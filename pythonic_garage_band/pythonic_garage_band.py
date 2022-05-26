class Band():
    instances = []

    def __init__(self, name, members=None):

        if members is None:
            members = []

        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solo_list = []
        for member in self.members:
            solo_list.append(member.play_solo())
        return solo_list

    @classmethod
    def to_list(cls):
        return cls.instances



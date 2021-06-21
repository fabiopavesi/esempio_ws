class Waveform:
    def __init__(self, persistence_manager):
        self.persistence_manager = persistence_manager
        pass

    def save(self):
        return self.persistence_manager.save()


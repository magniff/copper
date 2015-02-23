class SourceDepleted(Exception):
    def __init__(self):
        self.value = 'End of stream.'

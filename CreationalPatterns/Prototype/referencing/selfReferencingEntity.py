class SelfReferencingEntity:
    def __init__(self) -> None:
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent
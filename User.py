import time

class User:
    
    def __init__(self, email, password, timestamp=time.time()) -> None: #constructeur 
        self.email = email
        self.password = password
        self.timestamp = timestamp

    @classmethod
    def fromdict(cls, d: dict):
        """convetir dict to class object"""
        allowed = ('email', 'password', 'timestamp')
        df = {k: v for k, v in d.items() if k in allowed}
        return cls(**df)
    
    def __str__(self) -> str:
        return self.email

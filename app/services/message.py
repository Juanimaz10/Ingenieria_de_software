from dataclasses import dataclass


@dataclass
class Message():
    message:str = ''
    code:str = ''
    data:dict = None

@dataclass(init=False)
class MessageBuilder():
    message:str = ''
    code:str = ''
    data:dict = None
    
    def build(self):
        return Message(message=self.message, code=self.code, data=self.data)

    def add_message(self, message:str) -> 'MessageBuilder':
        self.message = message
        return self

    def add_code(self, code:str)-> 'MessageBuilder':
        self.code = code
        return self 
    
    def add_data(self, data:dict)-> 'MessageBuilder':
        self.data = data
        return self
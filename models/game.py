from models.base import Base 
from sqlalchemy import Column, Integer, String, Float

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    game_name = Column(String)
    platform = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
    def __repr__(self) -> str:
        return f"- {self.game_name} - {self.platform} - R${self.price} - {self.quantity}."
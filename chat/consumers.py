import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
  
  async def connect(self):
    # Acepta la conexión
    await self.accept()

    # Enviar estado de la conexión al usuario
    await self.send(text_data=json.dumps({
      'message': 'You are connected to the Echo Room!',
      'status': 'connected'
    }))

  async def disconnect(self, close_code):
    # Enviar estado de desconexión
    await self.send(text_data=json.dumps({
      'message': 'You have been disconnected!',
      'status': 'disconnected'
    }))

  async def receive(self, text_data):
    # Recibe el mensaje del usuario
    text_data_json = json.loads(text_data)
    message = text_data_json['message']

    # Enviar el mismo mensaje de vuelta (echo)
    await self.send(text_data=json.dumps({
        'message': f"{message}"
    }))
        
        
        
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne import Application, ServiceBase, rpc

from suds.client import Client


client = Client("http://localhost:8000/?wsdl")
result = client.service.suma(3, 4)
print(result)
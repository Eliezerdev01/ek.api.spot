from flask import Flask
import json, os
from a2wsgi import WSGIMiddleware

class ApiServerAllocator(object):
    def __init__(self, data={}):
        self.version = "0.1"
        self.data = data
        self.__author__ = "eliezerkenya.net"
        
    def _api_encoder_(self):
        json_inst = json.JSONEncoder()
        json_inst = json_inst.encode(self.data)
        return json_inst
    
    def _serv_decorder_(self):
        pass
    

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  
    
@app.route("/")
def index():
    return "This server is temporarily moved and outdated, out of service but expected to be opened soon, thank you"
    
@app.route("/main")
def main():
    with open("api-json-samp.json", "r") as rd:
        rd = {"feed": rd.read()}
    return rd
            
@app.route("/api/api-post-req/serv/api", methods=["GET","POST"])
def get_my_api():
    data = {}
    get = ApiServerAllocator(data=data)
    data = get._api_encoder_()
    return data
    
app = WSGIMiddleware(app)
from tornado import websocket, web, ioloop
import json
conns = []

#class IndexHandler(web.RequestHandler):
#    def get(self):
#        self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("Connect client")
        if self not in conns:
            conns.append(self)

    def on_close(self):
        print("Disconnect client")
        if self in conns:
            conns.remove(self)
            
    def on_message(self, message):
        try:
            print(message)
            decoded = json.loads(message)
            print(decoded)
            import datetime
            t = datetime.datetime.now()
            decoded["timestamp"] = t.strftime('%m/%d/%Y %H:%M:%S')
            for conn in conns:
                #if conn != self:                    
                conn.write_message(decoded)
        except:
            pass



#class ApiHandler(web.RequestHandler):

#    @web.asynchronous
#    def get(self, *args):
#        self.finish()
#        id = self.get_argument("id")
#        value = self.get_argument("value")
#        data = {"id": id, "value" : value}
#        data = json.dumps(data)
#        for c in cl:
#            c.write_message(data)

#    @web.asynchronous
#    def post(self):
#        pass

app = web.Application([
    #(r'/', IndexHandler),
    (r'/ws', SocketHandler),
    #(r'/api', ApiHandler),
    #(r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    #(r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './'}),
])

if __name__ == '__main__':
    app.listen(8080)
    ioloop.IOLoop.instance().start()
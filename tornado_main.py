import tornado.ioloop
import tornado.web

from banca_dati.mysql_persistence import MysqlPersistence
from banca_dati.pg_persistence import PgPersistence
from banca_dati.waveform import Waveform


class SaveHandler(tornado.web.RequestHandler):
    def post(self):
        waveform = Waveform(persistence)
        result = waveform.save()
        self.write({
            "result": result
        })

class RetrieveHandler(tornado.web.RequestHandler):
    def get(self):
        result = persistence.getHDF5()
        self.write({
            "result": result
        })

def make_app():
    return tornado.web.Application([
        (r"/", SaveHandler),
        (r"/asdf", RetrieveHandler),
    ])

if __name__ == "__main__":

    # Cambiando solo questa assegnazione si punta ad una o all'altra implementazione della banca dati
    # persistence = PgPersistence()
    persistence = MysqlPersistence()

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

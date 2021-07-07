import tornado.ioloop
import tornado.web

from banca_dati.mysql_persistence import MysqlPersistence
from banca_dati.pg_persistence import PgPersistence
from banca_dati.waveform import Waveform

PORT=8888

class SaveHandler(tornado.web.RequestHandler):
    def post(self, banca_dati):
        persistence = None

        print('banca_dati', banca_dati)
        if banca_dati == 'itaca':
            persistence = MysqlPersistence()
        elif banca_dati == 'esm':
            persistence = PgPersistence()

        waveform = Waveform(persistence)
        result = waveform.save()
        self.write({
            "result": result
        })

class RetrieveHandler(tornado.web.RequestHandler):
    def get(self, banca_dati):
        persistence = None
        print('banca_dati', banca_dati)
        if banca_dati == 'itaca':
            persistence = MysqlPersistence()
        elif banca_dati == 'esm':
            persistence = PgPersistence()

        result = persistence.getHDF5()
        self.write({
            "result": result
        })

def make_app():
    return tornado.web.Application([
        # (r"/(.*)", SaveHandler),
        (r"/(.*)/asdf", RetrieveHandler),
    ])

if __name__ == "__main__":

    # Cambiando solo questa assegnazione si punta ad una o all'altra implementazione della banca dati
    # persistence = PgPersistence()
    # persistence = MysqlPersistence()

    app = make_app()
    app.listen(PORT)
    print('Listening on port', PORT)
    tornado.ioloop.IOLoop.current().start()

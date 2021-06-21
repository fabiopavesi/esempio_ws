from banca_dati.persistence import Persistence


class PgPersistence(Persistence):
    def save(self):
        print('saving to Postgres')
        return 'saving to Postgres'
    def getHDF5(self):
        return 'This is the HDF5 file from Postgres-hosted metadata'

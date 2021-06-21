from banca_dati.persistence import Persistence


class MysqlPersistence(Persistence):
    def save(self):
        print('saving to Mysql')
        return 'saving to Mysql'

    def getHDF5(self):
        return 'This is the HDF5 file from MySQL-hosted metadata'

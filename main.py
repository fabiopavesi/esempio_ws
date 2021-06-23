from proxy.persistence_proxy import Persistence
from proxy.waveform_proxy import Waveform

if __name__ == '__main__':
    # print('saving a waveform')
    # waveform = Waveform('http://localhost:8888')
    # print(waveform.save())

    print('retrieving an HDF5 file')
    persistence = Persistence('http://localhost:8888')
    print(persistence.getASDF('IT.CLO..ecc-ecc'))

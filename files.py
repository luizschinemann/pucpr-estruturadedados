from os import listdir
from os.path import isfile, join

PATH = 'listas'

class Files:
    def read_directory(self):
        return [f for f in listdir(PATH) if isfile(join(PATH,f))]

    def create_file(self,file_name):
        if file_name is None:
            print("É necessário informar um nome para o arquivo")
            pass
        else:
            file_name = file_name+'.txt'
            f = open(PATH+'/'+file_name,'w')
            f.close()
            print('Arquivo: {} criado com sucesso!'.format(file_name))
            return

    def insert_word(self,word,file):
        f = open(file, 'w')
        f.write(word)
        f.close()

    def read_file(self,file):
        f = open(file,'r')
        print(f.read())
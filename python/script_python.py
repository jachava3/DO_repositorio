import os #operation system: permite acceder a los comandos de windows 


location = "C:/Users/Thinkpad/Desktop/DATAOPS/python/dataset"

##validar carpeta##

if not os.path.exists(location): ##en caso no exista creo una nueva
    os.mkdir() #make directory
else:
    ##si la carpeta ya existe borramos el contenido
    for root, dirs, files in os.walk(location, topdown=False):##walk para mapear el contenido de una parte
        for name in files:
            os.remove(os.path.join(root, name))##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root, name)) #remove directory / elimino todas mis carpetas 

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate() #para logear autentificacion correcta =  C:\Windows\System32\config\systemprofile\.kaggle

#print(api.dataset_list(search='henryshan')) # para saber los dataset disp[onibles

api.dataset_download_file('henryshan/apple-stock-price','AAPL.csv',path=location,quiet=False)
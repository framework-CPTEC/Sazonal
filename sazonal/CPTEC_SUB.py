# import matplotlib.pyplot as plt
from datetime  import datetime, timedelta
import numpy as np
import pandas as pd
# import Nio
import json
import gc
import pycurl
import io
import xarray as xr
import time, random, glob, shutil, os
import re
import urllib.request

class model(object):

    def __init__(self):

        """ 
            Função para inicializar o configurador do modelo BAM, retorna objeto com a função load habilitada para uso.

            Parametros
            ------------------------------------------------------------------------------------------------------------------------------------------------------       

            * Model     : Para configurar o BAM em novas resoluções altere o campo parameter
            * Variables : Para habilitar novas váriaveis adicionar o nome da variavel e o nome referente dentro do .idx ou .inv
            * Levels    : Define as variaveis com 1 unico nivel ou multiplos
            * Area      : Durante inicialização é adicionado o campo Reduce, quando True os parametros definidos aqui são aplicados para dar zoom em area desejada
            * Transform : Realiza transformação nas unidades das variaveis para uma unidade comum entre os modelos.
            * File      : Nome do arquivo disponivel no ftp
            * Server    : Servidor FTP consumido pela aplicação
            ------------------------------------------------------------------------------------------------------------------------------------------------------       

            Retorna objeto model
        """
        
        self.dict = {   
                    "model"     : {
                                    "name" : "bam",
                                    "parameter" : "TQ0666L064",
                                    "long_name" : "The Brazilian Global Atmospheric Model"
                                },
                    "variables" :  {  
                                     "prec" :  "ensemble_mean" ,
                                     "prec_ca" : "calibrated",
                                     "t2mt" : "ensemble_mean" ,
                                     "t2mt_ca" :  "calibrated",
                                     "psnm" :  "ensemble_mean" ,
                                     "role" :  "ensemble_mean" ,
                                     "tp85" :  "ensemble_mean",
                                     "zg50" :  "ensemble_mean",
                                     "uv85" :  "ensemble_mean" ,
                                     "uv20" :  "ensemble_mean",
                                     "vv85" :  "ensemble_mean",
                                     "vv20" :  "ensemble_mean",
                                     "cr85" :  "ensemble_mean",
                                     "cr20" :  "ensemble_mean"
                 },
                    "products" :   {  
                                    "week" : "week",
                                    "fort" : "fort",
                                    "3wks" : "3wks",
                                    "mnth" : "mnth"
                                },

                    "fields"    : {
                                    "anomalies"            :  "anomalies",
                                    "prob_positve_anomaly" :  "prob_positve_anomaly",
                                    "prob_terciles"        :  "prob_terciles",
                                    "totals"               :  "totals"
                                },

                    "file"    : {
                                    "bin" :     "BAM12_{}00_{}{}.dat"
                                },
            "server":   {
                            "ftp"    :     "http://dataserver.cptec.inpe.br/dataserver_subsaz"
            }
    
        } 


        self.dict.update({'save_netcdf': False})
        self.dict.update({'path_to_save': os.getcwd()})
        data_range = pd.date_range('20230104', datetime.today().strftime('%Y%m%d'), freq='W-WED')
        self.local_path = f"INPE/{self.dict['model']['name']}/{self.dict['model']['parameter']}/brutos"
        self.ftppath = f"/{self.dict['model']['name']}/{self.dict['model']['parameter']}/brutos"

        print(f"\n#### {self.dict['model']['long_name']} ({self.dict['model']['parameter']} / Hybrid) #####\n")
        print("-"*20)
        print(f"Forecast data available for reading.\n")

        i=0
        for dt in data_range:
            i+=1
            if i%5:
                print(dt.date(), end = " - ")
            else:
                print(dt.date())

        print("-"*20)
        print(f"Variables: {self.dict['variables']}")
        print("-"*20)
        print(f"Products: {self.dict['products']}")
        print("-"*20)
        print(f"Field: {self.dict['fields']}")  
        print("-"*20)      
        self.session = random.random()
        model.__clean__()


    def load(self, date=None, var='prec', product='week', field='anomalies', step='01'):

        """
        
        A função load prepara a lista de variaveis, produtos, campos, steps e datas que serão carregadas para memoria.

        Durante execução um diretorio temporario é criado para manipular os arquivos e é apagado assim que finalizada requisição.

        self.date é definido pela frequência que o modelo disponibiliza suas previsões, para o BAM do SUBSAZONAL de 7 em 7 dias.
        
        Parametros
        ------------------------------------------------------------------------------------------------------------       
        date  : Data da condição inicial date=YYYYMMDDHH, use HH para IC 00 e 12.
        step : String com nome o numero do Step disponivel para leitura ['01', '02', '03', '04'],
        var   : String com nome da variavel disponivel para leitura ['t2mt', 'prec'],
        field : String com nome do campo disponivel para leitura ['anomalies', 'prob_positve_anomaly', 'prob_terciles', 'totals'],
        produtc : String com nome do campo disponivel para leitura ['week', 'fort', '3wks', 'mnth']
        ------------------------------------------------------------------------------------------------------------       

        load(date='20240207', var='prec', step='01', product='week',field='anomalies')

        ------------------------------------------------------------------------------------------------------------       
        
        Retorna um Xarray contendo todas variaveis solicitadas com as transformações contidas em self.dict

        ------------------------------------------------------------------------------------------------------------       

        """
        #if (isinstance(steps,int)) : steps = [h for h in range(0, steps+1, 1)]
        if type(date) == int: date = str(date)
        if date == None: date = pd.date_range(datetime.today()+timedelta(days=-7), datetime.today(), freq='W-WED')[0].strftime('%Y%m%d')

        if type(var) == str: var = var
        print(f"var: {var} - date: {date}")

        self.variables = var
        self.product = product
        self.field = field
        self.step = step

        self.date   = date
        self.year   = self.date[0:4]
        self.mon    = self.date[4:6]
        self.day    = self.date[6:8]
        self.hour   = self.date[8:10]

        self.__getrange__()
        if os.path.exists(f".temporary_files/{self.session}"): shutil.rmtree(f".temporary_files/{self.session}")
        
        return self.file


    def __clean__():

        """
            Quando o processo de requisição é interrompido a ferramenta não removerá os arquivos temporarios,
            esta função remove todo diretorio temporario com mais de 2 dias em disco.

        """
        
        if os.path.exists(f".temporary_files"): 

            today = datetime.today()
            
            files = glob.glob(".temporary_files/0.*")
            for f in files:
                duration = today - datetime.fromtimestamp(os.path.getmtime(f))
                if duration.days >= 2:
                    shutil.rmtree(f)
    
    def help(self):

        """
            Função para exibir as informações dos modelos e suas parametrizações.
        
        """
        
        print('help')

    def __getrange__(self):

        """ 
            Função para criar dataframe com informações que serão consumidas por self.__curl__.
            Entre as informações coletadas estão as posições inferior e superior de cada variavel dentro no arquivo grib.

            Exemplo self.setup:
            --------------------------------------------------------------------------------------------------------------       
                forecast_date      upper   id      lower  start_date   var          level step_model varname
            0   2022082300  780016380  195  776016296  2022082300  tp2m  2 m above gnd        anl     t2m
            1   2022082306  780016380  195  776016296  2022082300  tp2m  2 m above gnd        anl     t2m
            --------------------------------------------------------------------------------------------------------------       

        """
        print("__getrange__")
        arr = []



        print(f"{self.dict['file']['bin']}")
        print(f"{self.dict['server']['ftp']}")
        print(f"{self.variables}")
        print(f"{self.dict['variables'][self.variables]}")
        print(f"{self.step}")
             
        invfile = self.dict['file']['bin'].format(self.date,self.product.upper(),self.step)
            #invfile = invfile.split('.grb')[:-1]
        print(invfile)

        # verifica se eh calibrated final _ca e retira 
        var_check = self.variables[:-3] if "_ca" in self.variables else self.variables

            #invfile = f'{self.ftppath}/{self.year}/{self.mon}/{self.day}/{self.hour}/{invfile}.inv'
        print(f"{self.dict['server']['ftp']}/{self.dict['variables'][self.variables]}/{var_check}_{self.product}/{self.field}/{self.year}/{self.mon}/{self.day}/{invfile}")


        try:
            url = (f"{self.dict['server']['ftp']}/{self.dict['variables'][self.variables]}/{self.variables}_{self.product}/{self.field}/{self.year}/{self.mon}/{self.day}/{invfile}")
            response = urllib.request.urlopen(url)
            data_url = response.read()
            dt = np.dtype("f4")
            data = np.frombuffer(data_url,  dtype=dt, count=-1 )
            print(data.size)

            temp = data.reshape(1,192,384)
            print(temp.shape)

            lat = [-89.28423,-88.357,-87.4243,-86.49037,-85.55596,-84.62133,-83.68657,-82.75173,-81.81684,-80.88191  \
            ,-79.94696,-79.01199,-78.07701,-77.14201,-76.20701,-75.27199,-74.33697,-73.40195,-72.46692,-71.53189 \
            ,-70.59685,-69.66182,-68.72678,-67.79173,-66.85669,-65.92165,-64.9866,-64.05155,-63.1165,-62.18145 \
            ,-61.2464,-60.31135,-59.3763,-58.44124,-57.50619,-56.57114,-55.63608,-54.70103,-53.76597,-52.83091 \
            ,-51.89586,-50.9608,-50.02574,-49.09069,-48.15563,-47.22057,-46.28551,-45.35045,-44.4154,-43.48034 \
            ,-42.54528,-41.61022,-40.67516,-39.7401,-38.80504,-37.86998,-36.93492,-35.99986,-35.0648,-34.12974 \
            ,-33.19468,-32.25962,-31.32456,-30.3895,-29.45444,-28.51938,-27.58431,-26.64925,-25.71419,-24.77913 \
            ,-23.84407,-22.90901,-21.97395,-21.03889,-20.10383,-19.16876,-18.2337,-17.29864,-16.36358,-15.42852 \
            ,-14.49346,-13.55839,-12.62333,-11.68827,-10.75321,-9.81815,-8.88309,-7.94802,-7.01296,-6.0779 \
            ,-5.14284,-4.20778,-3.27272,-2.33765,-1.40259,-0.46753,0.46753,1.40259,2.33765,3.27272 \
            ,4.20778,5.14284,6.0779,7.01296,7.94802,8.88309,9.81815,10.75321,11.68827,12.62333 \
            ,13.55839,14.49346,15.42852,16.36358,17.29864,18.2337,19.16876,20.10383,21.03889,21.97395 \
            ,22.90901,23.84407,24.77913,25.71419,26.64925,27.58431,28.51938,29.45444,30.3895,31.32456 \
            ,32.25962,33.19468,34.12974,35.0648,35.99986,36.93492,37.86998,38.80504,39.7401,40.67516 \
            ,41.61022,42.54528,43.48034,44.4154,45.35045,46.28551,47.22057,48.15563,49.09069,50.02574 \
            ,50.9608,51.89586,52.83091,53.76597,54.70103,55.63608,56.57114,57.50619,58.44124,59.3763 \
            ,60.31135,61.2464,62.18145,63.1165,64.05155,64.9866,65.92165,66.85669,67.79173,68.72678 \
            ,69.66182,70.59685,71.53189,72.46692,73.40195,74.33697,75.27199,76.20701,77.14201,78.07701 \
            ,79.01199,79.94696,80.88191,81.81684,82.75173,83.68657,84.62133,85.55596,86.49037,87.4243 \
            ,88.357,89.28423]
            lon = np.linspace(0, 360, 384) 

            ds = xr.Dataset({f'{self.variables}': (['time', 'lat', 'lon'],  temp),},
                coords={'lat': (['lat'], lat),
                        'lon': (['lon'], lon),
                        'time': pd.date_range(f'{self.year}-{self.mon}-{self.day}', periods=1)})

            ds.attrs['center']   = "National Institute for Space Research - INPE"
            ds.attrs['model']   = "The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid)"


            #for var in self.variables:
            #    if var in self.dict['variables']:
            #        value = self.dict['variables'][var]
            #        print(value)
                
            #self.setup = pd.DataFrame(arr, columns=['forecast_date', 'upper', 'id',
            #                                        'lower', 'start_date', 'var', 
            #                                        'level', 'step_model', 'varname'])

            #self.setup.drop_duplicates(inplace=True)
            #self.__curl__()
            print(ds)
            self.file =  ds
        except urllib.error.HTTPError as err:
            print('File not available on server!')
            self.file = None
            return 
        except Exception as e: 
            print(e)
            self.file = None
        


   
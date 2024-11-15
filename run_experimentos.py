"""
Módulo responsavel pela execução de campanhas da ferramenta, incluindo as configurações de experimentos do paper.

Classes:
    IntRange :  Tipo personalizado de argparse que representa um inteiro delimitado por um intervalo.
Funções:
    - print_config : Imprime a configuração dos argumentos para fins de logging.
    - convert_flot_to_int : Converte um valor float para int multiplicando por 100.
    - run_cmd : A função executa um comando de shell especificado e registra a saída.
    - check_files : Verifica se os arquivos especificados existem.
    - main: Função principal que configura e executa as campanhas.
    
"""
# Importação de bibliotecas necessárias
try:
    import sys
    import os
    import argparse
    import logging
    import subprocess
    import shlex
    import datetime
    from logging.handlers import RotatingFileHandler
    from pathlib import Path
    import itertools
    import mlflow
    import pandas as pd

#Tratamento de erro de import
except ImportError as error:
    print(error)
    print()
    print(" ")
    print()
    sys.exit(-1)
COMMAND = "pipenv run python main.py  "
COMMAND2 = "pipenv run python main.py  -ml "
DEFAULT_CAMPAIGN= ['Figura_1', 'Figura_2_a','Figura_2_b','Figura_3','Figura_4']

def list_of_ints(arg):
    return list(map(int, arg.split(',')))
def list_of_floats(arg):
    return list(map(float, arg.split(',')))
# Define a custom argument type for a list of integers
def list_of_strs(arg):
    return list(map(str, arg.split(',')))

def read_function(entrada,ml):
    # Read Excel file with multiple sheets
    xls = pd.read_excel("Tabela_experimentos/tabela_experimentos.xlsx", sheet_name=['Figura_1', 'Figura_2_a','Figura_2_b','Figura_3','Figura_4'])
    # Access individual sheets using sheet name
    sheet_name=entrada
    dic_direct={'Figura_1':"Figura_1/", 'Figura_2_a':'Figura_2_a','Figura_2_b':"Figura_2_b/",'Figura_3':"Figura_3/",'Figura_4':"Figura_4/"}
    for sheet in sheet_name:
        sheet_df=xls[sheet]
        for index, row in sheet_df.iterrows():
            print(row['Dataset'], row['K_Fold'])
            if ml:
                cmd = COMMAND2
            else: 
                COMMAND

            combination="{}dropout_d_{}_dropout_g{}epochs_{}_Layers_density".format(row['dropout_decay_rate_d'],row['dropout_decay_rate_g'],row['Epochs'],row["Layer_size"])
            cmd+="--output_dir {}{}/{}/  ".format(dic_direct[sheet],row["Dataset"],combination)
            cmd+= "--dropout_decay_rate_d {} ".format(row['dropout_decay_rate_d'])
            cmd+= "--dropout_decay_rate_g {} ".format(row['dropout_decay_rate_g'])
            cmd+= "--dense_layer_sizes_g {} ".format(row['Layer_size'])
            cmd+= "--dense_layer_sizes_d {} ".format(row['Layer_size'])
            cmd+= "--number_epochs {} ".format(row['Epochs'])
            cmd+= "-i datasets/reduced_{}.csv ".format(row['Dataset'])
            p1 = subprocess.Popen(cmd,shell=True) 
            p1.wait()

    
def main():
    """
    Função principal que configura e executa as campanhas.
    """

    parser = argparse.ArgumentParser(description='Torrent Trace Correct - Machine Learning')
    #definição dos arugmentos de entrada

    parser.add_argument("--campaign", "-c",     help='Classificador (ou lista de classificadores separada por ,) padrão:{}.'.format(DEFAULT_CAMPAIGN), default=DEFAULT_CAMPAIGN, type=list_of_strs)
    parser.add_argument('-ml','--use_mlflow',action='store_true',help="Uso ou não da ferramenta mlflow para monitoramento") 
    Parâmetros = parser.parse_args()
    read_function(Parâmetros.campaign,Parâmetros.use_mlflow)


if __name__ == '__main__':
    sys.exit(main())

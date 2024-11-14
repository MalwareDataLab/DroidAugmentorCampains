## 1. Preparação e instalação

1. Clonar o repositório e execute os seguintes comandos.
   ```bash
    git clone https://github.com/SBSegSF24/MalSynGen.git
    cd MalSynGen
   ```
2. Instalação das dependências.
   
   **Opção 1**: Construir uma imagem Docker localmente a partir do Dockerfile.
      
      ```bash
      ./scripts/docker_build.sh
      ```
   **Opção 2**: Utilizar o script **pip_env_install.sh**.
      
      ```bash
   ./pip_env_install.sh
      ```

   **Opção 3**: Configurar o venv.
   ```
   python3 -m venv .venv
   ```
   ```
   source .venv/bin/activate
   ```
   ```
   pip3 install -r requirements.txt
   ```

   **Opção 4**: Configurar o pipenv.
   ```
   pip install pipenv
   ```
   ```
   pipenv install -r requirements.txt
   ```
   Obs: É necessário a instalação do pipenv através da opção 4 ou opção 2 para garantir o funcionamento da ferramenta.
## 2. Execução
Executar a demonstração de funcionamento da ferramenta: 

   **Opção 1**: instalar as dependências e executar uma demonstração em um ambiente Linux. 
   ```bash
   ./run_demo_venv.sh
   ```

   **Opção 2**: Executar o docker demo que instancia uma versão reduzida do experimento.  
   ```bash
   ./run_demo_docker.sh
   ```

## 3. Reprodução 
Para a reprodução dos mesmos experimentos (campanhas) do paper execute o seguinte comando:
   **Opção 1**: No ambiente local.
   ```bash
     python3 run_experimentos.py -
   ```

 




#### 4 Parâmetros dos testes automatizados:

      --------------------------------------------------------------

    --campaign ou -c:    Especifica a campanha de avaliação que você deseja executar. 
                         Você pode fornecer o nome de uma campanha específica ou uma  
                         lista de campanhas separadas por vírgula. 
                         Por exemplo: --campaign SF24_4096_2048_10 ou --campaign 
                          Kronodroid_e,kronodroid_r.

    --demo ou -d:
                         Ativa o modo demo. Quando presente, o script será executado 
                         no modo demo, o que pode ter comportamento reduzido 
                         ou exibir informações de teste.
                         --verbosity ou -v: Especifica o nível de verbosidade do log.
                         Pode ser INFO (1) ou DEBUG (2). 
                         Por padrão, o nível de verbosidade é definido como INFO.


     Outros parâmetros de entrada são definidos dentro das campanhas de avaliação em 
     campaigns_available. Cada campanha tem suas próprias configurações específicas, 
     como input_dataset, number_epochs, training_algorithm, dense_layer_sizes_g, 
     dense_layer_sizes_d, classifier, activation_function, dropout_decay_rate_g, 
     dropout_decay_rate_d, e data_type. As configurações podem variar dependendo do 
     objetivo e das configurações específicas de cada campanha.  


     Em campaigns_available o script irá iterar sobre as combinações de configurações 
     especificadas e executar os experimentos correspondentes.

    --------------------------------------------------------------





## 5. Parâmetros da Ferramenta
|       Flag/ parametro       |                                  Descrição                                 | Obrigatório |
|:---------------------------:|:--------------------------------------------------------------------------:|:-----------:|
|     -i , --input_dataset    |              Caminho para o arquivo do dataset real de entrada             |     Sim     |
|       -o, --output_dir      |               Diretório para gravação dos arquivos de saída.               |     Não     |
|         --data_type         |       Tipo de dado para representar as características das amostras.       |     Não     |
| --num_samples_class_malware |                  Número de amostras da Classe 1 (maligno).                 |     Sim     |
|  --num_samples_class_benign |                  Número de amostras da Classe 0 (benigno).                 |     Sim     |
|       --number_epochs       |            Número de épocas (iterações de treinamento) da cGAN.            |     Não     |
|           --k_fold          |                 Número de subdivisões da validação cruzada                 |     Não     |
|      --initializer_mean     |          Valor central da distribuição gaussiana do inicializador.         |     Não     |
|   --initializer_deviation   |          Desvio padrão da distribuição gaussiana do inicializador.         |     Não     |
|      --latent_dimension     |              Dimensão do espaço latente para treinamento cGAN.             |     Não     |
|     --training_algorithm    | Algoritmo de treinamento para cGAN. Opções: 'Adam', 'RMSprop', 'Adadelta'. |     Não     |
|    --activation_function    |      Função de ativação da cGAN. Opções: 'LeakyReLU', 'ReLU', 'PReLU'      |     Não     |
|    --dropout_decay_rate_g   |              Taxa de decaimento do dropout do gerador da cGAN.             |     Não     |
|    --dropout_decay_rate_d   |           Taxa de decaimento do dropout do discriminador da cGAN.          |     Não     |
|    --dense_layer_sizes_g    |                   Valores das camadas densas do gerador.                   |     Não     |
|    --dense_layer_sizes_d    |                Valores das camadas densas do discriminador.                |     Não     |
| --latent_mean_distribution" |             Média da distribuição do ruído aleatório de entrada            |      Não    |
| --latent_stander_deviation" |                 Desvio padrão do ruído aleatório de entrada                |      Não    |
|         --batch_size        |            Tamanho do lote da cGAN. Opções: 16, 32, 64, 128, 256           |     Não     |
|         --verbosity         |                            Nível de verbosidade.                           |     Não     |
|        --save_models        |                    Opção para salvar modelos treinados.                    |     Não     |
|   --path_confusion_matrix   |                Diretório de saída das matrizes de confusão.                |     Não     |
|      --path_curve_loss      |          Diretório de saída dos gráficos de curva de treinamento.          |     Não     |
|        -a, --use_aim        |         Opção para utilizar a ferramenta de rastreamento Aimstack.         |     Não     |
|      -ml, --use_mlflow      |          Opção para utilizar a ferramenta de rastreamento mlflow.          |     Não     |
|        -rid, --run_id       |  Opção ligado ao mlflow, utilizada para resumir uma execução não terminada |     Não     |
|    -tb, --use_tensorboard   |          Opção para utilizar a ferramenta de rastreamento Tensorb          |     Não     |

## 6. Datasets
O diretório **datasets** do GitHub contém os conjuntos de dados balanceados utilizados nos experimentos, estes foram obtidos do Repositório [Malware data hunter](https://github.com/Malware-Hunter/datasets/tree/main)



## 7. Ferramentas de rastreamento

### 8.1. Mlflow

1. Instalar a ferramenta:
   
```bash
pip install mlflow
```

2. Instanciar um servidor local na porta 6002:

```bash
mlflow server --port 6002
```


4. Após o fim da execução, acesse o endereço http://localhost:6002/ no seu navegador para visualizar os resultados.


Documentação Mlflow: https://mlflow.org/docs/latest/index.html




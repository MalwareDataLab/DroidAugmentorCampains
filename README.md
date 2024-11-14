## 1. Preparação e instalação

1. Clonar o repositório e execute os seguintes comandos.
   ```bash
    git clone https://github.com/MalwareDataLab/WRSeg24-DroidAugmentor.git
    cd WRSeg24-DroidAugmentor
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
   ./run_reproduce_WRSEG24_venv.sh
   ```
   **Opção 2**: No ambiente docker
   ```bash
   ./run_reproduce_WRSEG24_docker.sh
   ```





## 4. Parâmetros da Ferramenta
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

## 5. Datasets
O diretório **datasets** do GitHub contém os conjuntos de dados balanceados utilizados nos experimentos, estes foram obtidos do Repositório [Malware data hunter](https://github.com/Malware-Hunter/datasets/tree/main)



## 6. Ferramentas de rastreamento

### 6.1. Mlflow

1. Instalar a ferramenta:
   
```bash
pip install mlflow
```

2. Instanciar um servidor local na porta 6002:

```bash
mlflow server --port 6002
```
3. Execute os experimentos com a flag -ml:

```bash
python3 run_experimentos.py -ml
```


4. Após o fim da execução, acesse o endereço http://localhost:6002/ no seu navegador para visualizar os resultados.


Documentação Mlflow: https://mlflow.org/docs/latest/index.html




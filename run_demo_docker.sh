#!/bin/bash
#USER_ID=$(id -u $USER)
if docker info >/dev/null 2>&1; then
	DIR=$(readlink -f shared)
	if [ -z "$(docker images -q  wrseg/droidaugmento:latest 2> /dev/null)" ]; then
	docker build -t wrseg/droidaugmentor:latest . 
	fi
	docker run -it --name=/DroidAugmentor-$RANDOM -v $DIR:/DroidAugmentor/shared -e DISPLAY=unix$DISPLAY  wrseg/droidaugmento:latest /DroidAugmentor/shared/app_run.sh --verbosity 20 --output_dir /DroidAugmentor/shared/outputs --input_dataset /DroidAugmentor/datasets/reduced_balanced_kronodroid_emulator.csv   --batch_size 256   --number_epochs 100 --k_fold 2 --training_algorithm Adam
	#ls shared/outputs/
else
    echo "Seu usuário atual não possui permissões para executar docker sem sudo, execute o seguinte comando e reinicialize a máquina: sudo usermod -aG docker SEU_USER "
fi

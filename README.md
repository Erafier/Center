# Center

## Установка

Работоспособность гарантируется только на Linux. Протестировано на  Ubuntu 19.04
Установить пакеты g++, gcc, git :`sudo apt install git gcc g++`  


В первую очередь установить пакетный менеджер miniconda:  
Команды запускать из домашней директории
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda-latest-Linux-x86_64.sh
```
На все вопросы установочника отвечать `yes`
После установки необходимо перезапустить терминал. В случае успешной установки перед именем пользователя появится надпись `(base)`

1. torchreid
```
$ git clone https://github.com/erafier/deep-person-reid.git
$ cd deep-person-reid/
$ conda create --name center python=3.7
$ conda activate center
$ pip install -r requirements.txt
```
Установка на машину с гпу: `$ conda install pytorch torchvision cudatoolkit=9.0 -c pytorch`  
Установка без гпу: `$ conda install pytorch torchvision cpuonly -c pytorch`

`
$ pip install pillow==6.2.2
$ python setup.py develop`

Все дальнейшие действия и запуск программы должны осуществляться из окружения center. Перед именем пользователя в терминале должно быть написано (center)
2. Установить пакеты в окружении center:
- flask: `pip install flask`
- pycocotools: `pip install cython; pip install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI`
3. detectron2 по инструкции из репозитория, из домашней директории
  ```  
  git clone https://github.com/facebookresearch/detectron2.git
  cd detectron2
  pip install -e .
  ```
4. Скачать данный репозиторий командой `git clone https://github.com/Erafier/Center.git`
5. Ссылка на изображения: https://drive.google.com/file/d/1v4-FuYKdz3uzW4cn7hYdK97kFINaNX_a/view?usp=sharing
Выполнить в командной строке   
`$ gdown --id 1v4-FuYKdz3uzW4cn7hYdK97kFINaNX_a; unzip static.zip -d Center`
6. Ссылка на конфиг и веса детектора: https://drive.google.com/file/d/14F6YAfNqvxnMlwm-C_mZwIsWRm8K7PvI/view?usp=sharing
`$ gdown --id 14F6YAfNqvxnMlwm-C_mZwIsWRm8K7PvI; unzip configs.zip -d Center/detector/`
7. Запускать командой `python app.py` из директории с проектом. 
8. Перейти в строке браузера по адресу http://127.0.0.1:5000

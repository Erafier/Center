# Center

## Установка
На машине должен быть установлен gcc: `sudo apt install gcc g++`

В первую очередь установить пакетный менеджер miniconda:
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda-latest-Linux-x86_64.sh
```
или
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
$ bash ~/miniconda.sh -b -p ~/miniconda 
$ rm ~/miniconda.sh
$ export PATH=~/miniconda/bin:$PATH
```
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
    ```
    $ python setup.py develop
  
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
5. Ссылка на изображения: https://drive.google.com/file/d/1j26AIpZ5CurMV7WBdQFQUKn__SGc-JNH/view?usp=sharing
  Загрузить командой `gdown --id 1j26AIpZ5CurMV7WBdQFQUKn__SGc-JNH` и распаковать `unzip static.zip -d Center`
6. Ссылка на конфиг и веса детектора: https://drive.google.com/file/d/1X35TJDyQEbk55THSsn63l04I4nfJYXwH/view?usp=sharing
  Загрузить командой `gdown --id 1X35TJDyQEbk55THSsn63l04I4nfJYXwH` и распаковать `unzip configs.zip -d Center/detector/`
7. Запускать командой `python app.py` из директории с проектом
8. Перейти в строке браузера по адресу 127.0.0.1:5000

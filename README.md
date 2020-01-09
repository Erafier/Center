# Center

Установка
  1. Должны быть установлены пакеты:
    - 
  2. torchreid по инструкции из репозитория
    - Установка на машину с гпу: conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
    - Установка без гпу: conda install pytorch torchvision cpuonly -c pytorch
  3. detectron2 по инструкции из репозитория
  4. Скачать данный репозиторий командой `git clone https://github.com/Erafier/Center.git`
  4. Ссылка на изображения: https://drive.google.com/file/d/1v4-FuYKdz3uzW4cn7hYdK97kFINaNX_a/view?usp=sharing
    Загрузить командой `gdown --id 1v4-FuYKdz3uzW4cn7hYdK97kFINaNX_a` и распаковать `unzip static.zip -d Center`
  5. Ссылка на конфиг и веса детектора: https://drive.google.com/file/d/1X35TJDyQEbk55THSsn63l04I4nfJYXwH/view?usp=sharing
    Загрузить командой `gdown --id 1X35TJDyQEbk55THSsn63l04I4nfJYXwH` и распаковать `uunzip configs.zip -d Center/detector/`
  6. Запускать командой `python app.py` из директории с проектом

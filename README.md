# Печать файлов из папки (RUS)

Программа написана для работы в OC Windows.</br>
Программа следит за дерикторией в системе. В случае появления нового
файла производится попытка печати на принтере, установленном в 
системе по-умолчанию, затем файл переносится во вложенную папку 
"backup".</br>

<H3>Установка и пример использования</H3>
1. Установить на компьютер интерпретатор Python (>= 3.10), при установке
обязательно установить галку PATH.
2. Скопировать файлы программы на свой ПК
3. Установить необходимые модули (<code>pip install -r /path/to/requirements.txt</code>)
4. В файле main.py указать путь до папки слежения(<code>PATH: str = "Z:\\test"</code>)
5. Запустить программу <code>python main.py</code>


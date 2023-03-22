# Печать файлов из папки (RUS)

Программа написана для работы в OC Windows.</br>
Программа следит за директорией в системе. В случае появления нового
файла производится попытка печати на принтере, установленном в 
системе по-умолчанию, затем файл переносится во вложенную папку 
"backup".</br>
Программа использует WinAPI для печати, следовательно на ПК должна быть установлена программа</br>
для чтения файлов, тип которых будем печатать. Для pdf требуется использовать FoxitReader.</br>

<H3>Установка и пример использования</H3>
1. Установить на компьютер интерпретатор Python (>= 3.10), при установке
обязательно установить галку PATH.</br>
2. Скопировать файлы программы на свой ПК</br>
3. Установить необходимые модули (<code>pip install -r /path/to/requirements.txt</code>)</br>
4. В файле config.json указать путь до папки слежения(Например: <code>"target_folder": "M:\\test"</code>)</br>
5. Запустить программу <code>python main.py</code></br>



# Printing files from a folder (ENG)

The program is written to work in Windows.</br>
The program monitors the directory in the system. If a new
file appears, an attempt is made to print on the printer installed in
the system by default, then the file is transferred to the
"backup" subfolder.</br>
The program uses WinAPI for printing, therefore the program must be installed on the PC</br>
for reading files, the type of which will be printed. For pdf, FoxitReader is required.</br>

<H3>Installation and usage example</H3>
1. Install the Python interpreter on the computer (>= 3.10), when installing
, be sure to set the PATH checkbox.</br>
2. Copy the program files to your PC</br>
3. Install the necessary modules (<code>pip install -r /path/to/requirements.txt </code>)</br>
4. In the file config.json specify the path to the tracking folder(For example: <code>"target_folder": "M:\\test"</code></code>)</br>
5. Run the <code>python program main.py </code></br>
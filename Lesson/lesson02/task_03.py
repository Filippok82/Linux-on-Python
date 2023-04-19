"""💡 --collect-only
Параметр --collect-only показывает, какие тесты будут выполняться с заданными
параметрами и конфигурацией, но не запускает их.
💡 -k EXPRESSION
Параметр -k позволяет использовать выражение для определения функций
тестирования.

test_asdict() и test_defaults(). Вы можете проверить фильтр с помощью: --collect-only:

💡-m MARKEXPR
Маркеры-один из лучших способов пометить подмножество тестовых функций для
совместного запуска. Отметим тесты, используя
декоратор @pytest.mark.run_these_please:
Теперь то же самое для test_replace().
💡 -x, --exitfirst
Опция -x прерывает тесты при ошибке (как стандартный assert python).
💡--maxfail=num
Параметр -x приводит к остановке после первого отказа теста. Если вы хотите,
чтобы некоторое количество сбоев было допущено, но не очень много, используйте
параметр --maxfail, чтобы указать, сколько ошибок допускается получить.
💡 -s и --capture=method
Флаг -s позволяет печатать операторы — или любой другой вывод, который обычно
печатается в stdout, чтобы фактически быть напечатанным в стандартном выводе во
время выполнения тестов. Это сокращённый вариант для --capture=no.
Другой вариант, который может помочь вам обойтись без операторов печати в
вашем коде,-l/--showlocals, который распечатывает локальные переменные в тесте,
если тест терпит неудачу.
💡-lf, --last-failed
При сбое одного или нескольких тестов способ выполнения только неудачных
тестов, полезен для отладки. –ff, --failed-first
Параметр --ff/--failed-first будет делать то же самое, что и --last-failed, а затем
выполнять остальные тесты, прошедшие в прошлый раз:
💡-v, --verbose
Опция -v/--verbose предоставляет более развёрнутую информацию по итогам.
Наиболее очевидным отличием является то, что каждый тест получает собственную
строку, а имя теста и результат прописываются вместо точки.
💡 -q, --quiet
Опция -q/--quiet противоположна -v/--verbos. Она сокращает объём информации в
отчёте.
💡-l, --showlocals
При использовании параметра -l/--showlocals локальные переменные и их значения
отображаются вместе с tracebacks для неудачных тестов.
💡--tb=style
Параметр --tb=style изменяет способ вывода пакетов трассировки для сбоев. При
сбое теста pytest отображает список сбоев и так называемую обратную
трассировку, которая показывает точную строку, в которой произошёл сбой. Хотя
tracebacks полезны большую часть времени, бывают случаи, когда они раздражают.
Вот где опция--tb=style пригодится. Полезны стили short, line и no.
● --tb=no полностью удаляет трассировку.
● --tb=line во многих случаях достаточно, чтобы показать, что не так. Если у вас
много неудачных тестов, этот параметр может помочь отобразить шаблон в
сбоях. Он сохраняет ошибку в одной строке.
● --tb=short показывает сокращённый вариант трассировки, то есть печатает
только строку assert и символ E без контекста.
Есть три оставшихся варианта трассировки, которые мы пока не рассмотрели.
● --tb=long покажет вам наиболее исчерпывающий и информативный traceback.
--tb=auto покажет вам длинную версию для первого и последнего tracebacks,
если у вас есть несколько сбоев.
● --tb=native покажет вам стандартную библиотеку traceback без
дополнительной информации.
💡 --durations=N
Опция --durations=N полезна, когда вы пытаетесь ускорить свой набор тестов. Она
не меняет ваши тесты, но сообщает самый медленный N номер
tests/setups/teardowns по окончании тестов. Если вы передадите --durations=0, он
сообщит обо всём в порядке от самого медленного к самому быстрому."""
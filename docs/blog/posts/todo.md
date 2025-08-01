---
# draft: true 
date: 2025-07-27
categories:
  - todo
tags:
  - todo
---

# TODO

<!-- more -->

## Clojure

Побачила згадку Clojure і тепер думаю, що треба трохи розібратися з курсами і
знов повчити його.  Остання спроба була в кінці 2017 - на початку 2018 і,
здається, тоді мені ще зарано було.

## pyneng

PDF:

* [quarto](https://quarto.org/docs/output-formats/pdf-basics.html)

### pyneng

* зробити завдання базового курсу, записати відео (згадати завдання, виправити помилки)
* те саме можна і з advpyneng

### переклад

* завдання з advpyneng, заразом вичитати


## To read/watch/listen

Tests

* [Autocon 2. Step 0: Test the Network! - Danny Wade](https://www.youtube.com/watch?v=3eKNLRVMtIg)

NUTS (Network Unit Testing System):

* https://github.com/network-unit-testing-system/nuts
* https://netcraftsmen.com/going-nuts-for-network-testing/
* https://networkautomagic.net/podcast/na003/ - багато корисних посилань
* [SwiNOG#39 | INPG Stack: An automated way of maintaining and testing a network | Marco Martinez| OST](https://youtu.be/ZVl0GnYMUEo?si=pShkgf-0vFXLUgQj)

Random links

* https://pythonpeople.fm/episodes/pamela-fox
* [An introduction to Python for linguists](https://v4py.github.io/intro.html)
* [Network Automagic 004 - Autocon 3 hallway track](https://www.youtube.com/watch?v=gVKPpbiAh50)

To read

* Creating TUI Applications with Textual and Python
* Network Programmability and Automation: Skills for the Next-Generation Network Engineer 2nd Edition
* Cisco pyATS ― Network Test and Automation Solution: Data-driven and reusable testing for modern networks (Networking Technology)

Maybe & rereads

* The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win
* The DevOps Handbook, 2nd Edition

## Update/add

* [uv](https://docs.astral.sh/uv/) - на заміну venv, install Python
* [ruff](https://github.com/astral-sh/ruff) - можливо зарано?

## What's next

Думаю між Ansible, Nornir і завершити базовий курс.

Базовий не дуже цікаво, але треба.
Може почати з відповідей на завдання і втягнуся.

З іншого боку, якщо говорити абстрактно, то Ansible краще для початку в
автоматизації, ніж Python. Тому наче як логічно додати його.

Можливо, варто комбінувати, щоб знову не зависнути з базовим.


> Ansible core 2.19, community 12 problems! (july 2025)

## youtube task solutions

* task answer 1, 2, 3 (only course topics)
* task answer with arbitrary topics used
* after functions: add type annotation version
* docstring


## pytest series

* write test for basic pyneng functions (chapters 9 - ...)


## ideas

Думаю повернутися до ідеї [pyneng-examples](https://github.com/natenka/pyneng-examples).

Як ідея додати залежності і наступне, щоб можна було автоматично зробити з
цього граф і за певною темою отримувати можливі шляхи і розгалудження теми.

Також це можна використовувати як добірку прикладів для практики читання коду.

example:

* netmiko
* netmiko + cli (argparse, click, typer)
* netmiko + textual (load devices, type command)
* netmiko tools

Можна використати LLM для основи docstring та опису, бо постійно руки не
доходили їх написати.

## for fun:

* textual
* переробити утиліту pyneng-quiz на нову версію textual 1.0.0


### textual + pyneng-cli

Можна прикрутити textual до pyneng-cli і спробувати запускати там тести.
А в різних віджетах показувати локальні змінні, код +- 5 рядків, якщо тест
не пройшов і подібне.

Також можна вибирати там які тести запускати (для яких завдань). Ставити опції
типу verbose.

Краще робити два варіанти запуску - чисто cli і tui.
У мене перевірки налаштовані на cli.

```
$ pyneng --help                                                                                                                                     
Usage: pyneng [OPTIONS] [TASKS]                                                                                                                     
                                                                                                                                                    
  PYNENG-CLI: Run tests for TASKS tasks. By default, all tests will run.                                                                            
                                                                                                                                                    
  These options do not run tests                                                                                                                    
   pyneng --docs                 Show pyneng documentation                                                                                          
   pyneng --save-all             Save to GitHub all modified files in the current directory
   pyneng --update               Update all tasks and tests in the current directory
   pyneng --update --test-only   Update only tests in the current directory
   pyneng 1,2 --update           Update tasks 1 and 2 and corresponding tests in current directory
   pyneng --update-chapters 4-5  Update chapters 4 and 5 (directories will be removed and updated versions copied)
```

## Подивитися мої лекції

* vim
* tmux
* asyncio
* rich


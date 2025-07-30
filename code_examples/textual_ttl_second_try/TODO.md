## TODO

Є основа для віджета вибору теми і основа для віджета питання. Плюс:

* Після вибору теми, вже є варіант спрацювання вибору питань.
* Після вибору відповідей, вони фіксуються.

Проблема: enter забирає на себе віждет checkbox, а я хочу щоб enter був для
перевірки відповіді.  При цьому, enter я можу переписати глобально, але
хочеться залишити enter також для вибору теми.
Можливо зі скрінами (screen) щось вийде зробити.

Думаю чи залишати панель вибору теми, після вибору теми.
Варіанти:

1. ховати/показувати по комбінації
2. ховати, після вибору теми переходити на 1 питання на екран
3. при виборі теми, показувати всі питання коротко в Vertical scroll, а після
   переходу на питання (комбо Почати quiz? Можливо хай буде по Enter), ховати
   вибір тем і перейти на питання на екран

~~3 варіант зробила тестово в файлі pquiz_widget_topic_selection_optionlist_show_all_q_rich.py
Там з rich показується все більш-менш ок. Тільки треба розібратися як зробити
widget типу Static, тільки з фокусом, щоб працювала клавіатура. Зараз не працює.~~

Це вже зробила. Фокус працює. Код в pquiz_widget_topic_selection_optionlist_show_all_q_rich_can_focus.py


## Треба розібратися

### чи можна робити update чи аналог не static widget, а чомусь іншому?

Хочеться щоб текст з тим, що це тільки preview питань, був закріпленим при прокрутці.

### Як краще зробити перехід з topic selection в questions? Різні screen?

В старій версії це зроблено так

```python
    def clear_current_view(self):
        self.view.layout.docks = []

    async def action_change(self, change: str) -> None:
        if change == "change topic":
            self.current_topic = None
            self.clear_current_view()
            await self.view.dock(self.topics_table)

    async def load_q_table(self):
        self.clear_current_view()
        # load questions
        self.help = HelpTable()
        await self.view.dock(self.help, edge="bottom")
        self.q_table = QuestionTable(topic_questions=self.current_topic_questions)
        await self.view.dock(self.q_table)

```

Зі старої версії треба передивитися як зараз краще робити on_load/on_mount/on_key


## Textual tutorial

```python
class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
```

compose() is where we construct a user interface with widgets, by yielding them.

Binding: key, action, description.

action_toggle_dark() defines an action method. Actions are methods beginning
with action_ followed by the name of the action. The BINDINGS list above tells
Textual to run this action when the user hits the D key. See actions in the
guide for details.

Action method

Action methods are methods on your app or widgets prefixed with action_. Aside
from the prefix these are regular methods which you could call directly if you
wished.



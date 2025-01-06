---
# draft: true 
date: 2025-01-05
categories:
  - tools
tags:
  - textual
  - cli
---

# Нотатка по Textual

## Quiz ideas

Цікаво спробувати зробити адмінку для створення/додавання запитань:

* щоб можна було заповнювати поля: код, опис, варіанти відповідей, правильна відповідь (одна чи декілька) тощо
* з цього робити JSON
* доречі можна зробити для початку адмінку для пересортування питань:
  * завантажити JSON
  * показати питання блоками
  * дати можливість видалити, змінити порядок, а потім і додати нові

Тестові приклади, поки читаю доки:

* зробити вибірку по номеру теми, під час введення номеру у widget Input (тут ще питання тільки по номеру теми чи ще й по номеру розділа)
* зробити вибірку по назві теми, під час введення номеру у widget Input
* можна все об'єднати в остаточній версії

## TODO

Phase 1

* read textual docs (write notes)
* asyncio review (my lectures)
* rewrite pyneng tool

<!-- more -->

Phase 2

* click review, what's new (my lecture)
* play with [trogon](https://github.com/Textualize/trogon)
* textual-web - publishing textual apps on the web

## Links

* [docs](https://textual.textualize.io/)
* [basic tutorial video](https://youtube.com/playlist?list=PLHhDR_Q5Me1MxO4LmfzMNNQyKfwa275Qe&si=wFN6SHOgwn_HJ0dm)


## Basics

```
pip install textual
```


### Command palette

``ctrl-p``

* [command palette docs](https://textual.textualize.io/guide/command_palette/)


### App

```python
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class StopwatchApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets"""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
```


* App class - responsible for loading configuration, setting up widgets, handling keys, ...
* BINDINGS: key, name of the action, description
* Header bar with a title
* Footer bar at the bottom with bound keys
* compose - construct a user interface with widgets
  * method may return a list of widgets, but it is generally easier to yield them
* action_toggle_dark - defines an action method. The BINDINGS list above tells Textual to run this action when the user hits the D key.

### Widgets

```python
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header


class TimeDisplay(Digits):
    """A widget to display elapsed time"""


class Stopwatch(HorizontalGroup):
    """A stopwatch widget"""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch"""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


# only new line
class StopwatchApp(App):
    def compose(self) -> ComposeResult:
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())
```

Containers - containers are widgets which contain other widgets

* Horizontal and VerticalScroll


Button:

* label (start, stop, reset)
* id
* variant - default style


VerticalScroll:

* will scroll if the contents don't quite fit
* takes care of key bindings required for scrolling, like Up, Down, ++pgdn++, ++pgup++, Home, End, etc.


When widgets contain other widgets (like VerticalScroll) they will typically
accept their child widgets as positional arguments. So the line 
``yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())`` creates a VerticalScroll
containing three Stopwatch widgets.


### Textual CSS


#### Manual style

Every widget has a styles object with a number of attributes that impact how
the widget will appear.

```python
self.styles.background = "blue"
self.styles.color = "white"
```

#### Textual CSS

```css
Stopwatch {   
    background: $boost;
    height: 5;
    margin: 1;
    min-width: 50;
    padding: 1;
}

TimeDisplay {   
    text-align: center;
    color: $foreground-muted;
    height: 3;
}

Button {
    width: 16;
}

#start {
    dock: left;
}

#stop {
    dock: left;
    display: none;
}

#reset {
    dock: right;
}
```

``background: $boost`` sets the background color to ``$boost``. The $ prefix picks a
pre-defined color from the builtin theme. There are other ways to specify
colors such as "blue" or rgb(20,46,210).



When the declaration begins with a ``#`` then the styles will be applied to widgets
with a matching "id" attribute. We've set an ID on the Button widgets we
yielded in compose. For instance the first button has id="start" which matches
``#start`` in the CSS.

```css
#start {
    dock: left;
}
```

Hide

```css
#stop {
    dock: left;
    display: none;
}

```

#### Dynamic CSS

CSS class

```
.started {
    background: $success-muted;
    color: $text;
}

.started TimeDisplay {
    color: $foreground;
}

.started #start {
    display: none
}

.started #stop {
    display: block
}

.started #reset {
    visibility: hidden
}
```


Combining the two selectors with a space ``.started #start`` creates a new
selector that will match the start button only if it is also inside a container
with a CSS class of "started".

### event hadler, class manipulation

New method

```python
class Stopwatch(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")
```

The on_button_pressed method is an event handler. Event handlers are methods
called by Textual in response to an event such as a key press, mouse click,
etc. Event handlers begin with on_ followed by the name of the event they will
handle. Hence on_button_pressed will handle the button pressed event.


When the button event handler adds or removes the "started" CSS class, Textual
re-applies the CSS and updates the visuals.

### Reactive attributes

To add a reactive attribute, import reactive and create an instance in your
class scope.

```python
from textual.reactive import reactive


class TimeDisplay(Digits):
    """A widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.set_interval(1 / 60, self.update_time)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = monotonic() - self.start_time

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")
```

Two reactive attributes to the TimeDisplay widget:
* start_time will contain the time the stopwatch was started (in seconds)
* time will contain the time to be displayed in the Stopwatch widget

Both attributes will be available on self as if you had assigned them in
``__init__``. If you write to either of these attributes the widget will update
automatically.


The first argument to reactive may be a default value for the attribute or a
callable that returns a default value.


set_interval() - creates a timer which calls self.update_time sixty times a
second.

#### watch method

If you implement a method that begins with watch_ followed by the name of a
reactive attribute, then the method will be called when the attribute is
modified. Such methods are known as watch methods.


## Guide

Експерименти в процесі читання доків, а саме Guide.

Базовий вибір кнопки/теми. Подобається, бо частина функціоналу автоматична саме через віджет кнопку.

### select, unselect, on_key, on_button_pressed

Це просто потренуватися після туторіал частини.

```python
import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static
from textual import events


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return list(q_dict.keys())


topics = load_topics("questions.json")


class TopicText(Button):
    #def on_button_pressed(self, event: Button.Pressed) -> None:
    #    self.select()

    def select(self) -> None:
        self.add_class("selected")

    def unselect(self) -> None:
        self.remove_class("selected")


class Topics(VerticalScroll):
    pass


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"

    #def compose(self) -> ComposeResult:
    #    yield Header()
    #    yield Footer()
    #    topics_list = [
    #        TopicText(f"{topic_id:<4} {text}", id=f"topic_{topic_id}")
    #        for topic_id, text in enumerate(topics, 1)
    #    ]
    #    yield Topics(*topics_list, id="topics")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [
            TopicText(f"{topic_id:<4} {text}", id=f"topic_{topic_id}")
            for topic_id, text in enumerate(topics, 1)
        ]
        yield from topics_list

    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            for button in self.query("TopicText"):
                button.unselect()
            selected_topic_text = self.query_one(f"#topic_{event.key}")
            # add expected type:
            # selected_topic_text = self.query_one(f"#topic_{event.key}", TopicText)
            selected_topic_text.select()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        for button in self.query("TopicText"):
            button.unselect()
        event.button.select()
        # selected_topic_text = self.query_one(f"#{event.button.id}")
        # selected_topic_text.select()


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
```

### Input widget

Це щоб не забути про віджет Input, бо він точно буде потрібен для фінальної версії.
Хочеться через нього зробити вибір тем, як зроблена command palette.

```python
import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Input, Static
from textual import events


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return list(q_dict.keys())


topics = load_topics("questions.json")


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Введіть номер теми та натисніть Enter", id="intro")
        yield Input()
        topics_list = [
            f"{topic_id:<4} {text}"
            for topic_id, text in enumerate(topics, 1)
        ]
        yield Static("\n".join(topics_list), id="questions")


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
```

### Сигнал з віджета про вибрану тему, летить до app

Розділ [Events and messages](https://textual.textualize.io/guide/events/),
приклад з документації, трохи перероблений під quiz.

```python
import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static
from textual import events


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicText(Static):
    class Selected(Message):
        def __init__(self, topic: str) -> None:
            self.topic = topic
            super().__init__()

    def __init__(self, topic: str) -> None:
        self.topic = topic
        super().__init__()

    def on_click(self) -> None:
        self.post_message(self.Selected(self.topic))

    def render(self) -> str:
        return str(self.topic)


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"
    TOPICS = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [TopicText(topic) for topic in self.TOPICS]
        yield from topics_list

    def on_topic_text_selected(self, message: TopicText.Selected) -> None:
        selected_topic = message.topic
        topics = self.query("TopicText")
        for top in topics:
            if top.topic != selected_topic:
                top.remove()
        for top in topics:
            top.styles.animate("background", "green", duration=0.1)


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
```



Те саме, тільки видаляю теми через VirticalScroll
```python
class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"
    TOPICS = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [TopicText(topic) for topic in self.TOPICS]
        yield VerticalScroll(*topics_list, id="topics")

    def on_topic_text_selected(self, message: TopicText.Selected) -> None:
        selected_topic = message.topic
        topics = self.query_one("#topics").remove()

        new_topic = TopicText(selected_topic)
        header = self.query_one("#intro")
        header.mount(new_topic)
        new_topic.styles.animate("background", "green", duration=0.1)
```

### Наступним треба спробувати

* комбінацію buttons + message
* почитати про dom, бо щось я його пропустила: https://textual.textualize.io/guide/CSS/

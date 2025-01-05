---
# draft: true 
date: 2025-01-05
categories:
  - tools
tags:
  - textual
  - cli
---

# Textual

!!! note "Допис буде поступово доповнюватися"

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
#start in the CSS.

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

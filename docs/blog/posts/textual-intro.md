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

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

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [
            TopicText(f"{topic_id:<4} {text}")
            for topic_id, text in enumerate(topics, 1)
        ]
        # yield from topics_list
        yield Topics(*topics_list, id="topics")

    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            for button in self.query("TopicText"):
                button.unselect()
            selected_topic_text = self.query_one(f"#topic_{event.key}")
            # add expected type:
            # self.query_one(f"#topic_{event.key}", TopicText)
            selected_topic_text.select()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        for button in self.query("TopicText"):
            button.unselect()
        event.button.select()


if __name__ == "__main__":
    app = TermQuiz()
    app.run()

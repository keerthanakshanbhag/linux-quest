from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Input, RichLog, Static


class LinuxQuest(App):
    """A keyboard-first Linux learning adventure."""

    TITLE = "Linux Quest"

    CSS = """
    Screen {
        layout: vertical;
    }

    #layout {
        height: 1fr;
    }

    #map {
        width: 30%;
        border: round $accent;
        padding: 1;
    }

    #right {
        width: 70%;
    }

    #mission {
        height: 1fr;
        border: round $success;
        padding: 1;
    }

    #output {
        height: 2fr;
        border: round $accent;
    }

    #command {
        dock: bottom;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="layout"):
            yield Static(
                "WORLD MAP\n\n"
                "[HOME]\n"
                "   |\n"
                "[VILLAGE]\n"
                "   |\n"
                "[FOREST]\n"
                "   |\n"
                "[CAVE] 🔒",
                id="map",
            )

            with Vertical(id="right"):
                yield Static(
                    "MISSION 01: THE LOST EXPLORER\n\n"
                    "Your adventure begins here!\n\n"
                    "Goal: Learn to navigate Linux.\n\n"
                    "Try typing: help\n"
                    "Then try: status",
                    id="mission",
                )

                yield RichLog(id="output", markup=False)

                yield Input(
                    placeholder="Enter a quest command...",
                    id="command",
                )

        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#output", RichLog).write(
            "Welcome to Linux Quest!"
        )
        self.query_one("#output", RichLog).write(
            "Type 'help' to see available commands."
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value.strip().lower()
        output = self.query_one("#output", RichLog)

        if not command:
            return

        output.write(f"quest$ {command}")

        if command == "help":
            output.write("Available commands:")
            output.write("  help   - Show available commands")
            output.write("  status - View your progress")
            output.write("  clear  - Clear the output panel")
            output.write("  exit   - Quit Linux Quest")

        elif command == "status":
            output.write("Level: 1")
            output.write("XP: 0")
            output.write("Missions completed: 0")

        elif command == "clear":
            output.clear()

        elif command == "exit":
            self.exit()

        else:
            output.write(
                "Unknown quest command. Type 'help' for assistance."
            )

        event.input.value = ""


if __name__ == "__main__":
    LinuxQuest().run()
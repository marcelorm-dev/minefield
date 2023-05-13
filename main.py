from src.interface.terminal_controller import TerminalController

terminal = TerminalController()
terminal.configure_game()

while not terminal.is_game_over():
    terminal.run_game()
else:
    terminal.end_game()

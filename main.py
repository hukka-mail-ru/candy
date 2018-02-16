import engine
import ui



#ui = ui.GraphicsUI()

consoleUI = ui.ConsoleUI()

game = engine.Game(consoleUI)

game.start()  


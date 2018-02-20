import engine
import ui




consoleUI = ui.ConsoleUI()
graphicsUI = ui.GraphicsUI()

game = engine.Game(graphicsUI)

game.start()  


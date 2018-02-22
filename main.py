import engine
import ui




consoleUI = ui.ConsoleUI()
graphicsUI = ui.GraphicsUI()

engine.GlobalGame.setUI(graphicsUI)
engine.GlobalGame.start()  


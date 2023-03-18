from loguru import logger

logger.add("./logs/{time:YYYY-MM-DD_HH-mm-ss}.log", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:5} | {name}:{function}:{line} - {message}",
           level="DEBUG", rotation="2 MB", compression="zip")

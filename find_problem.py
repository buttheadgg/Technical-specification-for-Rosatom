

def create_handlers(callback):
    handlers = []
    for step in range(5):
        #Добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(callback(step))
    return handlers

def execute_handlers(handlers):
    #Запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()

#lambda получит не несколько значений(как планировалось), а только один последний step.
#Колбэки вызовутся с последним значением переменной step, это значение 4.

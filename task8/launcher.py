import subprocess

process = []

while True:
    action = input('Действие: q - выход, s - запустить сервер и клиенты, x - закрыть все: ')

    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(2):
            process.append(subprocess.Popen('python client.py',  # -m send',0
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(2):
            process.append(subprocess.Popen('python monitor.py',  # -m listen',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        for i in process.copy():
            proc_to_kill = process.pop()
            proc_to_kill.kill()

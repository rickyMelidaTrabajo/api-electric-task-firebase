def task(app, url):

    @app.route(url+'get-tasks', methods=['GET'])
    def getTasks():
        return 'This is getTasks route'

    @app.route(url+'get-pending-task', methods=['GET'])
    def getPendingTask():
        return 'This is getPendingTask route'

    @app.route(url+'get-finished-task', methods=['GET'])
    def getFinishedTask():
        return 'This is getFinishedTask route'

    @app.route(url+'set-pending-task', methods=['GET', 'POST'])
    def setPendingTask():
        return 'This is setPendingTask route'

    @app.route(url+'set-finished-task', methods=['GET', 'POST'])
    def setFinishedTask():
        return 'This is setFinishedTask route'


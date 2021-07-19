def user(app, url):
    @app.route(url+'get-user', methods=['GET'])
    def getUser():
        return 'This is getUSer route'

    @app.route(url+'get-users', methods=['GET'])
    def getUsers():
        return 'This is getUsers route'

    @app.route(url+'set-user', methods=['GET', 'POST'])
    def setUser():
        return 'This is setUser route'

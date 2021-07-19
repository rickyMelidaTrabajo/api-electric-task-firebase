def technician(app, url):

    @app.route(url+'get-technician', methods=['GET'])
    def getTechnician():
        return 'this is apart route of technician'

    @app.route(url+'get-technicians', methods=['GET'])
    def getTechnicians():
        return 'This is the getTechnicians route'

    @app.route(url+'set-technician', methods=['GET', 'POST'])
    def setTechnician():
        return 'This is the setTechnician route'


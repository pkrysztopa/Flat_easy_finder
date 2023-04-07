import ui

if __name__ == "__main__":
    app = ui.create_app()
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

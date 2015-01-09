from flask.ext.script import Manager

from charts import create_app
from charts.app import print_stats

app = create_app()
manager = Manager(app)

@manager.command
def run_debug(port=5000):
    app.run(host='0.0.0.0', debug=True, port=int(port))

@manager.command
def stats():
    print_stats()

if __name__ == "__main__":
    manager.run()

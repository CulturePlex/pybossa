"""
Creates shell using IPython
"""
from werkzeug import script

from pybossa import model
from pybossa.core import create_app, db


def make_shell():
    return dict(app=create_app(),
                model=model,
                db_session=db.session)

if __name__ == "__main__":

    script.make_shell(make_shell, use_ipython=True)()

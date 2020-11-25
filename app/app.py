from flask import Flask
from flask_graphql import GraphQLView

from app.models.models import db_session
from app.schemas.schemas import schema, Department


def generate_app():
    app = Flask(__name__)
    app.debug = True

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
        ),
    )


if __name__ == "__main__":
    generate_app()
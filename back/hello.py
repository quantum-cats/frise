import graphene


class Website(graphene.ObjectType):
    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()


class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())

    def resolve_website(self, info, url):
        extracted = extract(url)
        return Website(url=url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image)


schema1 = graphene.Schema(query=Query)

import events

class Event(graphene.ObjectType):
    date = graphene.String(required=True)
    location = graphene.String()
    details = graphene.String()
    author = graphene.String()
    labels = graphene.String()


class EventQuery(graphene.ObjectType):
    event = graphene.Field(Event, date=graphene.String())

    def resolve_event(self, info, date):
        event = events.get_all_events(date)[0]
        return Event(date=date,
                     location=event.location,
                     details=event.details,
                     labels=event.labels,
                     author=event.author)


eventSchema = graphene.Schema(query=EventQuery)
result = eventSchema.execute('{ event }')
print(result.data['eventSchema'])  # "Hello World"

from flask import Flask
from flask_graphql import GraphQLView
from extraction_tutorial.schema import schema

app = Flask(__name__)
app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
app.run()

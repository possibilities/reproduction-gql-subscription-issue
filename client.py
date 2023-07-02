from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

transport = WebsocketsTransport(url="ws://localhost:3000/graphql")

client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

query = gql(
    """
    subscription Count {
        count(target: 10)
    }
"""
)

for result in client.subscribe(query):
    print(result)

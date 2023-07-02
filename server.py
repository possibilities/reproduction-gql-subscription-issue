import asyncio
import strawberry
from typing import AsyncGenerator
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class Widget:
    name: str


def create_app() -> web.Application:
    @strawberry.type
    class Query:
        widget: Widget

    @strawberry.type
    class Subscription:
        @strawberry.subscription
        async def count(self, target: int) -> AsyncGenerator[int, None]:
            for i in range(target):
                yield i + 1
                await asyncio.sleep(0.5)

    schema = strawberry.Schema(query=Query, subscription=Subscription)

    app = web.Application()
    app.router.add_route("*", "/graphql", GraphQLView(schema=schema))
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, port=3000)

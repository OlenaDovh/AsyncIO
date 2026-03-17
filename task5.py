from aiohttp import web
import asyncio


async def handle_root(request: web.Request) -> web.Response:
    """
    Handles the root route.
    Returns a simple 'Welcome, this is slow operation' message.
    """
    return web.Response(text="Welcome, this is slow operation")


async def handle_slow(request: web.Request) -> web.Response:
    """
    Handles the /slow route.
    Simulates a long-running operation without blocking the server.
    """
    print("Start slow operation")
    await asyncio.sleep(5)
    print("Slow operation finished")
    return web.Response(text="Operation completed")


async def make_app() -> web.Application:
    """
    Creates and configures the aiohttp application.
    """
    app = web.Application()

    app.add_routes([
        web.get('/', handle_root),
        web.get('/slow', handle_slow)
    ])
    return app


if __name__ == "__main__":
    app = asyncio.run(make_app())
    web.run_app(app, host='127.0.0.1', port=8080)

import jwt

from starlette.requests import Request

from fastapi_sqlalchemy import middleware


def test_middleware_upstream(session, app, client):
    @app.get("/payload")
    async def _get(
            request: Request
    ):
        return request.state.payload

    app.add_middleware(middleware.UpstreamPayloadMiddleware)

    headers = {
        "X-Payload-username": "testuser"
    }

    res = client.get("/payload", headers=headers)
    assert res.status_code == 200
    assert res.json() == {"username": "testuser"}


def test_middleware_jwt(session, app, client):
    @app.get("/payload")
    async def _get(
            request: Request
    ):
        return request.state.payload

    secret = "s0secret"
    app.add_middleware(middleware.JwtMiddleware, secret=secret)

    payload = {
        "username": "testuser"
    }
    token = jwt.encode(payload, secret).decode("utf-8")

    res = client.get("/payload", cookies={"jwt": token})
    assert res.status_code == 200
    assert res.json() == payload
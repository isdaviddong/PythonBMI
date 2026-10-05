import os

from waitress import serve

from app import app


if __name__ == "__main__":
    port = os.environ.get("HTTP_PLATFORM_PORT")
    if not port:
        raise RuntimeError("HTTP_PLATFORM_PORT must be provided by IIS HttpPlatformHandler")
    serve(app, host="127.0.0.1", port=int(port))

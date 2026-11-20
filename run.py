import uvicorn

HOST = "0.0.0.0"
PORT = 8000

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:application",
        host=HOST,
        port=PORT,
        reload=True,
        workers=1,
        log_level="info"
    )

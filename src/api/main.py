import uvicorn

def main():
    uvicorn.run("routers.api:app", port = 8000, reload = True)
    #uvicorn.run("api:app", port = 8000, host = '0.0.0.0', reload = True)
    #uvicorn.run("api:app", port = 8000, host = '0.0.0.0', debug = True, reload = True)

if __name__ == "__main__":
    main()
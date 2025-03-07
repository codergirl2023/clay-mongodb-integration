import uvicorn
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server.app:app", host="0.0.0.0", port=port, reload=True)
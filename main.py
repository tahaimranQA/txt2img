from fastapi import FastAPI
import requests  # Import the requests library

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, Fast"}


@app.get("/convert_text_to_image/{text}")
def convert_text_to_image(text: str):
    # Replace 'txt2img_service_url' with the actual URL of the txt2img service
    txt2img_service_url = "https://www.fotor.com/images/create"

    # Make a request to the txt2img service
    response = requests.get(f"{txt2img_service_url}", json={"cat": text})

    if response.status_code == 200:
        # Successfully received an image from txt2img service
        return {"image": response.content}
    else:
        return {"error": "Unable to convert text to image"}

@app.get("/health")
def check_health():
    # Add any health checks here
    # Example: Check if the txt2img service is reachable
    txt2img_service_url = "https://www.fotor.com/images/create"
    try:
        response = requests.get(txt2img_service_url)
        response.raise_for_status()
        return {"status": "ok", "message": "Service is healthy"}
    except requests.exceptions.RequestException as e:
        # raise HTTPException(status_code=503, detail=f"Service is unhealthy: {str(e)}")



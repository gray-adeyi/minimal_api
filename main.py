from fastapi import FastAPI, status
from enum import Enum
from datetime import datetime


app = FastAPI()


class Track(str, Enum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    MOBILE = "mobile"
    GENERAL = "general"
    PRODUCT_DESIGN = "product_design"
    VIDEO_MARKETING = "video_marketing"


@app.get("/")
def index(slack_name: str = "Gbenga Adeyi", track: Track = Track.BACKEND):
    timestamp = datetime.now()
    return {
        "slack_name": slack_name,
        "current_day": timestamp.strftime("%A"),
        "utc_time": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": "",
        "github_repo_url": "",
        "status_code": status.HTTP_200_OK,
    }

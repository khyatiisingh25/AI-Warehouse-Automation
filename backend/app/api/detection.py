from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, UploadFile

from app.schemas.detection import DetectionResponse
from app.services.ai.detector import YOLODetector


router = APIRouter(prefix="/detection", tags=["AI Detection"])

detector = YOLODetector()


@router.post("", response_model=DetectionResponse)
async def detect_objects(
    file: UploadFile = File(...),
) -> DetectionResponse:
    """Detect objects in an uploaded image."""

    suffix = Path(file.filename or "").suffix or ".jpg"

    with NamedTemporaryFile(delete=False, suffix=suffix) as temporary_file:
        temporary_path = Path(temporary_file.name)
        temporary_file.write(await file.read())

    try:
        detections = detector.predict(str(temporary_path))
        return DetectionResponse(detections=detections)
    finally:
        temporary_path.unlink(missing_ok=True)

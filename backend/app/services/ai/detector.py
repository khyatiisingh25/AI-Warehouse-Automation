from pathlib import Path
from typing import List

from ultralytics import YOLO

from app.schemas.detection import (
    BoundingBox,
    DetectionResult,
)


class YOLODetector:
    """Run YOLO inference and convert results into our API schema."""

    def __init__(self, model_path: str = "yolov8n.pt") -> None:
        self.model = YOLO(model_path)

    def predict(self, image_path: str) -> List[DetectionResult]:
        """Run object detection on an image."""

        if not Path(image_path).is_file():
            raise FileNotFoundError(
                f"Image file not found: {image_path}"
            )

        results = self.model.predict(
            source=image_path,
            verbose=False,
        )

        detections: List[DetectionResult] = []

        for result in results:
            names = result.names

            if result.boxes is None:
                continue

            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                x1, y1, x2, y2 = (
                    float(coordinate)
                    for coordinate in box.xyxy[0]
                )

                detections.append(
                    DetectionResult(
                        class_name=names[class_id],
                        confidence=confidence,
                        bounding_box=BoundingBox(
                            x1=x1,
                            y1=y1,
                            x2=x2,
                            y2=y2,
                        ),
                    )
                )

        return detections
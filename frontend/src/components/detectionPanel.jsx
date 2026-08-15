import { useState } from "react";
import { detectProducts } from "../api/detectionApi";

function DetectionPanel() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [detections, setDetections] = useState([]);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files?.[0];

    setFile(selectedFile || null);
    setDetections([]);
    setError("");
  };

  const handleDetection = async () => {
    if (!file) {
      setError("Please select an image first.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setDetections([]);

      const response = await detectProducts(file);

      setDetections(response.detections || []);
    } catch (err) {
      setError(err.message || "Detection request failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="page-placeholder">
      <div className="detection-panel">
        <div className="placeholder-icon">🔍</div>

        <h2>AI Detection</h2>

        <p>
          Upload an image to detect products using the warehouse AI backend.
        </p>

        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
        />

        {file && <p>Selected: {file.name}</p>}

        <button
          type="button"
          onClick={handleDetection}
          disabled={loading}
        >
          {loading ? "Detecting..." : "Detect Products"}
        </button>

        {error && (
          <p className="detection-error">
            {error}
          </p>
        )}

        {detections.length > 0 && (
          <div className="detection-results">
            <h3>Detection Results</h3>

            {detections.map((detection, index) => (
              <div
                className="detection-result"
                key={`${detection.class_name}-${index}`}
              >
                <strong>{detection.class_name}</strong>

                <span>
                  Confidence:{" "}
                  {(detection.confidence * 100).toFixed(1)}%
                </span>

                <span>
                  Box:{" "}
                  {detection.bounding_box.x1},{" "}
                  {detection.bounding_box.y1},{" "}
                  {detection.bounding_box.x2},{" "}
                  {detection.bounding_box.y2}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}

export default DetectionPanel;
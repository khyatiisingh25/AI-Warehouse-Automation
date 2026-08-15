import PropTypes from "prop-types";
import "./RobotVisualization.css";

const ROBOT_STATES = {
  IDLE: "IDLE",
  MOVING: "MOVING",
  WAITING: "WAITING",
  BLOCKED: "BLOCKED",
  COMPLETED: "COMPLETED",
};

const isSamePosition = (first, second) =>
  first?.row === second?.row && first?.column === second?.column;

const isRoutePosition = (position, route = []) =>
  route.some((point) => isSamePosition(point, position));

function RobotVisualization({
  rows,
  columns,
  robotId,
  currentPosition,
  targetPosition,
  route = [],
  state = ROBOT_STATES.IDLE,
}) {
  if (!rows || !columns || rows <= 0 || columns <= 0) {
    return (
      <section className="robot-visualization">
        <div className="robot-visualization__empty">
          Warehouse dimensions are not configured yet.
        </div>
      </section>
    );
  }

  const normalizedState = ROBOT_STATES[state]
    ? state
    : ROBOT_STATES.IDLE;

  const gridCells = [];

  for (let row = 0; row < rows; row += 1) {
    for (let column = 0; column < columns; column += 1) {
      const position = { row, column };

      const isCurrent = isSamePosition(position, currentPosition);
      const isTarget = isSamePosition(position, targetPosition);
      const isRoute = isRoutePosition(position, route);

      gridCells.push(
        <div
          key={`${row}-${column}`}
          className={[
            "robot-grid__cell",
            isRoute ? "robot-grid__cell--route" : "",
            isTarget ? "robot-grid__cell--target" : "",
            isCurrent ? "robot-grid__cell--current" : "",
          ]
            .filter(Boolean)
            .join(" ")}
          aria-label={`Warehouse position row ${row}, column ${column}`}
        >
          {isCurrent && (
            <span
              className={`robot-marker robot-marker--${normalizedState.toLowerCase()}`}
              title={`Robot ${robotId} - ${normalizedState}`}
            >
              🤖
            </span>
          )}

          {isTarget && !isCurrent && (
            <span className="robot-target" title="Target position">
              🎯
            </span>
          )}
        </div>,
      );
    }
  }

  return (
    <section className="robot-visualization">
      <div className="robot-visualization__header">
        <div>
          <h3>Digital Twin</h3>
          <p>Robot warehouse movement</p>
        </div>

        <span
          className={`robot-state robot-state--${normalizedState.toLowerCase()}`}
        >
          {normalizedState}
        </span>
      </div>

      <div
        className="robot-grid"
        style={{
          gridTemplateColumns: `repeat(${columns}, minmax(32px, 1fr))`,
        }}
      >
        {gridCells}
      </div>

      <div className="robot-details">
        <div>
          <span>Robot</span>
          <strong>{robotId || "—"}</strong>
        </div>

        <div>
          <span>Current Position</span>
          <strong>
            {currentPosition
              ? `(${currentPosition.row}, ${currentPosition.column})`
              : "—"}
          </strong>
        </div>

        <div>
          <span>Target Position</span>
          <strong>
            {targetPosition
              ? `(${targetPosition.row}, ${targetPosition.column})`
              : "—"}
          </strong>
        </div>

        <div>
          <span>Route Points</span>
          <strong>{route.length}</strong>
        </div>
      </div>

      <div className="robot-state-legend">
        {Object.values(ROBOT_STATES).map((robotState) => (
          <span key={robotState}>
            <i
              className={`robot-state-dot robot-state-dot--${robotState.toLowerCase()}`}
            />
            {robotState}
          </span>
        ))}
      </div>
    </section>
  );
}

RobotVisualization.propTypes = {
  rows: PropTypes.number.isRequired,
  columns: PropTypes.number.isRequired,
  robotId: PropTypes.string,
  currentPosition: PropTypes.shape({
    row: PropTypes.number,
    column: PropTypes.number,
  }),
  targetPosition: PropTypes.shape({
    row: PropTypes.number,
    column: PropTypes.number,
  }),
  route: PropTypes.arrayOf(
    PropTypes.shape({
      row: PropTypes.number,
      column: PropTypes.number,
    }),
  ),
  state: PropTypes.oneOf(Object.values(ROBOT_STATES)),
};

export default RobotVisualization;
from app.services.ai.demand.service import DemandPredictionService


def test_demand_prediction():
    service = DemandPredictionService()

    result = service.predict(
        product_id="PROD-01",
        historical_demand=[100, 120, 140],
    )

    assert result.product_id == "PROD-01"
    assert result.predicted_demand == 120


def test_demand_prediction_rejects_empty_history():
    service = DemandPredictionService()

    try:
        service.predict(
            product_id="PROD-02",
            historical_demand=[],
        )
        assert False
    except ValueError:
        assert True


def test_demand_prediction_rejects_negative_values():
    service = DemandPredictionService()

    try:
        service.predict(
            product_id="PROD-03",
            historical_demand=[100, -20, 80],
        )
        assert False
    except ValueError:
        assert True

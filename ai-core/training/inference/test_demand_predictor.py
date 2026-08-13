from demand_predictor import predict_next_day_demand


def test_predict_next_day_demand():
    prediction = predict_next_day_demand(35)

    assert isinstance(prediction, float)
    assert abs(prediction - 34.89374601148692) < 0.01


if __name__ == "__main__":
    test_predict_next_day_demand()
    print("Test passed")
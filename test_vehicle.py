from vehicle import vehicle_decision

def test_obstacle_detection():
    assert vehicle_decision("OBSTACLE") == "STOP VEHICLE"

def test_clear_road():
    assert vehicle_decision("CLEAR") == "MOVE FORWARD"

def test_sensor_error():
    assert vehicle_decision("ERROR") == "CHECK SENSOR"
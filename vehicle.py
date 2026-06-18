def vehicle_decision(sensor_status):

    if sensor_status == "OBSTACLE":
        return "STOP VEHICLE"

    elif sensor_status == "CLEAR":
        return "MOVE FORWARD"

    else:
        return "CHECK SENSOR"

if __name__ == "__main__":

    sensor_status = input("Enter Sensor Status: ")

    print(vehicle_decision(sensor_status))
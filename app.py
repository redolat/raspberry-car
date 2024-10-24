from flask import Flask, jsonify, request
from gpiozero import Motor

app = Flask(__name__)

# Define the GPIO pins for each motor
motor1 = Motor(forward=17, backward=18)  # GPIO pins for Motor 1
motor2 = Motor(forward=22, backward=23)  # GPIO pins for Motor 2
motor3 = Motor(forward=24, backward=25)  # GPIO pins for Motor 3

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the DC Motor Control API!"})

@app.route('/motor/<int:motor_id>/<string:direction>', methods=['POST'])
def control_motor(motor_id, direction):
    if motor_id == 1:
        motor = motor1
    elif motor_id == 2:
        motor = motor2
    elif motor_id == 3:
        motor = motor3
    else:
        return jsonify({"error": "Invalid motor ID!"}), 400

    if direction == "cw":
        motor.forward()
    elif direction == "ccw":
        motor.backward()
    else:
        return jsonify({"error": "Invalid direction! Use 'cw' or 'ccw'"}), 400

    return jsonify({"motor": motor_id, "direction": direction})

@app.route('/motor/<int:motor_id>/stop', methods=['POST'])
def stop_motor(motor_id):
    if motor_id == 1:
        motor = motor1
    elif motor_id == 2:
        motor = motor2
    elif motor_id == 3:
        motor = motor3
    else:
        return jsonify({"error": "Invalid motor ID!"}), 400

    motor.stop()
    return jsonify({"motor": motor_id, "status": "stopped"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
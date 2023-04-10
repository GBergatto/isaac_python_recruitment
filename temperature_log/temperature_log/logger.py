import rclpy
from std_msgs.msg import Float32
from datetime import datetime


class TemperatureLogger:
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "w")
        print("Temperature logger started at", datetime.now(), file=f)
        f.close()

    def callback(self, temperature: Float32):
        with open(self.filename, "a") as f:
            if (temperature.data >= 50):
                print(f"{datetime.now()}\t{temperature.data}", file=f)


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('temperature_logger')
    node.get_logger().info("Hello! Temperature logger node started!")

    tl = TemperatureLogger('log.txt')
    sub = node.create_subscription(Float32, "temperature", tl.callback, 10)

    rclpy.spin(node)


if __name__ == '__main__':
    tl = TemperatureLogger('log.txt')
    main()

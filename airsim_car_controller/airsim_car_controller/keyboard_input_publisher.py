import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pynput import keyboard

class KeyboardInputNode(Node):
    def __init__(self):
        super().__init__('keyboard_input_node')
        self.publisher_ = self.create_publisher(String, 'keyboard_input', 10)
        self.get_logger().info("keyboard input publisher Initialized")
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        msg = String()
        try:
            if key.char == 'w':
                msg.data = 'up'
            elif key.char == 's':
                msg.data = 'down'
            elif key.char == 'a':
                msg.data = 'left'
            elif key.char == 'd':
                msg.data = 'right'
        except AttributeError:
            if key == keyboard.Key.space:
                msg.data = 'space'
        
        self.publisher_.publish(msg)
      

    def on_release(self, key):
        msg = String()
        try:
            if key.char == 'w':
                msg.data = 'release_up'
            elif key.char == 's':
                msg.data = 'release_down'
            elif key.char == 'a':
                msg.data = 'release_left'
            elif key.char == 'd':
                msg.data = 'release_right'
        except AttributeError:
            pass

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardInputNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

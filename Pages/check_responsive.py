import time
from Pages.base_page import BasePage


class Responsiveness(BasePage):
    def test_responsiveness_on_multiple_devices(self):
        devices = [
            {"name": "Desktop", "width": 1920, "height": 1080}, #full HD
            {"name": "Desktop", "width": 2560, "height": 1440},  # full HD
            {"name": "Tablet", "width": 1024, "height": 1366}, #ipad pro
            {"name": "Mobile", "width": 430, "height": 932} ,#iphone 14 pro max
            {"name": "nest_hub_max", "width": 1280, "height": 800} , #nest hub max
            {"name": "samsung_galaxy", "width": 412, "height": 915},  # samsung galaxy s20 ultra
        ]
        for device in devices:
            self.driver.set_window_size(device["width"], device["height"])
            time.sleep(1)
            print(f"\nTesting on {device['name']} ({device['width']}x{device['height']})")
            self.scroll_updown_to_check_responsive()
            print(f"PASSED : {device['name']}")

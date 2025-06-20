import psutil
import time

# Set the CPU usage threshold
THRESHOLD = 30  # in percent

def monitor_cpu():
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")

    try:
        while True:
            # Get current CPU usage over 1 second
            cpu_usage = psutil.cpu_percent(interval=1)

            # Display alert if usage exceeds the threshold
            if cpu_usage > THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Optional: Print regular updates even if under threshold
            # else:
            #     print(f"CPU usage is normal: {cpu_usage}%")

            time.sleep(1)  # Small delay to avoid excessive polling

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the function
if __name__ == "__main__":
    monitor_cpu()


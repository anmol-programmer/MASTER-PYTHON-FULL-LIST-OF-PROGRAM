import time

class Notification:
    def send(self, message, priority):
        pass

class Email(Notification):
    def send(self, message, priority):
        print(f"Email sent | Priority: {priority} | Message: {message}")

class SMS(Notification):
    def send(self, message, priority):
        print(f"SMS sent | Priority: {priority} | Message: {message}")

class PushNotification(Notification):
    def send(self, message, priority):
        print(f"Push notification sent | Priority: {priority} | Message: {message}")

def send_with_retry(notification, message, priority, retries=3):
    for attempt in range(1, retries + 1):
        try:
            if attempt < retries:
                raise Exception("Temporary failure")

            notification.send(message, priority)
            print("Status: Success\n")
            return

        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(1)

    print("Notification delivery failed after retries\n")

while True:
    print("""
--- Notification System ---
1. Send Email
2. Send SMS
3. Send Push Notification
4. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("System exited.")
        break

    message = input("Enter message: ")

    print("""
Select Priority:
1. HIGH
2. MEDIUM
3. LOW
""")

    p = int(input("Enter priority: "))
    priority = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}.get(p, "LOW")

    match choice:
        case 1:
            notifier = Email()
        case 2:
            notifier = SMS()
        case 3:
            notifier = PushNotification()
        case _:
            print("Invalid option\n")
            continue

    send_with_retry(notifier, message, priority)

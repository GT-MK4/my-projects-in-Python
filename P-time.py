import time

# Ask user for minutes
minutes = int(input("Enter minutes: "))
seconds = 0  # start at 0 seconds

while True:
    # Display the clock in MM:SS format
    print(f"\rWait to end timer: {minutes:02d}:{seconds:02d}", end="")

    # Stop when timer reaches 0:00
    if minutes == 0 and seconds == 0:
        print("\n🎉 Timer ended!")
        break

    # Wait 1 second
    time.sleep(1)

    # Countdown logic
    if seconds == 0:
        if minutes > 0:
            minutes -= 1
            seconds = 59
    else:
        seconds -= 1


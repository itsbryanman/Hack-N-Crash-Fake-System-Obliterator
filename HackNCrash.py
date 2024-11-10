import time
import sys
import random

# Display text with typing effect
def type_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Generate random 'hacker-like' commands
def generate_hacker_command():
    commands = [
        "establishing connection to 127.0.0.1...",
        "accessing root@domain...",
        "initiating protocol bypass...",
        "decrypting security key...",
        "injecting payload...",
        "downloading sensitive data...",
        "establishing backdoor...",
        "updating DNS records...",
        "spoofing IP address...",
        "writing data to cache...",
        "overclocking CPU..."
    ]
    return random.choice(commands)

# Simulate the "hacking" phase
def hacking_sequence():
    type_text("Starting hack simulation...", speed=0.1)
    for _ in range(15):
        cmd = generate_hacker_command()
        type_text(f"> {cmd}", speed=0.03)
        time.sleep(random.uniform(0.1, 0.3))

# Dramatic obliteration phase
def obliterate_sequence():
    type_text("\nWARNING: SYSTEM BREACH IMMINENT", speed=0.1)
    for _ in range(5):
        type_text("!! ALERT !! MEMORY OVERLOAD DETECTED !!", speed=0.02)
        time.sleep(0.5)
    
    type_text("\n!!! INITIATING SELF-DESTRUCT SEQUENCE !!!", speed=0.1)
    time.sleep(1)
    
    obliteration_text = [
        "!!! FILESYSTEM CORRUPTION DETECTED !!!",
        "!!! PURGING ALL LOG FILES !!!",
        "!!! ERASE ALL MEMORY MODULES !!!",
        "!!! SHUTTING DOWN NETWORK INTERFACE !!!",
        "!!! DESTROYING ALL TRACE EVIDENCE !!!"
    ]
    
    for line in obliteration_text:
        type_text(line, speed=0.08)
        time.sleep(0.5)

    # End with a dramatic shutdown
    type_text("\nSystem shutdown imminent...", speed=0.1)
    time.sleep(2)
    type_text("Goodbye.", speed=0.1)

# Main function to run the simulation
def main():
    hacking_sequence()
    obliterate_sequence()

if __name__ == "__main__":
    main()

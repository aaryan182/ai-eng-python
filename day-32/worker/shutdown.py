import signal
import sys
from worker.worker import running

def handle_shutdown(sig, frame):
    global running
    print("[WORKER] Graceful shutdown")
    running = False
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)

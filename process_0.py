import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# Check if Redis is installed
redis_installed = run_command("which redis-server")
print("Redis installation:", "Found" if redis_installed else "Not found")

# Check if Redis is running
redis_running = run_command("pgrep redis-server")
print("Redis process:", "Running" if redis_running else "Not running")

# Check Redis version
redis_version = run_command("redis-server --version")
print("Redis version:", redis_version if redis_version else "Unable to determine")
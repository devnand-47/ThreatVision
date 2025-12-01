from flask import Flask, render_template, jsonify
import requests
import random
import time

app = Flask(__name__)

# --- CONFIGURATION ---
# We use a real live list of SSH Brute Force attackers
THREAT_FEED_URL = "https://lists.blocklist.de/lists/ssh.txt"
GEO_API_URL = "http://ip-api.com/json/{}"

# Cache to store the bad IPs so we don't download the file every second
bad_ips = []

def update_threat_intel():
    """Downloads the latest list of real attackers"""
    global bad_ips
    try:
        print(" [*] Downloading Real Threat Data...")
        response = requests.get(THREAT_FEED_URL, timeout=10)
        if response.status_code == 200:
            # Split by line and take the top 500 IPs to save memory
            bad_ips = response.text.split('\n')[:500]
            # Filter out empty lines
            bad_ips = [ip for ip in bad_ips if ip]
            print(f" [+] Loaded {len(bad_ips)} real malicious IPs.")
        else:
            print(" [-] Failed to download data. Using simulation mode.")
    except Exception as e:
        print(f" [!] Error updating feed: {e}")

# Load data immediately on startup
update_threat_intel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/feed')
def feed():
    """Fetches a REAL attacker and geolocates them"""
    
    # 1. Pick a random bad IP from our real list
    if not bad_ips:
        real_ip = "1.1.1.1" # Fallback if list is empty
    else:
        real_ip = random.choice(bad_ips)

    try:
        # 2. Geolocate the IP (Free API)
        # Note: In a production app, you would use a local database (GeoLite2) 
        # to avoid rate limits. For this demo, we use the free API.
        geo_response = requests.get(GEO_API_URL.format(real_ip), timeout=2).json()
        
        if geo_response['status'] == 'fail':
            # If Geo-lookup fails, pretend it's from "Unknown" to keep map running
            src_country = "Unknown Origin"
            src_lat = 0
            src_lon = 0
        else:
            src_country = geo_response.get('country', 'Unknown')
            src_lat = geo_response.get('lat', 0)
            src_lon = geo_response.get('lon', 0)

    except:
        src_country = "Hidden Proxy"
        src_lat = 0
        src_lon = 0

    # 3. Target is "Your Server" (We simulate your location for the visual)
    # Let's pretend your server is in the USA (Virginia Data Center)
    dst_country = "Your Server (Protected)"
    dst_lat = 39.0438
    dst_lon = -77.4874

    attack_data = {
        "id": random.randint(10000, 99999),
        "type": "SSH Brute Force", # Since we are using the SSH blocklist
        "src_ip": real_ip, # SHOW THE REAL IP
        "src_country": src_country,
        "src_lat": src_lat,
        "src_lon": src_lon,
        "dst_country": dst_country,
        "dst_lat": dst_lat,
        "dst_lon": dst_lon,
        "timestamp": time.strftime("%H:%M:%S")
    }
    
    return jsonify(attack_data)

if __name__ == '__main__':
    print(" [+] THREATVISION CTI DASHBOARD STARTED...")
    app.run(debug=True, port=5001)

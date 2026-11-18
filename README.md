# Motorcycle CarPlay Dashboard (for iPhone 6 Plus)

A lightweight, high-contrast Apple CarPlay-style dashboard built specifically for mounting an **iPhone 6 Plus** (running iOS 12.5.7) on a motorcycle fuel tank or handlebar mount, tethered to an **iPhone 14 Pro** hotspot.

---

## Features

1. **Apple CarPlay Split Dashboard Layout**:
   - **Left**: Live interactive map with GPS location and follow-me navigation.
   - **Right Top**: Large digital GPS speedometer (km/h or mph) with heading and altitude.
   - **Right Middle**: Glove-friendly music & audio player with large physical touch targets.
   - **Right Bottom**: Quick action shortcuts (Day/Night high contrast, Spotify/Apple Maps deep links).
   - **Left Dock**: Status clock, connectivity indicators, and quick app switcher.
2. **Turn-by-Turn Navigation**:
   - Tap the Search icon on the map to search any destination.
   - Live turn guidance banner with distance and maneuver instructions via OSRM.
3. **Screen Keep-Awake**:
   - Uses an invisible HTML5 video loop so iOS Safari will **never lock or turn off the screen** while you ride.
4. **Optimized for iPhone 6 Plus (1 GB RAM / A8 Chip)**:
   - Built with pure HTML5/CSS/JavaScript (no heavy frameworks).
   - Consumes under 30 MB of RAM, preventing crashes and overheating.

---

## How to Deploy with Free HTTPS (Recommended for Road Riding)

> [!IMPORTANT]
> iOS Safari requires **HTTPS** to allow GPS location and speedometer access. Deploying this single file to **GitHub Pages** gives you a free, permanent HTTPS link that works anywhere on your motorcycle via your iPhone 14 Pro hotspot.

### Step 1: Upload to GitHub Pages
1. Create a new free repository on [GitHub](https://github.com/new) named `moto-carplay`.
2. Upload `index.html` from this folder to the repository.
3. In your repository on GitHub, go to **Settings → Pages**.
4. Under **Branch**, select `main` and `/ (root)`, then click **Save**.
5. GitHub will provide your free HTTPS link (e.g. `https://<your-username>.github.io/moto-carplay/`).

### Step 2: Open and Add to Home Screen on iPhone 6 Plus
1. Connect your iPhone 6 Plus to your iPhone 14 Pro's hotspot.
2. Open **Safari** on the iPhone 6 Plus and navigate to your GitHub Pages URL.
3. Tap **Allow** when Safari prompts for Location Access.
4. Tap the **Share** button (the square with an arrow at the bottom of Safari).
5. Tap **Add to Home Screen**.
6. Name it **CarPlay** and tap **Add**.

### Step 3: Launch Full-Screen
* Tap the new **CarPlay** icon on your home screen.
* It will open **full-screen without any Safari URL bars or buttons**, looking and functioning exactly like a real CarPlay motorcycle screen!

---

## Local Testing on Laptop

To preview or test on your local network:
```powershell
python moto-carplay/server.py
```
Then visit `http://localhost:8080` in your computer's browser.

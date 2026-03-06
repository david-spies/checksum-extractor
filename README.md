<img width="1280" height="633" alt="chksum_extractor_" src="https://github.com/user-attachments/assets/606c7ff9-474a-4c50-b957-c7e80d79bc62" />

# CHKSUM HASH // EXTRACTOR
### Cryptographic Hash Extraction & Signature Verification Tool

```diff
+ ▓ AUTHORIZED USE ONLY | SHA-256 · SHA-512 · MD5 | INTEGRITY VERIFICATION SYSTEM ▓
```

A modern, browser-based cryptographic hash extractor rebuilt from a Python/Tkinter original. Drop any file, extract its hash, and verify it against a developer-published signature — all client-side with zero uploads, zero dependencies, and zero installs.

---

## Features

- **Three Hash Algorithms** — SHA-256, SHA-512, and MD5 available on demand
- **Drag & Drop or Browse** — supports `.exe`, `.msi`, `.iso`, and all file types
- **100% Client-Side** — all hashing is performed in your browser via the Web Crypto API and pure JavaScript; no file data ever leaves your machine
- **Signature Comparison** — paste a developer's published hash and run an instant verification check for a verified match or mismatch verdict
- **Copy & Export** — copy the extracted hash to clipboard or download it as a named `.txt` file
- **Live Progress Tracking** — real-time progress bar during file read and hash computation
- **Tech-Noir UI** — CRT scanline effects, glitch animations, solarized-green on black, slate blue accents, and monospace typography

---

## Usage

### 1. Open the App

Open `checksum-extractor.html` in any modern browser. No server required.

### 2. Load a Target File

Drag and drop your file onto the drop zone, or click to open a file browser. Supported types: `.exe` `.msi` `.iso` and all others.

### 3. Select an Algorithm

Choose from the algorithm panel on the right:

| Algorithm | Output Length | Use Case |
|-----------|--------------|----------|
| **SHA-256** | 64 hex chars | Recommended — most common standard |
| **SHA-512** | 128 hex chars | High-security verification |
| **MD5** | 32 hex chars | Legacy compatibility |

### 4. Execute Extraction

Click **▶ EXECUTE HASH EXTRACTION**. A progress bar will track the read and computation. Large files (2 GB+) may take 30–60 seconds.

### 5. Copy or Save the Hash

Once complete, use **⊕ COPY HASH** to copy to clipboard or **⬇ SAVE .TXT** to download a text file named after your target file and algorithm (e.g., `kali-linux_sha256.txt`).

### 6. Verify the Signature

Paste the developer's published hash into the **SIGNATURE VERIFY** panel and click **◈ RUN SIGNATURE COMPARISON**. The comparison is case-insensitive.

```diff
+ ✓ SIGNATURE MATCH     → File is authentic and unmodified
- ✗ SIGNATURE MISMATCH  → File may be corrupted or tampered with
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Runtime | Vanilla HTML5 / CSS3 / JavaScript (ES2020+) |
| Hashing (SHA-256, SHA-512) | Web Crypto API (`crypto.subtle.digest`) |
| Hashing (MD5) | Pure JS implementation (RFC 1321) |
| File I/O | FileReader API, Blob, Clipboard API |
| Fonts | Google Fonts — Orbitron · Share Tech Mono · VT323 |
| Dependencies | **None** |

---

## Performance Notes

- Files under ~500 MB process in under 5 seconds on modern hardware
- Files 500 MB – 2 GB typically complete in 5–30 seconds
- Files 2 GB+ may take 30–60 seconds depending on machine specs
- The browser tab remains responsive during processing

---

## Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome / Edge 89+ | ✓ Full |
| Firefox 90+ | ✓ Full |
| Safari 15+ | ✓ Full |
| Opera 76+ | ✓ Full |

> Requires a browser with Web Crypto API support. All modern browsers qualify.

---

## Security Notes

- **No network requests are made.** The application operates entirely offline after the initial page load (fonts may load from Google Fonts on first open).
- **No file data is transmitted.** All hashing runs in-memory within your browser's sandboxed JavaScript engine.
- **MD5 is included for legacy compatibility only.** MD5 is cryptographically broken and should not be used for security-critical verification. Prefer SHA-256 or SHA-512.

---

## Local / Offline Use

To run completely offline, download the Google Fonts used and update the `@import` in the `<style>` block, or replace with system monospace fonts:

```css
/* Replace the Google Fonts import with local fallbacks */
font-family: 'Courier New', Courier, monospace;
```

---

## Original Project

This application is a modern rebuild of the **Checksum Hash Extractor** originally written in Python with a Tkinter GUI by **David Spies**. The original supported SHA-256, SHA-512, and MD5 extraction with file-comparison via a `compare.txt` workflow.

The browser version retains full feature parity and adds drag-and-drop, inline comparison input, clipboard integration, and a client-side-only architecture.

---

## License

Open source. Free to use, modify, and distribute.

---

```diff
+ // END OF DOCUMENT — CHKSUM v2.0 — SYSTEM READY ▓
```

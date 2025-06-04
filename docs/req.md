To build a terminal multiplexer on **Windows in C/C++ using ConPTY**, here’s **exactly what you need to install** before starting:

---

## ✅ 1. **C/C++ Compiler & Build Tools**

Choose one of the following:

### 🔷 Option A: **Visual Studio (Recommended for ConPTY)**

* **Download**: [https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)
* During installation, select:

  * ✅ "Desktop development with C++"
  * ✅ "Windows 10/11 SDK"

✅ **Pros**:

* Full support for `ConPTY` and Win32 APIs
* Easy debugging
* Integrated terminal, build tools

---

### 🔷 Option B: **MSYS2 + MinGW (Alternative for CMake + GCC)**

* **Download**: [https://www.msys2.org/](https://www.msys2.org/)
* After install:

  ```bash
  pacman -Syu   # update
  pacman -S mingw-w64-x86_64-gcc cmake make
  ```

🟡 **Note**: ConPTY works best with MSVC, not GCC. MSYS2 + GCC *may* require more work for linking `kernel32.lib`.

---

## ✅ 2. **Windows SDK (for ConPTY)**

If you use **Visual Studio**, it comes with the **Windows 10 or 11 SDK**, which includes the necessary headers like:

* `consoleapi2.h`
* `winconpty.h`

You need:

* **Windows 10 version 1809 (build 17763) or later**

Check your SDK:

```sh
dir "C:\Program Files (x86)\Windows Kits\10\Include\"
```

Look for version `10.0.17763.0` or newer.

---

## ✅ 3. **CMake** (If not using Visual Studio)

* **Download**: [https://cmake.org/download/](https://cmake.org/download/)
* Used for managing build scripts

---

## ✅ 4. **Terminal Emulator (Optional)**

* **Windows Terminal**: Better experience than default `cmd.exe`

  * [https://aka.ms/terminal](https://aka.ms/terminal)

---

## ✅ 5. **Git (for cloning samples and version control)**

* **Download**: [https://git-scm.com/](https://git-scm.com/)

---

## ✅ 6. **(Optional but useful)** Editor

| Editor        | Why Use It                 |
| ------------- | -------------------------- |
| Visual Studio | Best for full Win32 apps   |
| VS Code       | Lightweight, great plugins |
| CLion         | CMake integration (paid)   |

---

## 📦 Final Checklist

| Tool/Component             | Status |
| -------------------------- | ------ |
| Visual Studio w/ C++ SDK   | ✅      |
| Windows SDK (>= 17763)     | ✅      |
| Git                        | ✅      |
| CMake (if not using VS)    | ✅      |
| Optional: Windows Terminal | ✅      |

---

Let me know which setup you're using (Visual Studio, MSYS2, or something else), and I can give you a ready-to-run **starter project** that uses `ConPTY` to launch a shell.

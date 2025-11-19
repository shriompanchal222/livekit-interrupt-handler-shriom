# livekit-interrupt-handler-shriom
A custom LiveKit interruption handler to ignore filler words during TTS and detect real user interruptions.
# LiveKit Interrupt Handler (Shriom)

A custom extension layer over LiveKit Agents to ignore filler words while
the agent is speaking and detect real user interruptions.

## What Changed
- Added `livekit_interrupt_handler.py`
- Added environment variable selection for ignored fillers
- Implements is_filler_only() and should_interrupt() logic
- Non-invasive: does NOT modify LiveKit base VAD

## What Works
- Ignores: "uh", "umm", "hmm", "haan" during TTS
- Detects real commands: "wait", "stop", "not that"
- Mixed fillers + command → interruption happens
- ASR text is filtered safely

## Environment Variable

## Steps to Test
1. Set environment variable:
   - Windows:
     ```
     setx IGNORED_WORDS "uh,umm,hmm,haan"
     ```
2. Run your agent using this handler.
3. Speak:
   - "umm" → ignored  
   - "stop" → agent stops  
   - "umm okay stop" → agent stops  

## Python Version
Python 3.10+  

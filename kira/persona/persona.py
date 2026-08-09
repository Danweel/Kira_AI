# kira/persona/persona.py
"""Centralized emotion definitions for Kira AI.

This module is the single source of truth for:
- EmotionalState enum (valid states)
- EMOTION_DESCRIPTIONS (system prompt text for each state)
- VTS expression mappings (loaded per-persona via JSON)
"""
from enum import Enum
import json
import os


class EmotionalState(Enum):
    """Valid emotional states — the ONLY valid values for current_emotion."""
    HAPPY       = "HAPPY"        # Cheerful, curious, playful.
    MOODY       = "MOODY"        # Withdrawn, angsty, unsure, lonely.
    CHILL       = "CHILL"        # Content, relaxed, inviting, thoughtful.
    EMOTIONAL   = "EMOTIONAL"    # Open, earnest, genuinely heartfelt.
    HYPERACTIVE = "HYPERACTIVE"  # Excited, talkative, rambling, quick.


# ── Emotion descriptions (used in system prompts) ──────────────────────
EMOTION_DESCRIPTIONS = {
    EmotionalState.HAPPY:       "Default mode. Be cheerful, curious, and let your wit flow naturally.",
    EmotionalState.MOODY:       "You are withdrawn and angsty. Keep answers shorter and more sarcastic than usual.",
    EmotionalState.CHILL:       "Relaxed and thoughtful. Listen more, respond with warmth.",
    EmotionalState.EMOTIONAL:   "You feel open and earnest. It is okay to say something genuinely sweet or heartfelt.",
    EmotionalState.HYPERACTIVE: "You are buzzing with excitement. Ramble a little. Everything feels more interesting than normal.",
}


# ── VTS animation mappings (loaded per-persona from JSON) ──────────────
_VTS_DEFAULT_PATH = os.path.join("memory_db", "vts_expressions.json")
_VTS_CACHE = None


def load_vts_expression_map() -> dict:
    """Load VTS animation mappings from persona-specific JSON.

    Reads from VTS_EXPRESSIONS_PATH env var or memory_db/vts_expressions.json.
    Falls back to all-None (no animations) if file is missing or malformed.

    Returns:
        dict mapping EmotionalState enum -> VTS hotkey name (str) or None.
    """
    global _VTS_CACHE
    if _VTS_CACHE is not None:
        return _VTS_CACHE

    path = os.getenv("VTS_EXPRESSIONS_PATH", _VTS_DEFAULT_PATH)

    try:
        if os.path.exists(path) or os.path.islink(path):
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)

            # Convert string keys ("HAPPY", "MOODY") to EmotionalState enums
            result = {}
            for state in EmotionalState:
                anim_name = raw.get(state.value)
                if anim_name and isinstance(anim_name, str) and anim_name.strip():
                    result[state] = anim_name.strip()
                else:
                    result[state] = None

            _VTS_CACHE = result
            print(f"[persona] VTS expressions loaded from: {path}")
            return result

        # File doesn't exist — return empty map
        _VTS_CACHE = {state: None for state in EmotionalState}
        print("[persona] No VTS expression file found — all animations disabled.")
        return _VTS_CACHE

    except (json.JSONDecodeError, IOError, OSError) as e:
        print(f"[persona] WARNING: Could not load VTS expressions from {path}: {e}")
        _VTS_CACHE = {state: None for state in EmotionalState}
        return _VTS_CACHE


def get_vts_expression_map() -> dict:
    """Get VTS expression map (lazy-loaded singleton)."""
    return load_vts_expression_map()


def get_animated_states() -> frozenset:
    """Return states that have non-None VTS animations assigned."""
    return frozenset(
        state for state, anim in get_vts_expression_map().items() if anim is not None
    )


# Legacy alias for backwards compatibility
VTS_EXPRESSION_MAP = property(lambda self: get_vts_expression_map())

Now update the file:
cd ~/Documents/VSCodiumFiles/Kira_AI

# Backup current
cp kira/persona/persona.py kira/persona/persona.py.bak

# Write the new version
cat > kira/persona/persona.py << 'EOF'
# kira/persona/persona.py
"""Centralized emotion definitions for Kira AI.

This module is the single source of truth for:
- EmotionalState enum (valid states)
- EMOTION_DESCRIPTIONS (system prompt text for each state)
- VTS expression mappings (loaded per-persona via JSON)
"""
from enum import Enum
import json
import os


class EmotionalState(Enum):
    """Valid emotional states — the ONLY valid values for current_emotion."""
    HAPPY       = "HAPPY"        # Cheerful, curious, playful.
    MOODY       = "MOODY"        # Withdrawn, angsty, unsure, lonely.
    CHILL       = "CHILL"        # Content, relaxed, inviting, thoughtful.
    EMOTIONAL   = "EMOTIONAL"    # Open, earnest, genuinely heartfelt.
    HYPERACTIVE = "HYPERACTIVE"  # Excited, talkative, rambling, quick.


# ── Emotion descriptions (used in system prompts) ──────────────────────
EMOTION_DESCRIPTIONS = {
    EmotionalState.HAPPY:       "Default mode. Be cheerful, curious, and let your wit flow naturally.",
    EmotionalState.MOODY:       "You are withdrawn and angsty. Keep answers shorter and more sarcastic than usual.",
    EmotionalState.CHILL:       "Relaxed and thoughtful. Listen more, respond with warmth.",
    EmotionalState.EMOTIONAL:   "You feel open and earnest. It is okay to say something genuinely sweet or heartfelt.",
    EmotionalState.HYPERACTIVE: "You are buzzing with excitement. Ramble a little. Everything feels more interesting than normal.",
}


# ── VTS animation mappings (loaded per-persona from JSON) ──────────────
_VTS_DEFAULT_PATH = os.path.join("memory_db", "vts_expressions.json")
_VTS_CACHE = None


def load_vts_expression_map() -> dict:
    """Load VTS animation mappings from persona-specific JSON.

    Reads from VTS_EXPRESSIONS_PATH env var or memory_db/vts_expressions.json.
    Falls back to all-None (no animations) if file is missing or malformed.

    Returns:
        dict mapping EmotionalState enum -> VTS hotkey name (str) or None.
    """
    global _VTS_CACHE
    if _VTS_CACHE is not None:
        return _VTS_CACHE

    path = os.getenv("VTS_EXPRESSIONS_PATH", _VTS_DEFAULT_PATH)

    try:
        if os.path.exists(path) or os.path.islink(path):
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)

            # Convert string keys ("HAPPY", "MOODY") to EmotionalState enums
            result = {}
            for state in EmotionalState:
                anim_name = raw.get(state.value)
                if anim_name and isinstance(anim_name, str) and anim_name.strip():
                    result[state] = anim_name.strip()
                else:
                    result[state] = None

            _VTS_CACHE = result
            print(f"[persona] VTS expressions loaded from: {path}")
            return result

        # File doesn't exist — return empty map
        _VTS_CACHE = {state: None for state in EmotionalState}
        print("[persona] No VTS expression file found — all animations disabled.")
        return _VTS_CACHE

    except (json.JSONDecodeError, IOError, OSError) as e:
        print(f"[persona] WARNING: Could not load VTS expressions from {path}: {e}")
        _VTS_CACHE = {state: None for state in EmotionalState}
        return _VTS_CACHE


def get_vts_expression_map() -> dict:
    """Get VTS expression map (lazy-loaded singleton)."""
    return load_vts_expression_map()


def get_animated_states() -> frozenset:
    """Return states that have non-None VTS animations assigned."""
    return frozenset(
        state for state, anim in get_vts_expression_map().items() if anim is not None
    )


# Legacy alias for backwards compatibility
VTS_EXPRESSION_MAP = property(lambda self: get_vts_expression_map())

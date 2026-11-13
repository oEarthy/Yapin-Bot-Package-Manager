"""
This project automatically runs the code at "https://www.yapin.gg/sdk/yapper.py"
This is just meant as a demonstration, and from a cybersecurity standpoint, this is horrible
Please make sure you use this project with an understanding of the risks when running it!

Author: Earthy
"""
import builtins
import time
from urllib.request import Request, urlopen

# You can use hour, minute, second, day, month, year for time and message for the message
# Example: "[<hour>:<minute>:<second>] [Yapper] <message>"
LOGGER_FORMAT = "[<hour>:<minute>:<second>] [Yapper] <message>"
DEBUG_MODE = True

def _yapper_print(*args, **kwargs):
    if not args or not isinstance(args[0], str) or not args[0].startswith("[yapper]"):
        return builtins.print(*args, **kwargs)

    sep = kwargs.get("sep")
    if sep is None:
        sep = " "
    message = sep.join(str(arg) for arg in args)
    message = message[len("[yapper]"):].lstrip()
    now = time.localtime()
    formatted = LOGGER_FORMAT
    for field, value in (
        ("day", time.strftime("%d", now)),
        ("month", time.strftime("%m", now)),
        ("year", time.strftime("%Y", now)),
        ("hour", time.strftime("%H", now)),
        ("minute", time.strftime("%M", now)),
        ("second", time.strftime("%S", now)),
        ("message", message),
    ):
        formatted = formatted.replace(f"<{field}>", value)
    return builtins.print(formatted, **kwargs)

def log_message(message):
    _yapper_print(f"[yapper] {message}")

def _log_command(msg):
    author = getattr(msg, "author", None) or "unknown"
    author_id = getattr(msg, "author_id", None)
    if author_id:
        author = f"{author} ({author_id})"
    
    # Could have probarly just the variable msg below but....
    if not msg.args:
        _yapper_print(f"[yapper] Recived /{msg.command} by {author}")
    else:
        _yapper_print(f"[yapper] Recived /{msg.command} {msg.args} by {author}")

def _enable_debug_command_logging():
    if not DEBUG_MODE:
        return

    # we pretend the error isnt there.... :]
    original_init = Bot.__init__ # type: ignore

    def init_with_debug_logging(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.on("command", _log_command)

    Bot.__init__ = init_with_debug_logging # type: ignore

def _load_sdk():
    url = "https://www.yapin.gg/sdk/yapper.py"
    request = Request(
        url,
        headers={
            "User-Agent": "yapper-sdk-fetcher/1.0",
            "Accept": "text/plain,*/*",
        },
    )

    with urlopen(request, timeout=30) as response:
        source = response.read().decode("utf-8")

    globals()["print"] = _yapper_print
    exec(compile(source, url, "exec"), globals()) # <--- horrible cyber security
    _enable_debug_command_logging()

_load_sdk()

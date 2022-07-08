import argparse
import configparser
import json

cfg = configparser.ConfigParser()
cfg.read('configs/conf.cfg')

VERSION = float(str(cfg.get('SYSTEM', 'version'))[1:-1])
DATE = cfg.get('SYSTEM', 'date')


argparser = argparse.ArgumentParser(description=cfg.get("SYSTEM", "desc"))
argparser.add_argument('-d', '--ducky', help=cfg.get("SYSTEM", "input_desc"))
argparser.add_argument('-i', '--ino', help=cfg.get("SYSTEM", "output_desc"))
argparser.add_argument('-v', '--verbose', action='count', default=0)
argparser.add_argument('--version', action='version',
                       version=f"Ducky Script to Arduino converter by caxapok v{VERSION}\nRelease date: {DATE[1:-1]}")

SPECIAL_BUTTONS = json.loads(open(cfg.get("ENCODER", "keyfile"), 'r').read())
DEFAULT_DELAY = int(cfg.get("DUCKY", "default_delay"))*10
code = ""


def read_script(script):
    with open(script, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parse_line(line)


def write_output(sample, keyword, ino_code, output):
    start_code, end_code = open(sample, "r").read().split(keyword)[:2]
    with open(output, 'w') as f:
        f.write(start_code)
        f.write(ino_code)
        f.write(end_code)


def delay(t):
    return f"\n    delay({t});"


def get_key_code(key):
    if SPECIAL_BUTTONS.get(str(key).lower()):
        return SPECIAL_BUTTONS[str(key).lower()]
    else:
        return f'\"{key}\"'


def parse_line(line):
    global code, DEFAULT_DELAY

    if line.startswith("\n"):
        return

    if line.startswith("REM"):
        comment = line.split("REM ")[1]
        code += f"\n    // {comment}"
        return

    if line.startswith("DEFAULT_DELAY") or line.startswith("DEFAULTDELAY"):
        DEFAULT_DELAY = int(line.split("DEFAULT_DELAY ")[1])*10
        return

    if line.startswith("DELAY"):
        d = int(line.split("DELAY ")[1])
        code += delay(d)
        return

    if line.startswith("STRING"):
        string = line.split("STRING ")[1]
        code += f"\n    Keyboard.print(\"{string}\");"
        code += delay(DEFAULT_DELAY)
        return

    if SPECIAL_BUTTONS.get(str(line.split(" ")[0]).lower()):
        keys = line.split(" ")
        for key in keys:
            code += f"\n    Keyboard.press({get_key_code(key)});"
        code += delay(100)
        code += f"\n    Keyboard.releaseAll();"
        code += delay(DEFAULT_DELAY)
        return

    if line.startswith("CTRL-SHIFT"):
        n = line.split("CTRL-SHIFT ")[1]
        code += f"\n    Keyboard.press(KEY_LEFT_CTRL);"
        code += f"\n    Keyboard.press(KEY_LEFT_SHIFT);"
        if SPECIAL_BUTTONS.get(str(n).lower()):
            code += f"\n    Keyboard.press({get_key_code(n)});"
        else:
            code += f"\n    Keyboard.print(\"{get_key_code(n)}\");"
        code += delay(100)
        code += f"\n    Keyboard.releaseAll();"
        code += delay(DEFAULT_DELAY)
        return
    return


if __name__ == '__main__':
    args = argparser.parse_args()
    script = args.ducky
    output = args.ino
    read_script(script)
    write_output(cfg.get("ENCODER", "ino_sample"), cfg.get("ENCODER", "keyword"), code, output)
    if args.verbose > 0:
        print(code)
    print("Has been converted!")

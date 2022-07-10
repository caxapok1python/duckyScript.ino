# Your payload

Now try to convert your payload

### Write Ducky Script

Create a new text file. I named it payload.txt

Write some "Ducky Code". For example, I wrote the code to open the command line

```
REM ----Title: Open Command Prompt as administrator

DEFAULT_DELAY 25

REM ----Open Windows Run
GUI r
STRING powershell Start-Process cmd -Verb runAs
ENTER
DELAY 1000
ALT y
```

### Convert it into Arduino code

Open current directory in Command Promt you like. Then use encoder:

```
python3 <path to encoder.py> -d <path to ducky script file> -i <path to Arduino file>
```

{% hint style="warning" %}
Replace `python3` with `python` in Windows
{% endhint %}

For example:

```
python3 encoder.py -d open_cmd/payload.txt -i open_cmd/open_cmd.ino
```

```
python encoder.py -d open_cmd/payload.txt -i open_cmd/open_cmd.ino
```

### Than load your script to Arduino

Perform similar actions to those on the previous [page](first-steps.md#open-arduino-ide-and-and-load-program-to-your-atmega32u4).

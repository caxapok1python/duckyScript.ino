# First steps

### How it works

First, let's figure out how this program works. This script converts code from the Ducky Scritp language into code that is understandable to the Arduino compiler.

### Run the example

Firstly open the Terminal in current direcroty

{% hint style="info" %}
You should open CMD or PowerShell if you use Windows system
{% endhint %}

Now type in command prompt:

```
python3 encoder.py -d ./example/payload.txt -i ./example/example.ino
```

{% hint style="warning" %}
Use `python` in Windows

```
python encoder.py -d ./example/payload.txt -i ./example/example.ino
```
{% endhint %}

### Open Arduino IDE && Load program to your ATmega32u4

![Arduino open window](<../.gitbook/assets/изображение (10).png>)

Press `Ctrl+O` and choose `example/example.ino`&#x20;

Now choose Arduino Leonardo

![](<../.gitbook/assets/изображение (3).png>)

Choose port

![](<../.gitbook/assets/изображение (6).png>)

Finally press `Ctrl+U`

# Get Nvidia jetpack version easly

Checker is a python script, where combined all versions of Jetpack boxes.
You can easly run and check what version of Nvidia Jetpack version in your box.

## Installation and Usage

Use the [python3](https://www.python.org/downloads/release/python-390/) to run script.

After installation python3 , you can use this command.
```bash
cd /root || exit 1 && wget https://raw.githubusercontent.com/thedevopsre/nvidia-jetpack/main/checker.py && python3 /root/checker.py > /root/output.txt
```

## Output

To get information you can cat output.txt file

```
cat /root/output.txt
```
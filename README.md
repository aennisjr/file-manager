# file-manager
Manage files in your Windows folders automatically. Clone the repository:

```git clone https://github.com/aennisjr/file-manager.git```

CD into the directory:

```cd file-manager```

Run the code:

```python manager.py```


### Optional command line arguments:

`-d` lets you define a directory to reorganize. For example:

```python manager.py -d C:\Users\ThinkPad\Documents\School```

If not supplied, the ```TARGET_DIR``` value defined in the code will be used instead.

`-f` lets you force move files. If a similar file with the same name in the destination already exists, the force flag automatically renames the file then moves it to the new location. Usage:

```python manager.py -f```

or:

```python manager.py -f -d C:\Users\ThinkPad\Documents\School```

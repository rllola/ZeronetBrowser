# Troubleshooting

## Fail to load plugins

Absolute path needs to be given to add the plugins.
in PluginManager.py (line 22)
```
#sys.path.append(self.plugin_path)
sys.path.append(os.path.join(os.getcwd(), self.plugin_path))
```

## Use Zeronet as a module

Create a file inside ZeroNet folder

`__init__.py`
```
import main
import Config
```

# Qt 5.11.2

Using Qt 5.11 because 5.10.1 qt.conf is broken and for windows

## PyQT 5.11.3 (Windows)

Using PyQt5 5.11.3 because of compile bug

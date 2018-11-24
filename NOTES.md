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

## QtWebEngineProcess Error

```
QTWEBENGINEPROCESS_PATH=$PWD/PyQt5/Qt/libexec/QtWebEngineProcess ./ZeronetBrowser
```

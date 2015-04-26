# Webassets Babel

Babel filter for [Webassets](https://webassets.readthedocs.org/en/latest/)

## Description

Turn your ES6+ code into ES5 friendly code using https://babeljs.io/

## Installation

```
npm install -g babel
pip install webassets-babel
```

## Using

First register filter:

```
from webassets.filter import register_filter
from webassets_babel import BabelFilter
register_filter(BabelFilter)
```

Then you can use it in your build process:

```
Bundle('file.js', filters='babel')
```

You can change babel binary using BABEL_BIN setting of your application.

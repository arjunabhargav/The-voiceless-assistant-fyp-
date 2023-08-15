# Project Setup

Follow the Steps below to set up the project requirements.

## Local Development

Create or start a virtual environment with Python 3.x.

```
cd env/Scripts
activate
```

## Update pip

```
pip install --upgrade pip
```

Install required packages:

```
pip install -r requirements.txt
```

## Route Modification (Optional | Not required)

In file `Braille_Image_to_text.py`

```py
model = load_model('<Use your braille_train.h5 model absolute path)>')
```

Or let it be the relative path `/project/braille_train.h5`
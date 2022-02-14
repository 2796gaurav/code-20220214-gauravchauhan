# Foobar

Solution for A problem statement

## Installation

1. download or clone the repo
  ```sh
  git clone https://github.com/2796gaurav/code-20220214-gauravchauhan.git
  ```
2. install packages in requirements.txt
  ```sh
  pip install -r requirements.txt
  ```
3. run command -  to run fastapi server
  ```bash
  python -m uvicorn main:app --reload 
  ```
4. Go to below URL to test API's in swagger
  ```sh
  http://127.0.0.1:8000/docs#/default/
  ```
  
## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## SIMPLE HOROSCOPE BOT USING RASA


- Step 1: Make a virtual environment

```
 virtualenv rasaenv --python=/usr/bin/python3
```

- Step 2: Activate the virtual env

```
source <path_to_venv>+/bin/activate
```

- Step 3: Install rasaX and rasa sdk

```
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

- Step 4: install remaining requirements

  ```
  pip install -r requirements.txt"
   ```

- Step 5: This is rough skeleton for building chatbot using rasa. So, kindly, add nlu data i.e. training text inside nlu.md and stories in stories.md.

- Step 6: Also, add actions in actions.py and custom component for autocorrect component too.

- Step 7: Add horoscope list and add the path to nlu.

- Step 8: Train rasa

```
rasa train

```

- Step 9: Run rasa shell and rasa actions

```
rasa run actions & rasa shell

```


EXAMPLE SAMPLE

![] (images/out.mp4)

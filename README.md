# ClickSocialWeb

Click social has both projects the back-end and the front-end

### Back-End

#### Setup
To run the back-end project it's necessary to install all the python package and run the
server with flask cli

First check if your environment has python 3.+ and virtualenv installed
```bash
  $ cd backend
  $ virtualenv venv
  $ source venv/bin/activate
  $ cd clicksocial/clicksocial
  $ pwd # Copy the value that this command will display
  $ export FLASK_APP=clicksocial/clicksocial.py # Substitute clicksocial with the last copied value
  $ cd ../
  $ pip install -e .
  $ flask run
  $ http://localhost:5000
```


### Front-End

#### Setup
To run the front-end project it's necessary to install all dependencies and run with
angular cli

```bash
  $ npm install # Install dependencies
  $ ng serve
```

#### Development server
Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

#### Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive/pipe/service/class/module`.

#### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

#### Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

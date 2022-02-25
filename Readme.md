# Cron Explainer ![travis-ci](https://app.travis-ci.com/diegosperes/cron-explainer.svg?branch=master)

It is a cli command which generate a human readable output from the cron expression making easier to understand when the command will execute.

    $ cron-explainer "*/15 0 1,15 * 1-5 /usr/bin/find"

    minute:         {0, 45, 30, 15}
    hour:           {0}
    day of month:   {1, 15}
    month:          {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    day of week:    {1, 2, 3, 4, 5}
    command:        /usr/bin/find

## How to contibute?

- Fork the project and clone it in your machine
- Introduce your changes
- Make sure the changes are aligned with the project code style using the following make command `format-code`
- Make sure all the tests are passing.
- Push the changes to your fork and create a PR from there.


## How to setup the local envinronment? 

This project was built with python3.9 please install it before continue. The make command `setup` will automatically create a virtualenv inside of the project directory called `.env_python3.9` and install all the dependencies needed.


## How to run the tests?

Run the make command `test` which will create the virtualenv if it is necessary.

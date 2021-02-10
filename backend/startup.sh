#!/bin/bash

# RUN Application

pyagent run -c /jcapp/appdynamics.cfg -- gunicorn -b 0.0.0.0:8000 manage:app

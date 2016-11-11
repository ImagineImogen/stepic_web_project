to start =>
        git clone https:github.com/ImagineImogen/stepic_web_project web
        cd web
        sh init.sh
        sudo gunicorn - b 0.0.0.0:8080 hello:app # where app is the name of python function

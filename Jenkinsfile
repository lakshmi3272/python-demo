pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 app.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export PYTHONPATH=$WORKSPACE
                    python -m pytest -v
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
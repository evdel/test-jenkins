pipeline {
    agent {
        docker {
            image 'python:3.5-alpine' 
        }
    }

    stages {
        stage('Test') {
            steps {
                sh 'pytest ./tests.py'  
            }
        }
    }
}

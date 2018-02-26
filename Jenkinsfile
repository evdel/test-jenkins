pipeline {
    agent {
        docker { image 'python:3.4-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'python --version'  
            }
        }
    }
}

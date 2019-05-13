pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'ls'
                    sh 'cd pydvd'
                    sh 'pylint *.py'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
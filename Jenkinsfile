pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'pylint pydvd/*.py'
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
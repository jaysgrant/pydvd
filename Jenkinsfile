pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'pylint --rcfile=pylint.cfg $(find . -maxdepth 2 -name "*.py" -print) MYMODULE/ > pylint.log' //|| exit 0'
                    sh 'cat pylint.log'
                }
            }
        }
    }

    post {
        always {
            recordIssues enabledForFailure: true, tool: pyLint()
            cleanWs()
        }
    }
}
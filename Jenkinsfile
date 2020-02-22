pipeline {

    agent {docker-python-worker}

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'pylint --rcfile=pylint.cfg pydvd/*.py --disable=W1202 --output-format=parseable --reports=no > pylint.log || echo "pylint exited with $?"'
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
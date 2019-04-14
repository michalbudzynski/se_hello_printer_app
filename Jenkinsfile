 pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
                sh 'make deps'
            }
        }
        stage('Test') {
            steps {
                sh 'make test_xunit || true'
		step($class: 'XunitBuilder',
			thresholds: [
				[$class: 'SkippedThreshold', failureThreshold: '0'],
				[$class: 'FailedThreshold', failureThreshold: '1']
			tools: [[$class: 'JunitType', pattern: 'test_result.xml']]])
            }
        }
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
    }
}

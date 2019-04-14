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
                sh 'make test'
            }
        }
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
	stage('Testxunit') {
            steps {
                sh 'make test_xunit || true'
		step([$class: 'XUnitBuilder',
			thresholds: [
				[$class: 'SkippedThreshold', failureThreshold: '0'],
				[$class: 'FailedThreshold', failureThreshold: '1']],
			tools: [[$class: 'JUnitType', pattern: 'test_results.xml']]])
            }
        }


    }
}

post {
      always {
        cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
        }
    }
}

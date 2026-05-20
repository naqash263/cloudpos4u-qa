pipeline {
    agent any

    environment {
        CI = "true"
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                sh '''
                    cd /workspace/cloudpos4u-qa

                    echo "Cleaning previous reports..."
                    rm -rf reports
                    mkdir -p reports
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    cd /workspace/cloudpos4u-qa

                    echo "Creating Python virtual environment..."
                    rm -rf .jenkins_venv

                    python3 -m venv .jenkins_venv
                    . .jenkins_venv/bin/activate

                    echo "Installing dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run UI and API Tests') {
            steps {
                withCredentials([
                    string(credentialsId: 'BASE_URL', variable: 'BASE_URL'),
                    string(credentialsId: 'API_BASE_URL', variable: 'API_BASE_URL'),
                    string(credentialsId: 'ADMIN_EMAIL', variable: 'ADMIN_EMAIL'),
                    string(credentialsId: 'ADMIN_PASSWORD', variable: 'ADMIN_PASSWORD')
                ]) {
                    sh '''
                        cd /workspace/cloudpos4u-qa

                        . .jenkins_venv/bin/activate

                        echo "Running Pytest UI and API tests..."
                        pytest tests/ui tests/api tests/ai -m "not ai_live" \
                          --html=reports/report.html \
                          --self-contained-html \
                          --alluredir=reports/allure-results
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    cd /workspace/cloudpos4u-qa

                    echo "Adding Allure environment metadata..."
                    cat > reports/allure-results/environment.properties <<EOF
Project=CloudPOS4U QA Automation
Environment=Jenkins Docker
Frontend=https://bakebite-pos.cloudpos4u.com
API=https://bakebite-pos.cloudpos4u.com/api
Browser=Chromium Headless
Framework=Pytest + Selenium + Requests
Reporting=Allure + Pytest HTML
CI=Jenkins
Performance=JMeter
Database=PostgreSQL
EOF

                    echo "Generating Allure report..."
                    allure generate reports/allure-results -o reports/allure-report --clean
                '''
            }
        }

        stage('Run JMeter Performance Test') {
            steps {
                sh '''
                    cd /workspace/cloudpos4u-qa

                    echo "Running JMeter performance test..."
                    rm -rf reports/jmeter-report
                    rm -f reports/jmeter-results.jtl
                    rm -f reports/jmeter.log

                    jmeter -n \
                      -j reports/jmeter.log \
                      -t performance/cloudpos4u-performance.jmx \
                      -l reports/jmeter-results.jtl \
                      -e \
                      -o reports/jmeter-report
                '''
            }
        }

        stage('Copy Reports to Jenkins Workspace') {
            steps {
                sh '''
                    cd /workspace/cloudpos4u-qa

                    echo "Copying reports to Jenkins workspace..."
                    rm -rf "$WORKSPACE/reports"
                    mkdir -p "$WORKSPACE/reports"

                    cp -r reports/* "$WORKSPACE/reports/"

                    echo "Reports copied:"
                    ls -la "$WORKSPACE/reports"
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true

            echo "Pipeline completed. Reports archived under Jenkins build artifacts."
        }

        success {
            echo "CloudPOS4U QA pipeline completed successfully."
        }

        failure {
            echo "CloudPOS4U QA pipeline failed. Check reports, screenshots, logs, and console output."
        }
    }
}
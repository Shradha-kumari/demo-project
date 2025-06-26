pipeline {
    agent { label "vinod" }
    environment {
    GCP_PROJECT = 'sonorous-charge-462106-g6'	
    BUCKET_NAME = 'test_cf_1234'
}

    stages {
        stage('copy') {
            steps {
                echo 'this will clone github'
                git url: "https://github.com/Shradha-kumari/demo-project.git", branch: "main"
                echo 'code clone done'
            }
        }
            stage('Authenticate to GCP') {
                steps {
                    withCredentials([file(credentialsId: 'gcp-creds', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                        gcloud config set project $GCP_PROJECT
                    '''
        }
      }
    }

            stage('Upload to GCS') {
            steps {
                sh '''
                echo "Uploading files to GCS..."
                gsutil -m cp -r * gs://$BUCKET_NAME
                '''
            }
            }
  }
}
    

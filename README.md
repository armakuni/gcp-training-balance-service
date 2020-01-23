# Balance Services

The project contains below:

- REST service running on Cloud Run
- Balance Worker running on Google Function

#### Environment variables

The service uses the below variables in its configuration. They all have default values as shown below if they are not otherwise specified:

BALANCE_NAMESPACE=account_balances(default)
PORT=5002(default)
APP_NAME=Balance Service App(default)

#### Requirements

- A Firestore instance up and running in your Google Cloud account
- google service account to access the Firestore

#### Refer below link for more detail about setting up the environment to use google Firestore

- https://cloud.google.com/firestore/docs/quickstart-servers


### To run linter

```bash
make lint
```

### To run tests

```bash
make tests
```

### To run the balance service locally

```bash
make run
```

### Deployment

#### Cloud Run

This repository contains a cloudbuild.yaml file to deploy this service on to cloud run.

```bash
gcloud builds submit --substitutions=_BALANCE_NAMESPACE="[BALANCE_NAMESPACE]"
```

#### Cloud Function

NOTE: for the services to function correctly, they must use the same ```[BALANCE_NAMESPACE]```, otherwise they will be interacting with different collections in Firestore.

This service uses a cloud function to retrieve messages from the balance updates topic and store them in the balance collection.
To deploy this, we must provide it with the name of the topic.
When running below commands ensure that you are in the root directory of this project.

Run below command to update the gcloud SDK

```bash
gcloud components update
```

Now we can deploy the function to listen to the topic and execute when a new message is received:

```bash
gcloud functions deploy store_account_balance_update --trigger-topic [BALANCE_UPDATES_TOPIC] --set-env-vars BALANCE_NAMESPACE=[BALANCE_NAMESPACE] --runtime python37 --source=balance_worker
```

where "store_account_balance_update" is the name of the function specified in the ```main.py``` file of balance_worker folder.
And should not be changed unless updated in the main.py with same name.

You will be prompted to allow unauthenticated invocations of this function.
Enter ```N``` as we do not want this function to be invoked by anything other than the topic we specified.

### API documentation

You can access the API documentation by launching the application and visiting [swagger ui](http://localhost:5002/docs/)

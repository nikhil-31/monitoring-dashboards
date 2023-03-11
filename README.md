Note: For the screenshots, you can store all of your answer images in the answer-img directory.

## Verify the monitoring installation
TODO: run kubectl command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

Take a screenshot of the output and include it here to verify the installation

![pods_and_services](https://user-images.githubusercontent.com/19944703/222135481-f4a3e3ed-0e7c-497f-842d-c614dea53def.png)

![Screenshot from 2023-02-28 22-22-27](https://user-images.githubusercontent.com/19944703/222135499-5780cf52-8c28-4fe1-8efd-5222db2d9030.png)

![Screenshot from 2023-02-28 22-24-35](https://user-images.githubusercontent.com/19944703/222135788-2adec79f-ec66-476a-bc9f-15fd3038bb6d.png)

![Screenshot from 2023-02-28 22-26-32](https://user-images.githubusercontent.com/19944703/222135795-1caa9ae2-ad65-4fcb-ae4d-9ad9ef934018.png)

## Setup the Jaeger and Prometheus source
TODO: Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![Screenshot from 2023-02-28 22-27-13](https://user-images.githubusercontent.com/19944703/222136029-97cbb6f4-e266-48b7-bf96-171aaeaf9c32.png)

## Create a Basic Dashboard
TODO: Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Screenshot from 2023-02-28 22-27-54](https://user-images.githubusercontent.com/19944703/222136120-571117f7-d577-4f78-8423-201d4fc70bd0.png)

![Screenshot from 2023-02-28 22-28-54](https://user-images.githubusercontent.com/19944703/222136142-4a63aa15-27f9-49a4-9493-1ac415ed6aad.png)


## Describe SLO/SLI
TODO: Describe, in your own words, what the SLIs are, based on an SLO of monthly uptime and request response time.

SLA -> The agreement you make with your clients
SLO -> The objectives the team must hit to meet the agreeent
SLI -> The real numbers of your performance

The SLO's objectives or goals of a team can be 99.5% uptime and less than 200ms latency
The SLI's are the actual measure of these objects, currently the service/ system can be 99.9% uptime
and 159ms latency in MAR 2023


## Creating SLI metrics.
TODO: It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

1. The average 20x or 30x responses of the web application for the month of MAR 2023 is 99%
2. It took an average of 1s for incoming requests to be served for the month of MAR 2023
3. 1.5% of the total incoming requests had 50x responses for the month of MAR 2023
4. The average CPU usage of the web applications for the month of MAR 2023 is 50%
5. The UI in the frontend application for the month of MAR 2023 took an average of 200ms to be served


## Create a Dashboard to measure our SLIs
TODO: Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure
 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![final_dashboard](https://user-images.githubusercontent.com/19944703/223995333-e4c2571d-f92b-4659-9574-37f4208c2d07.png)



## Tracing our Flask App
TODO: We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![Screenshot from 2023-03-01 17-45-09](https://user-images.githubusercontent.com/19944703/222136615-0073f571-04e2-4378-ae19-ee93b80f1879.png)

![Screenshot from 2023-03-01 14-06-18](https://user-images.githubusercontent.com/19944703/222136654-5d6b4ea7-b2a4-44d6-95d5-5b80f0d9709e.png)



## Jaeger in Dashboards
TODO: Now that the trace is running, let's add the metric to our current Grafana dashboard. 
Once this is completed, provide a screenshot of it here.

![jaeger](https://user-images.githubusercontent.com/19944703/224051225-2e75ed05-ae01-461a-ba82-7cc28f2ec3bf.png)

![Screenshot from 2023-03-09 19-43-07](https://user-images.githubusercontent.com/19944703/224051376-86253e65-524a-457b-912c-1466ae26886b.png)



## Report Error
TODO: Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing 
(400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer
 span to demonstrate how we can user a tracer to locate errors easily.

### TROUBLE TICKET

Name: Carl Pei

Date: MAR 2, 2023

Subject: Backend service's star endpoint returning 500

Affected Area: Backend service, star endpoint - /star

Severity: HIGH

Description: The star endpoint returns a 500 server error response,
analyzing the span, the mongodb database server is not available, 
causing the endpoint to connect to a mongodb database that does not exist.

![500](https://user-images.githubusercontent.com/19944703/223994026-cea2c05b-9599-4a26-98b5-8c1c1e0e8448.png)

## Creating SLIs and SLOs
TODO: We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

SLOs:
1. 99.95% uptime for month of MAR 2023
2. 0.05% error budget - 4xx and 5xx responses
3. Latency should be below 500ms
4. Monthly average CPU should be less than 60%
5. Monthly average memory usage should not exceed 600Mib

SLIs:
1. The average 20x or 30x responses of the web application for the month of MAR 2023 was 98%
2. 2% of total incoming requests had 5xx responses for the month of MAR 2023
3. It took an average of 500ms for incoming requests to be served for the month of MAR 2023
4. The average CPU usage was 55%
5. The average memory usage was 500Mib



## Building KPIs for our plan
TODO: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. The average 20x or 30x responses of the web application for the month of MAR 2023 was 98%
   - monthly uptime - This KPI indicates the total usability of the application
   - 20x code responses per month - this KPI indicates availability of the pages of the application
   - Monthly traffic - This KPI will indicate the number of requests served by the application
2. 2% of total incoming requests had 5xx responses for the month of MAR 2023
   - Monthly downtime - this KPI indicates the number of times the application was down
   - Errors per month - this KPI will indicate the monthly errors encountered in the application.
   - Monthly traffic - this KPI will indicate the number of requests served by the application.
3. It took an average of 500ms for incoming requests to be served for the month of MAR 2023
   - Average monthly latency - this KPI will indicate the time it took for the application to respond to requests.
   - Monthly uptime - this KPI indicates the total usability of the application.
   - Monthly traffic - this KPI will indicate the number of requests served by the application.
4. The average CPU usage was 55%
   - Average monthly CPU usage of pod used by the application - this KPI will indicate how much CPU is used by the source pod of the application.
   - Average monthly CPU usage of all the pods - this KPI will indicate how much CPU is used by all the pods required to run the application.
   - Monthly quota limit - this KPI will indicate whether the application is exceeding its usage of the CPU quota.
5. The average memory usage was 500Mib
   - Average monthly memory usage of pod used by the application - this KPI will indicate how much memory is used by the source pod of the application.
   - Average monthly memory usage of all the pods - this KPI will indicate how much memory is used by all the pods required to run the application.
   - Monthly quota limit - this KPI will indicate whether the application is exceeding its usage of the memory quota.


## Final Dashboard
TODO: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.

### GETTING STARTED

port forward for jaeger
```
kubectl port-forward service/simplest-query --address 0.0.0.0 16686:16686
```

port forward for grafana
```
kubectl port-forward service/prometheus-grafana --address 0.0.0.0 3000:80 -n monitoring
```

port forward for frontend service
```

kubectl port-forward service/frontend-service --address 0.0.0.0 8080:8080
```

port forward for backend service
```
kubectl port-forward service/backend-service --address 0.0.0.0 8081:8081
```
 
port forward for prometheus service
```
kubectl port-forward service/prometheus-operated -n monitoring --address 0.0.0.0 9090:9090
```

## scripts
### Shell Script to force delete pods
```shell
for i in pod/backend-app-6c556b676-sl2ch
  echo "kubectl delete $i --grace-period=0 --force"
  kubectl delete $i --grace-period=0 --force
done
```

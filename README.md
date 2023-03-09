**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation
*TODO:* run `kubectl` command to show the running pods and services for all components. 

Take a screenshot of the output and include it here to verify the installation

![pods_and_services](https://user-images.githubusercontent.com/19944703/222135481-f4a3e3ed-0e7c-497f-842d-c614dea53def.png)

![Screenshot from 2023-02-28 22-22-27](https://user-images.githubusercontent.com/19944703/222135499-5780cf52-8c28-4fe1-8efd-5222db2d9030.png)

![Screenshot from 2023-02-28 22-24-35](https://user-images.githubusercontent.com/19944703/222135788-2adec79f-ec66-476a-bc9f-15fd3038bb6d.png)

![Screenshot from 2023-02-28 22-26-32](https://user-images.githubusercontent.com/19944703/222135795-1caa9ae2-ad65-4fcb-ae4d-9ad9ef934018.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![Screenshot from 2023-02-28 22-27-13](https://user-images.githubusercontent.com/19944703/222136029-97cbb6f4-e266-48b7-bf96-171aaeaf9c32.png)


## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Screenshot from 2023-02-28 22-27-54](https://user-images.githubusercontent.com/19944703/222136120-571117f7-d577-4f78-8423-201d4fc70bd0.png)

![Screenshot from 2023-02-28 22-28-54](https://user-images.githubusercontent.com/19944703/222136142-4a63aa15-27f9-49a4-9493-1ac415ed6aad.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLIs or Service Level Indicators are measurable indicators of how the applications/ website/ service is faring compared
to the promise of the organization to its customers and stakeholders. This promise is also known as SLOs or Service 
Level Objectives

An Example, SLI for a monthly uptime is the rate of the 20x or 30x responses of the website in a total incoming
requests per month. For example, the average 20x or 30x responses of the web applications for the month of MAR 2023
is 96%

On the other hand, the SLI for a request response time is how long the request took to be served in actuality. for
example, it took an average of 1sec for incoming requests to be served in the month of MAR 2023

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. 
Describe in detail 5 metrics to measure these SLIs. 

1. The average 20x or 30x responses of the web application for the month of MAR 2023 is 96 %
2. It took an average of 1s  for incoming requests to be served for the month of MAR 2023
3. 1.5% of the total incoming requests had 50x responses for the month of MAR 2023
4. The average CPU usage of the web applications for the month of MAR 2023 is 50%
5. The login requests in the web application for the month of MAR 2023 took an average of 2seconds to be served

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want 
to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour 
period and take a screenshot.

![final_dashboard](https://user-images.githubusercontent.com/19944703/223995333-e4c2571d-f92b-4659-9574-37f4208c2d07.png)


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a 
screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to 
perform Jaeger traces on the backend service.

![Screenshot from 2023-03-01 17-45-09](https://user-images.githubusercontent.com/19944703/222136615-0073f571-04e2-4378-ae19-ee93b80f1879.png)

![Screenshot from 2023-03-01 14-06-18](https://user-images.githubusercontent.com/19944703/222136654-5d6b4ea7-b2a4-44d6-95d5-5b80f0d9709e.png)


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, 
provide a screenshot of it here.

![Screenshot from 2023-02-28 22-28-54](https://user-images.githubusercontent.com/19944703/222136142-4a63aa15-27f9-49a4-9493-1ac415ed6aad.png)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are 
seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of 
the tracer span to demonstrate how we can user a tracer to locate errors easily.


TROUBLE TICKET

Name: Carl Pei

Date: MAR 2, 2023

Subject: Backend service's star endpoint does not work

Affected Area: Backend service, star endpoint

Severity: High

Description: The mongo database, connection cannot be found.

### SCREENSHOTS

![500](https://user-images.githubusercontent.com/19944703/223994026-cea2c05b-9599-4a26-98b5-8c1c1e0e8448.png)

## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs 
that you would use to measure the success of this SLO.

SLI or Service Level Indicators are measurable indicators of how the application/website is faring 
compared to the promise of the organization to its customers and stakeholders. This promise is also known as 
SLOs or Service level Objectives

An example SLI for monthly uptime is the rate of the 20x or 30x (valid requests) responses of the website in a total 
incoming requests per month.

Another example is the request response time for the given request to be served. 

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well 
as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. The average 20x or 30x responses of the web application for the month of MAR 2023 is 97.99%
2. It took an average of 700ms for incoming requests to be served for the month of MAR 2023
3. 1.5% of the total incoming requests had 50x responses for the month of MAR 2023
4. The average CPU usage of the web application fo the month of MAR 2023 is 50%
5. The list api request took 2 seconds to be returned in MAR 2023

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing
your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are 
represented in the dashboard.  

![final_dashboard](https://user-images.githubusercontent.com/19944703/223995333-e4c2571d-f92b-4659-9574-37f4208c2d07.png)

### GETTING STARTED

1. port forward for jaeger
```
kubectl port-forward service/simplest-query --address 0.0.0.0 16686:16686
```

2. port forward for graphana
```
kubectl port-forward service/prometheus-grafana --address 0.0.0.0 3000:80 -n monitoring
```

3. port forward for frontend service
```

kubectl port-forward service/frontend-service --address 0.0.0.0 8080:8080
```

4. port forward for backend service
```
kubectl port-forward service/backend-service --address 0.0.0.0 8081:8081
```
 
5. port forward for prometheus service
```
kubectl port-forward service/prometheus-operated -n monitoring --address 0.0.0.0 9090:9090
```

### Shell Script to force delete pods
```shell
for i in pod/backend-app-6c556b676-sl2ch
  echo "kubectl delete $i --grace-period=0 --force"
  kubectl delete $i --grace-period=0 --force
done
```

sum(rate(flask_http_request_duration_seconds_sum{container=~"backend|frontend"}[5m])) / sum(rate(flask_http_request_duration_seconds_count{container=~"backend|frontend"}[5m])) 
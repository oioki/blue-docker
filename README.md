# Application
```
$ COLOR=blue python app.py
USER           COLOR          
two            blue           
three          blue           
samename       blue           
```

# Docker
```
$ docker build -t blue-docker .
...

$ docker run -e COLOR=blue blue-docker
USER           COLOR          
two            blue           
three          blue           
samename       blue           
```

# Docker Hub
```
docker login --username=oioki
docker tag blue-docker oioki/blue-docker
docker push oioki/blue-docker
```

# Kubernetes
```
$ kubectl create -f job.yaml
job "blue" created

$ kubectl describe jobs/blue
Name:           blue
...
  Normal  SuccessfulCreate  1m    job-controller  Created pod: blue-ppmc2

$ kubectl logs blue-ppmc2
USER           COLOR          
two            blue           
three          blue           
samename       blue           
```

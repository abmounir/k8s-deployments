# k8s-deployments
k8s deployments - Rolling updates | Blue/Green | Canary









## run prometheus and grafana

```bash 
kubectl port-forward deployment/prometheus-grafana 3000:3000
```
## run prometheus
```bash
kubectl port-forward svc/prometheus-operated   9090:9090
```

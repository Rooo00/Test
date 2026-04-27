# Troubleshooting

Comandos que ayudan a resolver problemas

## Terraform

```bash
# Si es necesario forzar la recreación de las instancias
terraform apply -replace="aws_instance.controller" -replace="aws_instance.worker"
```

## Kubernetes

Verificar la instalación del cluster

```bash
# Si algo falla, estos comandos ayudan a diagnosticar el problema:

# Dentro del controller
sudo systemctl status k3s.service
sudo ss -lntp | grep 6443
sudo kubectl get nodes -o wide

# Dentro del worker
sudo systemctl status k3s-agent --no-pager
sudo journalctl -u k3s-agent -n 50 --no-pager

# Desde la laptop
kubectl get nodes
```

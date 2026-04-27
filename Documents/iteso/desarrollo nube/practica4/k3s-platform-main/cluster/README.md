# Despliegue de un cluster k3s

Cluster de 2 nodos (1 controller + 1 worker) en AWS usando Terraform.

Este documento también cubre la instalación de k3s.

## Levantar el cluster

```bash
# Inicializar Terraform
terraform init

# Validar la configuración
terraform validate

# Revisar el plan de ejecución
terraform plan

# Crear la infraestructura
terraform apply -auto-approve
```

## Configurar `kubectl` en tu computadora

```bash
# Extraer la llave privada y la IP del controller:
terraform output -raw ssh_private_key > k3s.pem
chmod 600 k3s.pem
CONTROLLER_IP=$(terraform output -raw controller_public_ip)
echo "IP del controlador: $CONTROLLER_IP"

# Crear directorio de configuración de kubectl
mkdir -p ~/.kube

# Copiar el kubeconfig desde el controller
ssh -i k3s.pem ubuntu@$CONTROLLER_IP \
  "sudo cat /etc/rancher/k3s/k3s.yaml" | \
  sed "s/127.0.0.1/$CONTROLLER_IP/g" > ~/.kube/config

# Verificar que el cluster responde
kubectl get nodes
```

Ya puedes correr `kubectl apply -f <manifiesto>`

## Eliminar el cluster

Es muy importante que no olvides eliminar el cluster después de utilizarlo.

```bash
terraform destroy -auto-approve
```


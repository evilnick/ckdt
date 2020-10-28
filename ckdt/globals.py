# Useful globals for the Charmed Kubernetes Docs Tool

config_url = (
    "https://api.jujucharms.com/charmstore/v5/~containers/*charm*/archive/config.yaml"
)

# the github id for the charmed-kubernetes/kubernetes-docs repo
repo_id = 142455969

# The location of the markdown files in that repo
pages_dir = 'pages/k8s'

# a list of the 'core' charms for CK (the defined bundle doesn't include integrators etc)
core_list = [
"aws-iam",
"aws-integrator",
"azure-integrator",
"calico",
"canal",
"containerd",
"docker",
"docker-registry",
"easyrsa",
"etcd",
"flannel",
"gcp-integrator",
"kata",
"keepalived",
"kubeapi-load-balancer",
"kubernetes-master",
"kubernetes-worker",
"openstack-integrator",
"tigera-secure-ee",
"vsphere-integrator"
]
